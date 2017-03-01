from qcrest import QCREST
import logging
import time

# #logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

#variables
host = "td-almhp"
port = 8080
domain = "CND"
project = "TA5000"
username = "taut01"
password = "Qbttxpse!5"

run_flag = list()

def spooky_event_occurs():
    return True
def cue_mystery_machine():
    return False
def scooby_snack():
    return True
def set_the_trap():
    return True
def meddling_kids():
    return True

#create QC/ALM session instance
instance = QCREST(username, password, domain, project, "", "", host, port)
#login
instance.rest_authentication()
#create a run for a given test
instance.set_test_name("my_test_name")
instance.create_run("479228")

#start timer
time_start = time.clock()

#step 1
instance.set_design_step_name("spooky_event_occurs")
if spooky_event_occurs():
    instance.set_status("Passed")
    instance.set_actual_result("monster from depth appears")
else:
    run_flag.append(False)
    instance.set_status("Failed")
    instance.set_actual_result("not spooky enough")
instance.real_submit_step()    
    
#step 2
instance.set_design_step_name("cue_mystery_machine")
if cue_mystery_machine():
    instance.set_status("Passed")
    instance.set_actual_result("riding in the van")
else:
    run_flag.append(False)
    instance.set_status("Failed")
    instance.set_actual_result("flat tire")
instance.real_submit_step()


#step 3
instance.set_design_step_name("scooby_snack")
if scooby_snack():
    instance.set_status("Passed")
    instance.set_actual_result("chowing down on snacks")
else:
    run_flag.append(False)
    instance.set_status("Failed")
    instance.set_actual_result("not even for a scooby snack?")
instance.real_submit_step()    


#step 4
instance.set_design_step_name("set_the_trap")
if set_the_trap():
    instance.set_status("Passed")
    instance.set_actual_result("box propped up with a stick")
else:
    run_flag.append(False)
    instance.set_status("Failed")
    instance.set_actual_result("trap failed - trapped scooby on accident")
instance.real_submit_step()    

#step 5
instance.set_design_step_name("meddling_kids")
if meddling_kids():
    instance.set_status("Passed")
    instance.set_actual_result("another mystery solved!")
else:
    run_flag.append(False)
    instance.set_status("Failed")
    instance.set_actual_result("baddie got away!")
instance.real_submit_step()    

#push/attach documents reports
time_end = time.clock()
duration = str(int(round(time_end - time_start)))

if False in run_flag:
    instance.rest_finish_test(duration, "Failed")
else:
    instance.rest_finish_test(duration, "Passed")
#close session
instance.rest_logout()
