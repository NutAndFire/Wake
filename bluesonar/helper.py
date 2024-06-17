from datetime import datetime
from prettytable import PrettyTable


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

myTable = PrettyTable(["Date", "Name", "IP Address", "Status", "Message"])

def message(name, status, addr):   
    if status == "Connected":
        myTable.add_row([datetime.now(), name, addr, f"{bcolors.OKGREEN}✓{bcolors.ENDC}", ""])
    else:
        myTable.add_row([datetime.now(), name, addr, f"{bcolors.FAIL}☓{bcolors.ENDC}", status])

def printTable():
    myTable.align = "l"
    myTable.align["Status"] = "c"
    print(myTable)
    myTable.clear_rows()