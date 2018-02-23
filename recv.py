from socket import *
import sys 
import playaudio
from multiprocessing import Process
HOST = ""
PORT = 5008
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

if __name__=="__main__":
    msg, address = s.recvfrom(8192)
    while True:
        p=Process(target=(playaudio.play),args=(msg,))
        p.start()
        msg, address = s.recvfrom(8192)
        p.join()
s.close()
sys.exit()
