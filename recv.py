import playaudio
from websocket import create_connection
ws = create_connection("ws://localhost:9999")
while True:
    playaudio.play(bytes(ws.recv()))
ws.close()
