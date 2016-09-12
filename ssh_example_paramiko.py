#example ssh using paramiko
#can also utilize other ssh libraries
#including the taut/robot library http://robotframework.org/SSHLibrary/latest/SSHLibrary.html
#can utilize regular expressions to map varying prompts

import paramiko
import re
import time
import logging

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

class Ssh():
    """
    Library for ssh communication

    *Parameters* :
      - *ip*         : <string>    ; IP address
      - prompt       : <string>    ; A regular expression string defining the prompt, generally use default
      - port         : <int>       ; Port
      - username     : <string>    ; Username
      - password     : <integer>   ; Password
      - session      : <string>    ; A string defining the session type [ta5k|dpu|aoe|rpi]
      

    *Returns* : None

    Requirements:
    - paramiko
    MS Visual C++ Compiler -  http://aka.ms/vcpython27
    pip install --upgrade pip
    pip install paramiko

    mother of all prompts:
    (^|\\n)\S+[>#]$|\$|\[y\/n\]$|\nPassword:|\nUsername:|\ncli\s+(?!\[none\])\[\w+\].*>|\ncli\s+(?!\[none\])\[\w+\].*#
    """

    def __init__(self, ip, prompt='(^|\\n)\S+[>#]$|\$|\[y\/n\]$|\nPassword:|\nUsername:|\ncli\s+(?!\[none\])\[\w+\].*>|\ncli\s+(?!\[none\])\[\w+\].*#', port=22, username='ADMIN', password='PASSWORD', session='ta5k'):
        """
        Initialize the class
        """
        self.ip = ip
        self.prompt = prompt
        self.port = port
        self.username = username
        self.password = password
        self.session = session
        
    def __del__(self):
        """
        Deconstructor to close the ssh clients
        """
        self._sshClient.close()
        self._sshChannel.close()

    def createSshClient(self):
        """
        Creates a ssh client, invokes a shell and returns a channel to this shell.

        *Parameters* : None

        *Returns* : None
        """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ip, port=self.port, username=self.username, password=self.password, allow_agent=False)
            channel = client.invoke_shell(width=256)
            self._sshClient = client
            self._sshChannel = channel
        except:
            raise AssertionError('could not open ssh connection.')

        time.sleep(5)
        return client, channel

    def reconnectSshClient(self):
        """
        Checks if a ssh client is already open and, if so, checks if it is still active.
        Otherwise a new client is started. Returns the current ssh client.

        *Parameters* : None

        *Returns* : None

        """
        try:
            if self.getClientStatus():
                pass
            else:
                #reconnect ssh client
                logger.debug("DEBUG MSG::::>>>> SSH CLIENT RECONNECT")
                self._sshClient, self._sshChannel = self.createSshClient()

                #handle any necessary login procedures
                if "ta5k" in self.session.strip().lower() or "ta500" in self.session.strip().lower():
                    #session ta5k
                    self.execSshCommand("term len 0")
                elif "dpu" in self.session.strip().lower() or "pma" in self.session.strip().lower():
                    #session dpu
                    self.dpu_login()
                    self.execSshCommand("configure-terminal")
                else:
                    pass
        except:
            raise AssertionError("ssh client connection failed...")

        return self._sshClient, self._sshChannel

    def getClientStatus(self):
        """
        Get the client SSH status

        *Returns* : <boolean> status
        """
        return self._sshClient.get_transport().is_active()

    def execSshCommand(self, command, prompt=None):
        """
        Execute the CLI command on shenick.

        *Parameters*    :
        - *command*     : <string>  ; Command to be executed

        *Returns* : None
        """
        if prompt is None:
            prompt = self.prompt


        client, channel = self.reconnectSshClient()
        output = ''
        try:
            # clear leftovers
            while channel.recv_ready():
                channel.recv(1)
            # send the command
            channel.send(command + '\n')
            logger.debug("DEBUG MSG::::>>>> COMMAND EXECUTED: {0}".format(command))
            # wait until channel has data
            while not channel.recv_ready():
                time.sleep(0.1)
            # read until end of prompt
            while not re.search(prompt, output, re.IGNORECASE):
                while channel.recv_ready():
                    output += channel.recv(1)
            # check for errors
            if 'cli>ERROR:' in output:
                assert False, output

        except AssertionError as e:
            raise AssertionError('ssh command "%s" failed with error "%s"' % (command, e))

        # return output without command and prompt
        # print '\n'.join(output.splitlines()[1:-1])
        return '\n'.join(output.splitlines()[1:-1])

    def dpu_login(self, password=None):
        """
        Login to DPU

        *Parameters* :
        - password         : <string>    ; DPU password - defaults to session password = self.password

        """
        logger.debug("DEBUG MSG::::>>>> DPU LOGIN")
        if password is None:
            password = self.password

        self.execSshCommand("pma_cli")
        self.execSshCommand(password)


if __name__ == '__main__':

    #######################
    #EXAMPLES
    ######################


    #AOE
    # ip = "10.21.1.45"
    # port = 22
    # username = "emsadmin"
    # password =  "4150ems"

    # instance = Ssh(ip=ip, port=port, username=username, password=password)
    # instance.createSshClient()
    # output = instance.execSshCommand("ifconfig")
    # print output
    # ipv4 = re.findall('inet\s+(.*?)\s+netmask', output)
    # for ip in ipv4:
    #     print "Here be an IP address: {0}".format(ip)
    # print instance.execSshCommand("uname -a")
    # print instance.execSshCommand("ps aux | grep 'ps aux'")
 


    #RPi
    # ip = "10.13.100.6"
    # port = 22
    # username = "alarm"
    # password = "alarm"

    # instance = Ssh(ip=ip, port=port, username=username, password=password)
    # instance.createSshClient()
    # print instance.execSshCommand("ps aux")

    #DPU
    ip = "10.255.64.90"
    port = 22
    username = "pmasadmin"
    password = "adtran"
    session = 'dpu'

    instance = Ssh(ip=ip, port=port, username=username, password=password, session=session)
    instance.createSshClient()
    instance.dpu_login()
    print instance.execSshCommand("configure-terminal")
    for i in range(0,10):
        time.sleep(1)
        print instance.getClientStatus()
    print instance.execSshCommand("cli session dpu https://localhost:8443/dpudatastore/id=e62dpu1/restconf")
    print instance.execSshCommand("show interfaces-state interface 'gfast 0/1' oper-status")



    #TA5K
    # ip = "10.13.100.81"

    # instance = Ssh(ip=ip)
    # instance.createSshClient()
    # instance.execSshCommand("term len 0")
    # print instance.execSshCommand("show ver 1/a")
    # for i in range(0,10):
    #     time.sleep(1)
    #     print instance.getClientStatus()
    # print instance.execSshCommand("sho version 1/a")