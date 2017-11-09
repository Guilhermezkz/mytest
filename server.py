import socket
import pyaudio
from _socket import SOCK_DGRAM, AF_INET

UDP_IP = '127.0.0.1'
UDP_PORT = int(input('Enter the port you will use'))
ADDRESS = (UDP_IP, UDP_PORT)


sock = socket.socket(AF_INET, SOCK_DGRAM)
sock.bind(ADDRESS)


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    output=True, frames_per_buffer=CHUNK)

frames = []

while True:
    data, addr = sock.recvfrom(CHUNK * CHANNELS * 2)
    frames.append(data)
    try:
        stream.write(frames.pop(0), CHUNK)
        pass
    except Exception as e:
        raise e
    pass
