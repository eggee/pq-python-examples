from taut_hpqc import HpqcRest

host = "td-almhp"
port = 8080
domain = "CND"
project = "TA5000"
username = "username"
password = "password"

instance = HpqcRest(host, port, domain, project)
instance.login(username, password)
# instance.run_create(your_test_name, test_instace_id, owner, etc)
instance.run_create("my_test_name", 447573, "taut01")
