import ipaddress
import argparse

from sys import exit as sysexit

parser = argparse.ArgumentParser()
parser.add_argument('--ip', action='store', dest='ipaddr', required=True, help='The IP address you want to check against the network policy')
parser.add_argument('--policy', action='store', dest='iplist', required=True, help='The list of ip addresses as returned from DESC NETWORK POLICY')

try:
	args = parser.parse_args()
except:
	parser.print_help()
	sysexit(0)

try:
	ip = ipaddress.ip_address(args.ipaddr)
except:
	print("{} doesn't seem to be a valid IPv4 address.".format(args.ipaddr))
	sysexit(1)

subnet_hit = False
policy_ip_list = args.iplist.split(',')

for policy_ip in policy_ip_list:
	if ipaddress.ip_address(ip) in ipaddress.ip_network(policy_ip, False): #setting the strict bit to False in case of less-than-perfect network definitions
		print("{} matches subnet/ip {}. This entry is in position {}. of the network policy.".format(ip, policy_ip, policy_ip_list.index(policy_ip) + 1))
		subnet_hit = True

if not subnet_hit:
	print("{} was not found in any of the subnets defined in the network policy.".format(ip))