from ncclient import manager

host = '10.255.64.90'
port = 830
username = "pmasadmin"
password = "adtran"
session = 'dpu'

with manager.connect_ssh(host=host, port=port, username=username, password=password, hostkey_verify=False) as netconf_manager:
    print 'made it'
