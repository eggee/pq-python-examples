import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG)

#example to create an interface on MOSAIC using REST

mcp_ip = "10.255.64.39"
protocol = "https"
headers = {'content-type': 'application/json'}
auth = ('ADMIN', 'PASSWORD')
data = {
    "input":{
    "interface-context":{
        "interface-name": "1234_OTHER",
        "interface-type": "gigabit-ethernet",
        "number-of-lower-layer-interfaces": 0
        }
    }
}

uri = "{0}://{1}/api/restconf/operations/adtran-cloud-platform-uiworkflow:create".format(protocol, mcp_ip)
print requests.post(uri, headers=headers, auth=auth, data=json.dumps(data), verify=False)