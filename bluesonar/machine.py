import socket
from bluesonar.helper import bcolors as bc


class Machine():
    def __init__(self, client, port):
        self.client = client
        self.addr = client[1]
        self.mac = client[2]
        self.port = port
        self.dictName = dict 

    def onSuccess(self, client, addr, mac):
        self.dictName = {client: {'name': client, 'msg': 'Connected', 'addr': addr, 'mac': mac}}

    def onError(self, client, err, addr, mac):
        self.dictName = {client: {'name': client, 'msg': err, 'addr': addr, 'mac': mac}}

    def connect(self):
        socket.setdefaulttimeout(3.0)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:           
            try:
                s.connect((self.addr, self.port))
                self.onSuccess(self.client[0], self.addr, self.mac)
            except socket.error as err:
                if err.args[0] == 10061:
                    self.onSuccess(self.client[0], self.addr, self.mac)                
                else:
                    self.onError(self.client[0], err, self.addr, self.mac)
            s.close()            

    def fault_report(self, err):
        print(f"{bc.WARNING}Error: {err}{bc.ENDC}")


class Scales(Machine):
    def __init__(self, addr, port=135):
        super().__init__(addr, port)
