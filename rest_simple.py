import requests

url = 'http://10.13.100.81/restconf/SNMPslot254/adtran-hello'
auth = ('ADMIN', 'PASSWORD')
http_req = requests.get(url=url, auth=auth)
print http_req.status_code, http_req.content