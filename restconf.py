import json
import requests
import logging
import time
import urllib


class Rest():
    """
    REST interaction library
    args = {
                hostname: device hostname
                port: device port
            }
    """
    def __init__(self, hostname, port):
        """
        class initialization
        """
        self.hostname = hostname
        self.port = str(port)


    def perform_generic_request(self, type, uri, body=None, header=None, auth=None, del_item=None, url_ip=True):
        """
        perform a generic HTTP request operation on NBI
        args = {
                    type: the operation request type [GET|PUT|POST|DELTE|NOTIFY]
                    uri: the url suffix.  Generally url = 'http/<hostname>:<port>/<uri>'
                    body: the data payload to send along with the request
                    header: the header information (like content-type) to send with the request
                    auth: the authentication to send with the request
                }
        """
        #build the url
        url = 'http://' + self.hostname + ':' + self.port + uri

        #print url
        #determine http request type and carry out the request returning status and content
        if type.upper() == 'GET':
            #perform GET request

            if auth:
                auth = auth
            else:
                auth = {}

            logging.info('HTTP REQUEST - GET')
            http_req = requests.get(url=url, auth=auth)
            return (http_req.status_code, http_req.content)
        elif type.upper() == 'PUT':
            #perform PUT request

            if body:
                body = body
            else: 
                body = {}
            if header:
                header = header
            else: 
                header = {}
            if auth:
                auth = auth
            else:
                auth = {}

            logging.info('HTTP REQUEST - PUT')
            http_req = requests.put(url=url, data=json.dumps(body), headers=header, auth=auth)
            return (http_req.status_code, http_req.headers, http_req.content)
        elif type.upper() == 'POST':
            #perform POST request

            if body:
                body = body
            else: 
                body = {}
            if header:
                header = header
            else: 
                header = {}
            if auth:
                auth = auth
            else:
                auth = {}

            logging.info('HTTP REQUEST - POST')
            http_req = requests.post(url=url, data=json.dumps(body), headers=header, auth=auth)
            return (http_req.status_code, http_req.headers, http_req.content)
        elif type.upper() == 'DELETE':
            #perform DELETE request

            if del_item:
                del_item = del_item
            else:
                del_item = ''

            logging.info('HTTP REQUEST - DELETE')
            url = url + del_item
            http_req = requests.delete(url)
            return (http_req.status_code, http_req.content)
        elif type.upper() == 'NOTIFY':
            logging.info('HTTP REQUEST - NOTIFY - NOT YET SUPPORTED')
            #notification not yet supported - have not had to use it yet
        else:
            #throw warning msg if unsupported request type
            logging.warning('UNSUPPORTED HTTP REQUEST TYPE! OPTIONS: [GET|PUT|POST|DELETE|NOTIFY]')


if __name__ == '__main__':


    ##########
    #TA5K
    ##########
    hostname = "10.13.100.81"
    port = ''
    instance = Rest(hostname, port)

    url_suffix = '/restconf/SNMPslot254/adtran-hello'
    auth = ('ADMIN', 'PASSWORD')
    print instance.perform_generic_request('GET', url_suffix, auth=auth)