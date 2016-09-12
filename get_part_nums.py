import telnetlib

#define a list
part_num_list = list()

#connect to shelf
tn = telnetlib.Telnet('10.11.5.16')
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
tn.write('show version\n')

#copy all output of the show version to string variable 'a'
output = tn.read_until('#')

#print output


#get the part num

#make a 'string array' or 'list' of the 'show version' output at each of the line-breaks
#eg a = ['line1', 'line2'], or,
#eg  a = ['show version\r', '1/1 TA5000 1187550E1 \r', '  Part Number  : 1187550E1\r', ....]
output_split = output.split("\n")

#print output_split


for line in output_split:
	#Check each line for the keyword 'Part Number'
    #print line
	if 'Part Number' in line:
		#Make a new 'string array' or 'list' appending all part numbers
		part_num_list.append(line.split()[3])

#print part_num_list
		
#print out each item (the part numbers) in the list
print "here be a list of ye part numbers:"
for part_num in part_num_list:
	print part_num