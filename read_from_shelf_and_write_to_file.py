##############################################
#read from shelf and write to file
##############################################

import telnetlib
import time

#ip
ip = "10.13.100.81"
#output file path
my_file = "C:/temp/running_config_output_" + time.strftime("%b_%d_%Y_%H-%M-%S") + ".txt"


#print file_contents
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
tn.write('sho run top\n')
output = tn.read_until('#')
print output
output = output.split('\r\n')
#write from shelf to file
with open(my_file, 'w') as filename:
     for line in output:
        filename.write(line)
        filename.write('\n')


tn.close()

