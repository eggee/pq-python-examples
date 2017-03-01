from taut_hpqc import HpqcRest
import logging

#logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#variables
host = "td-almhp"
port = 8080
domain = "CND"
project = "TA5000"
username = "taut01"
password = "Qbttxpse!5"


flag_spooky_event = False
flag_mystery_machine = False
flag_scooby_snack = False
flag_set_the_trap = False
flag_meddling_kids = False


def spooky_event(text):
    flag_spooky_event = True
    return text
def mystery_machine(text):
    flag_mystery_machine = True
    return text
def scooby_snack(text):
    flag_scooby_snack = True
    return text
def set_the_trap(text):
    flag_set_the_trap = True
    return text
def meddling_kids(text):
    flag_meddling_kids = True
    return text


#create QC/ALM session instance
instance = HpqcRest(host, port, domain, project)
#login
instance.login(username, password)
#create a run for a given test
created_run = instance.run_create("my_test_name", 479228, "taut01")
print created_run
instance.run_get(_id=created_run['id'])
print instance._generic_entity_call(method="get", entity_type="runs/{0}/run-steps".format(created_run['id']))
#step 1
if spooky_event("monster from depth appears"): 
    pass
#some fake stuff
#push to QC - actual results field
#do some stuff
#some fake stuff
#push to QC -  - actual results field + attach a document
#...

#push/attach documents reports
#close session

