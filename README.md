# parallelTransfer.py
Small python wrapper script for parallel usage of transfer clients 'etransfer' and 'm5copy'

# DISCLAIMER 

This is currently very rough, with no error handling and absolutely no gaurantee it will not do something terrible, use at your own risk.

m5copy implementation only supports transferring from 'file' type

# USAGE 

./parallelTransfer.py <file_name(s)> <destination> <number_of_parallel_processes> <transfer_client>

When using wild cards for file, make sure you enclose file call in ''
Destination should be in the standard format you would use for 'etransfer' or 'm5copy'
if using m5copy and number of parallel processes exceeds number of available UDP ports, nothing will happen (maybe), but it will be constrained to the number of ports available.
Transfer client 0 for etransfer or 1 for m5copy
