from socket import *
import sys 
import playaudio
from multiprocessing import Process,Queue
HOST = ""
PORT = 5008
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

def recv(q):
    msg,address=s.recvfrom(8192)
    q.put(msg)
if __name__=="__main__":
    msg, address = s.recvfrom(8192)
    while True:
        q=Queue()
        p=Process(target=recv,args=(q,))
        p.start()
        playaudio.play(msg)
        msg=q.get()
        p.join()
s.close()
sys.exit()
