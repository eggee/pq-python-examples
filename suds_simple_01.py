from suds.client import Client
import logging
import time

logging.basicConfig(level=logging.CRITICAL)

# xml_i_want_to_send ="""
# <?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
#   <SOAP-ENV:Header>
#     <models:aoewsHeader xmlns:models="http://models.ws.common.adtran.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="models:aoewsHeader">
#       <operationStatus>
#         <status>SUCCESS</status>
#         <statusMessage/>
#       </operationStatus>
#       <operationName/>
#       <transactionId/>
#       <sessionId/>
#       <aoewss>
#         <userName>jmcclain</userName>
#         <password>jmcclain7227</password>
#       </aoewss>
#       <messageType>REQUEST</messageType>
#     </models:aoewsHeader>
#   </SOAP-ENV:Header>
#   <SOAP-ENV:Body>
#     <serviceactivation:getConfiguredServicesRequest xmlns:serviceactivation="http://serviceactivation.models.ws.common.adtran.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="serviceactivation:getConfiguredServicesRequest">
#       <subscriberId>ERPS00103103</subscriberId>
#     </serviceactivation:getConfiguredServicesRequest>
#   </SOAP-ENV:Body>
# </SOAP-ENV:Envelope>
# """

url = "http://10.21.1.45/aoe/ManageServiceProvisioning?wsdl"

client = Client(url)

#get a list of services
print client



# aoe_header.aoewss.password = password
# aoe_header.aoewss.userName = user
# aoe_header.transactionId = 'getConfiguredServices- 12:59:59,2016-04-21'

# client.set_options(soapheaders=auth)





# aoe_header = client.factory.create('aoewsHeader')
# client.set_options(soapheaders=aoe_header)
# client.service.authenticateUser("jmcclain")
# client.service.suspendService("ERPS00103103", "CUSTOM" )
# time.sleep(5)
client.set_options(soapheaders=headers)
client.service.resumeService(subscriberId="ERPS00103103", serviceType="CUSTOM")
# print client.service.getConfiguredServices(subscriberId="ERPS00103103")
# client.service.getConfiguredServicesResponse(xml_i_want_to_send)

# print client.envelope
# print client.last_received().str()


#getConfiguredServices
# equipId             :  1021171
# customServiceStatus :  ENABLED
# serviceTemplateName :  ERPS_map_GponDataVideo
# circuitId           :  ERPS00103103
# success             :  true
# serviceConfigured   :  true
# bondedService       :  false
# serviceType         :  CUSTOM
# templateName        :  ERPS_map_GponDataVideo
# circuitDescription  :  ERPS00103103
# subscriberId        :  ERPS00103103
