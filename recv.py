import pyaudio
from socket import *
import sys 
from threading import Thread

frames=[]

def recv():
    HOST = ""
    PORT = 5008
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind((HOST,PORT))
    while True:
        msg,address=s.recvfrom(8192)
        frames.append(msg)

def play(stream):
    while True:
        if len(frames) > 0:
            stream.write(frames.pop(0))

CHUNK=1024
RATE=16000
p=pyaudio.PyAudio()
stream=p.open(format = pyaudio.paInt16,
              channels = 2,
              rate = RATE,
              frames_per_buffer = CHUNK,
              input = False,
              output = True)

if __name__=="__main__":
    p1=Thread(target=recv)
    p2=Thread(target=play,args=(stream,))
    p1.setDaemon(True)
    p2.setDaemon(True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
s.close()
sys.exit()
