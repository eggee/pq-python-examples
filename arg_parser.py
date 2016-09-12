##########################################################
#Run py calling 'python argParserExample.py --ip="1.2.3.4"'
#For usage run 'python argParserExample.py -h'
##########################################################

import argparse

parser = argparse.ArgumentParser(description='Description: example of how to use argParser')
parser.add_argument('--ip', help='ip address')
parser.add_argument('--slot', help='slot')
args = parser.parse_args()



if args.ip:
    ip = args.ip
if args.slot:
    slot = args.slot
    
    
print 'hey, this is your ip: ' + ip
print 'hey, this is your slot: ' + slot