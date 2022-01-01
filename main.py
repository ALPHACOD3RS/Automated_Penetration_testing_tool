import nmap
import pyfiglet
import sys
import json
import socket
import re
from datetime import datetime


# target = '127.0.0.1'
# target = input()sc
# print("target")
ascii_banner = pyfiglet.figlet_format("CYBER TALENT")
print(ascii_banner)

scanner = nmap.PortScanner()
ip_addr= input("Please enter the IP address you want to scan: ")
ip = socket.gethostbyname(ip_addr)
print("The IP you entered is: ", ip)
type(ip_addr)

'''resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan 
                4)Version scan\n""")
print("You have selected option: ", resp)
'''

# Defining a target
if len(sys.argv) == 2:

    # translate hostname to IPv4
    ip_add = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

# Add Banner
print("-" * 50)
print("Scanning Target: " + ip_addr)
#print("Scanning started at:" + str(datetimcde.now()))
print("-" * 50)

try:

    # will scan ports between 1 to 65,535
    for port in range(1, 100):
        protocolname = 'tcp'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((ip_addr, port))
        if result == 0:
            print("port: %s >> service name: %s" %(port, socket.getservbyport(port, protocolname)))
            print(scanner.scan(ip_addr, arguments="-sV")['scan'][ip_addr])
            #print(scanner.csv())
            #line = scanner.readlines()
            x = scanner
            #'ipv4':.*'.\d+.\d+.\d+.\d+'
            m = re.match("'ipv4': '(\d+.\d+.\d+.\d+)'", x)


        s.close()

except KeyboardInterrupt:
    print("\n Exitting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()


