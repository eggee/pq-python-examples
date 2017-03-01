import pytest
import time
import logging
from tbaas import TestBed

logging.basicConfig(level="DEBUG")

img_url = "http://release5.adtran.com/data/images/stable/MCP__18120000F1/16.05-1444/18120000F1-16.05-1444.ova"

@pytest.fixture(scope="session", autouse=True)
def testbed(request):
    """Make TBaaS MCP test bed instance"""
    testbed_name = "AUTO_BUILD_" + time.strftime("%Y.%m.%d-%H:%M:%S")
    testbed_config = {
        "heat_template_version": "2013-05-23",
        "resources": {
        "my-virtualbox": {
            "type": "VIRTUALBOX",
            "properties": {
                "img_url": img_url
                }
            }
        }
    }

    testbed = TestBed(testbed_config, tbaas_user='pq', tbaas_password='pq', name=testbed_name)
    testbed.start()
    def fin():
        testbed.stop()
    request.addfinalizer(fin)
    return testbed

@pytest.fixture(scope="session")
def host_ip(testbed):
    print testbed.attributes['my-virtualbox']['vm_ip']
    return testbed.attributes['my-virtualbox']['vm_ip']

