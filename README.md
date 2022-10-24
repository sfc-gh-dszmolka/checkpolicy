# checkpolicy
A very simple Python script based on the `ipaddress` library, trying to determine if a given IP address is within *any* of the subnets specified as part of a Snowflake network policy.

Current version takes a single IP , and a comma-separated list of IP's/CIDR ranges against which the IP will be checked.

## usage
```shell
usage: checkpolicy.py [-h] --ip IPADDR --policy IPLIST

optional arguments:
  -h, --help       show this help message and exit
  --ip IPADDR      The IP address you want to check against the network policy
  --policy IPLIST  The list of ip addresses as returned from DESC NETWORK POLICY
```

## example to check 4 random IP's against a fictive network policy
```shell
$ export POLICY="10.220.0.0/16,10.216.32.0/20,20.195.64.240/28,10.216.64.0/20,10.8.210.0/23,91.233.207.64/26,10.9.210.0/23,10.8.212.0/22,10.9.212.0/22,1.1.1.1"
$ for ip in 20.195.64.241 20.195.64.239 1.1.1.1 8.8.8.8; do python3 checkpolicy.py --ip "$ip" --policy "$POLICY"; done
```
```shell
20.195.64.241 matches subnet/ip 20.195.64.240/28. This entry is in position 3. of the network policy.
20.195.64.239 was not found in any of the subnets defined in the network policy.
1.1.1.1 matches subnet/ip 1.1.1.1. This entry is in position 10. of the network policy.
8.8.8.8 was not found in any of the subnets defined in the network policy.
```
