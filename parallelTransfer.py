#!/usr/bin/env python3 

###### IMPORT #####
from multiprocessing import Pool, Queue
import time
import os
import sys
import itertools
import glob
import subprocess

# --DISCLAIMER--

# This is currently very rough, use at your own risk.
# m5copy implementation only supports transferring from 'file' type

# --USAGE-- 

# ./parallelTransfer.py <file_name(s)> <destination> <number_of_parallel_processes> <transfer_client>

# When using wild cards for file, make sure you enclose file call in ''
# Destination should be in the standard format you would use for 'etransfer' or 'm5copy'

# If using m5copy and number of parallel processes exceeds number of available UDP 
# ports, nothing will happen (maybe), but it will be constrained to the number of 
# ports available.
# Transfer client 0 for etransfer or 1 for m5copy - defaults to m5copy

# --MANUALLY EDIT--

# etransfer client location:
etc = '~/etransfer/Linux-x86_64-native-opt/etc'

# Define available UDP ports (open on destination) for m5copy transfers.
udp_ports = [2640, 2641, 2642, 2643, 2644, 2645, 2646, 2647, 2648, 2649, 2650, 2651, 2652, 2653, 2654]
free_udp_ports = Queue() # start port queue

# -----------------------------------------------------------------------------

def transfer(transfer_file): # Remnant of testing
    time.sleep(3)
    os.system('cp ' + transfer_file + ' ' + destination)
    print(etc + transfer_file + ' ' + str(destination))
    return
    
def etransferFunc(transfer_file):
    os.system(etc + ' ' + transfer_file + ' ' + str(destination))
    print(transfer_file + ' being sent to ' + str(destination))
    return
    
def m5copyFunc(transfer_file):
    free_port = free_udp_ports.get() # block until a free udp port is available
    #os.system('m5copy --resume -udt -p 2630' + ' file://' + transfer_file + ' ' + destination)
    try:
        os.system('m5copy --resume -udt -p ' + str(free_port) + ' file://' + transfer_file + ' ' + destination + ' > /dev/null')
        print(transfer_file + ' transferred.')
    finally:
        free_udp_ports.put_nowait(free_port) # release port back to the queue
    return   
   
def main(tag, num_proc, transfer_client=1):
    # Initialise available ports
    for port in udp_ports:
        free_udp_ports.put_nowait(port)
    # Parse file argument and create list of files for transfer
    file_list = glob.glob(str(tag)) # using glob as it supports wildcards
    # Pick transfer method depending on command line argument
    if transfer_client == 0:
        print('Using etransfer client...')
        with Pool(int(num_proc)) as p:
            p.map(etransferFunc, file_list)
    elif transfer_client == 1:
        print('Using m5copy client...')
        with Pool(int(num_proc)) as p:
            p.map(m5copyFunc, file_list)          
    else:
        print('Please pick a valid transfer client - use 0 for etransfer or 1 for m5copy')

if __name__ == "__main__":
    destination = sys.argv[2] # this needs to be set here, as Pool.map() only supports one iterable argument
    main(sys.argv[1], sys.argv[3], sys.argv[4])
