import sys
import socket
from datetime import datetime


target_name=input("Define target: ") #The IP of the target
target=socket.gethostbyname(target_name) #If the target_name is a website, this returns the IPv4 address
write_file=open("Port scanning of "+ target +".txt","a") #The txt file which contains the information of the part scanning
print("Scanning started at: "+ str(datetime.now())) #notifies the user that the scanning 

try:
    for port in range(1,65535): # Scanning ports 1 to 65535, the ports of TCP and UDP sockets. 
        print(port) # for testing purposes, it may be omitted
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP port creation
        socket.setdefaulttimeout(1) # Take a 1 second break between closing and starting a new connection, it could have been a float
        result=s.connect_ex((target,port)) # TCP connect (UDP is connectless), connect_ex() also handles exceptions (result==0==connection established)in contrast to connect() 
        if result==0: # If the port is open and allows connection
            write_file.write("Port {} is open\n".format(port)) # Append the port result to the file
            write_file.flush() # Clear/Flush the .write buffer
        s.close() # close the socket
    print("Port scanning complete\n") # The current iteration is so slow, that it will take A LOT of time for the interpeter to actually run this line. I will use threading in the near future
    write_file.close() # Close the txt
except KeyboardInterrupt: # standatd socket error handling, aside from connectivity issues 
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
# As it currently stands, this program doesn't give a lot of usefull information about a network. In the upcoming update, i will include code to find the services of each port
# and possibly make use of the python threading module.
