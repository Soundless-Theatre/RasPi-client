import pyaudio
from socket import *
import sys 
from multiprocessing import Process,Queue

HOST = ""
PORT = 5008
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

def recv(q):
    msg,address=s.recvfrom(8192)
    q.put(msg)

CHUNK=128
RATE=16000
p=pyaudio.PyAudio()
stream=p.open( format = pyaudio.paInt16,
              channels = 2,
              frames_per_buffer = CHUNK,
              input = False,
              output = True)

if __name__=="__main__":
    msg, address = s.recvfrom(8192)
    while True:
        q=Queue()
        p=Process(target=recv,args=(q,))
        p.start()
        stream.write(msg)
        msg=q.get()
        p.join()
s.close()
sys.exit()
