#pip install --trusted-host pypi.adtran.com --upgrade -i http://pypi.adtran.com/simple taut_core
#pip install --trusted-host pypi.adtran.com --upgrade -i http://pypi.adtran.com/simple taut_ta5k

import taut_ta5k

host = "10.13.100.81"
alias = "ERPS_COT"
param_dict = {"slot": 1, "port": 1}

instance = taut_ta5k.communication.ta5k_telnet.Ta5kTelnet()
instance.connect(host=host, alias=alias)
print instance.interface_t1_config_get(param_dict)