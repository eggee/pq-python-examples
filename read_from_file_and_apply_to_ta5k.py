##############################################
#read from file and apply to shelf config
##############################################

import telnetlib

#ip
ip = "10.13.100.81"
#file path
filepath = "C:/temp/running_config.txt"
#open the file
my_file = open(filepath)
#read in the file
file_contents = my_file.read()
#split the file by carriage return and line feed
file_contents = file_contents.split("\n")
# file_contents = "show version\r\nshow version\r\n"
# file_contents = file_contents.split("\n")

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
tn.write('conf t\n')
print tn.read_until('#')
#write from file to the shelf
for line in file_contents:
    #print line
    tn.write(line + '\n')
    print tn.read_until('#')


tn.close()
my_file.close()
