import socket
import os

def open_ports(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True

os.system('cls||clear')
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
host = input("Enter Target Mashine > ")
print("|_HOST   PORT   STATE")
for port in range(1, 1025):
    if open_ports(host, port):
        print("| ", host, "  ",port, "\033[32m OPEN \033[37m")
    else:
        pass
