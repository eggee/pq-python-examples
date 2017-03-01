import time
import telnetlib
import re

#some variables
ip = '10.213.253.34'
slot = '7'
count = 100
loop_dict = dict()
off_hook = dict()

#connect to shelf
tn = telnetlib.Telnet(ip)
#login
tn.read_until('Username:')
tn.write('ADMIN\n')
test = re.compile(b"Password:")
print test
tn.expect([test])
tn.write('PASSWORD\n')
#look for the prompt
tn.read_until('>')
tn.write('enable\n')
tn.read_until('#')
tn.write('term len 0\n')
tn.read_until('#')

while True:
    tn.write('show table int fxs 1/{0}'.format(slot) + "\n")
    output = tn.read_until('#')
    output = output.split("\r\n")
    for line in output[4:-1]:
        status = re.match("fxs\s(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s", line)
        interface = status.group(1)
        loop_status = status.group(5)
        loop_dict[interface] = loop_status
    for key, value in loop_dict.iteritems():
        if value == "Off-Hook":
            off_hook[key] = value
    
    temp =  off_hook
    time.sleep(5)
    # print loop_status
    # if status.group(5) == "Off-Hook"
    #     print status.group(1), status.group(5)

    #fxs\s(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s
    # print output


