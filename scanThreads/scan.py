import threading
from queue import Queue
from bluesonar.machine import Scales
from bluesonar.helper import message
from bluesonar.helper import bcolors as bc
from wakeOnLan.wol import Wol


class Scan(object):      
    def __init__(self):
        self.results = {}
        self.sorted_results = {}   

    def connectThread(self, client):    
            scale = Scales(client.get())     
            scale.connect()                        
            client.task_done()
            self.results[scale.client[0]] = scale.dictName.get(scale.client[0])

    def scanNow(self, clients):
        try:
            q = Queue(maxsize=0)
            num_threads = len(clients)

            for _ in range(num_threads):           
                worker1 = threading.Thread(target=self.connectThread, args=(q, ), daemon=True)
                worker2 = threading.Thread(target=self.connectThread, args=(q, ), daemon=True)
                
                worker1.start()
                worker2.start()          

            for client in clients:
                q.put(client)
                
            q.join()

            self.sorted_results = {key: value for key, value in sorted(self.results.items())}
            
            for site in self.sorted_results.keys():
                message(self.sorted_results[site]['name'], self.sorted_results[site]['msg'], self.sorted_results[site]['addr'])                
               
                if self.sorted_results[site]['msg'] == 'Connected':
                    continue
                else:
                    Wol().wol(self.sorted_results[site]['mac'])                  
            
        except KeyboardInterrupt:        
            print("\nCtrl+c pressed, Exiting...")
            q.join()