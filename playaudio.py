# -*- coding:utf-8 -*-
import pyaudio
CHUNK=128
RATE=16000
p=pyaudio.PyAudio()
stream=p.open(	format = pyaudio.paInt16,
		channels = 2,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = False,
		output = True) # inputとoutputを同時にTrueにする
def play(sau):
    output = stream.write(sau)
