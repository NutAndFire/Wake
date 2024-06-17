import os
import time as t
from bluesonar.helper import bcolors as bc
from bluesonar.helper import printTable
from scanThreads.scan import Scan
from datetime import datetime, time


# Below is my test sample, FORMAT is NAME, IP Address and MAC. It need to be a tuples within a list.
client = [('WDM-DT-IT-004', '10.1.0.92', b"\xa4\xbb\x6d\xb7\x31\x74"),
          ('WDM-DT-IT-TEST', '10.1.0.93', b"\xde\xad\xbe\xef\x00\x01"),
          ('WDM-DT-IT-TEST2', '10.1.0.94', b"\xde\xad\xbe\xef\x00\x02")
         ]

begin_time = time(5,30)
end_time = time(22,00)

if __name__ == "__main__":    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            today = datetime.today().isoweekday()                        
            if today >= 1 and today <= 5:             
                check_time = datetime.now().time()
                if begin_time < end_time:
                    if check_time >= begin_time and check_time <= end_time:
                        scan = Scan()
                        scan.scanNow(clients=client)
                        printTable()
                        # Sleeps for 45 Seconds
                        t.sleep(45.0)
                    elif check_time >= begin_time or check_time <= end_time:
                        print(f"[>] Out of hours {datetime.now()}\n")
                        # Sleeps for 30 mins
                        t.sleep(900.0)
                else:
                    print(f"{bc.WARNING}[!!] Check begin and end times as they seem to be wrong!{bc.ENDC}")
                    input("Press Enter to continue...")
                    exit(1)
            else:
                if today == 6:
                    print(f"[>] Today is Saturday {datetime.today().now()}")
                    t.sleep(21600.0)
                elif today == 7:
                    print(f"[>] Today is Sunday {datetime.today().now()}")
                    t.sleep(21600.0)
                else:
                    print(f"[>] Error unknown day!")
                    t.sleep(21600.0)                
        except KeyboardInterrupt:        
            print("\n[!] Ctrl+c pressed, Exiting...")
            quit()
