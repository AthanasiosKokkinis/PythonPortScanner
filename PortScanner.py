import sys
import socket
from datetime import datetime


target_name=input("Define target: ")
target=socket.gethostbyname(target_name)
write_file=open("Port scanning of "+ target +".txt","a")
print("Scanning started at: "+ str(datetime.now()))

try:
    for port in range(1,65535):
        print(port)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        if result==0:
            write_file.write("Port {} is open\n".format(port))
            write_file.flush()
        s.close()
    print("Port scanning complete\n")
    write_file.close()
except KeyboardInterrupt:
    print("\nKeyboard interruption\n")
    write_file.close()
    sys.exit()
except socket.gaierror:
    print("\nCouldn't resolve hostname\n")
    write_file.close()
    sys.exit()
except socket.error:
    print("\nSocket error\n")
    write_file.close()
    sys.exit()
    
