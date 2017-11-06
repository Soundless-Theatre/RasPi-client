import plaaudio
from websocket import create_connection
ws = create_connection("ws://localhost:9999")
while True:
    playaudio.play(ws.recv())
ws.close()
