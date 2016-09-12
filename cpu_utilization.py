#example call to this script: python cpu_utilization.py -i 10.13.100.81 -s 5

import time
import getopt
import sys
import telnetlib

#set some default variables
ip = '10.13.100.81'
slot = 12


#allow for cmd arguments to pass lists and file name
try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:s:", ["help", "ip=", "slot="])
except getopt.GetoptError as err:
	print "usage: python {0} -h <help> -i <ip_address> -s <slot>".format(sys.argv[0])
	print str(err) # will print something like "option -a not recognized"
	sys.exit()

for o, a in opts:
	if o == "-h":
		print "usage: python {0} -h <help> -i <ip_address> -s <slot>".format(sys.argv[0])
		sys.exit()
	elif o == "-i":
		ip = a
	elif o == "-s":
		slot = a


#connect to shelf
tn = telnetlib.Telnet(ip)
#login
tn.read_until('Username:')
tn.write('ADMIN\n')
tn.read_until('Password:')
tn.write('PASSWORD\n')
#look for the prompt
tn.read_until('>')
tn.write('enable\n')
tn.read_until('#')
tn.write('term len 0\n')
tn.read_until('#')

#for n in range(0, 1000):
while True:
	tn.write('show proc sum 1/{0}'.format(slot) + "\n")
	utilization = tn.read_until('#')

	#print utilization
	utilization = utilization.split("\r\n")
	#print utilization

	#loop through each line of the 'show proc sum' output
	for line in utilization:
		if "Current" in line:
			#print line
			line = line.split()
			y = line[4]
			y = y.split("%")[0]
			print y



