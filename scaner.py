#import libraries
import socket  #conenct to target port
import os      #make some system commands

def open_ports(host, port):   #see if port is open
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False  #port is close
    else:
        return True   #port is open

    # \033[32m = Green
    # \033[37m = White
    # \033[31m = Red
    
os.system('cls||clear')
print("\033[32m ")   #print ascii art
print(r"""  
                 .-'''/.\
                 (_.--'  |
                  |  ==  |
             o-._ .--..--. _.-o
                 |   ||   |
                  ;--|`--:
                  |. |   |
                  |  ;_ .|
                  |_____ |
                 /|     '|\
                 //`----'\\
                ////|  |  \\
                /   |  |    \
                   /|  |\
                  / \  / \ Port Scanner
                 /   \/   \   By Megalodon
                /          \
                |          |
               ||    /\    ||
               ||   ,  .   || """)
host = input("\033[37mEnter Target Machine \033[32m > \033[37m ")
print("|_HOST   PORT   STATE")
for port in range(1, 1025):  #scanning first 1024 ports '65535 in total'
    if open_ports(host, port):
        print("| ", host, "  ",port, "\033[32m OPEN \033[37m") #display open ports
    else:
        pass   #dont print closed ports
