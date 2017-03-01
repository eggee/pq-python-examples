from suds.client import Client
import logging

# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)

url = "http://www.webservicex.net/geoipservice.asmx?WSDL"

client = Client(url)

# list the available services
# print client

#send the message and print the reply
response = client.service.GetGeoIP(IPAddress='8.8.8.8')
print response
