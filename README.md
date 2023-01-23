# parallelTransfer.py
Small python wrapper script for parallel usage of transfer clients 'etransfer' and 'm5copy'

# Disclaimer 

This is currently very rough, with no error handling and absolutely no gaurantee it will not do something terrible, use at your own risk.

m5copy implementation only supports transferring from 'file' type

# Usage 

parallelTransfer.py <file(s)> <destination_m5copy_format> <number_processes> <transfer_client_id>

When using wild cards for file, make sure you enclose file call in ''

Destination should be in the standard format you would use for 'etransfer' or 'm5copy'

if using m5copy and number of parallel processes exceeds number of available UDP ports, nothing will happen (maybe), but it will be constrained to the number of ports available.

Transfer client 0 for etransfer or 1 for m5copy

# TO-DO

* Add proper stdout handling
* Add support for transferring from vbs type