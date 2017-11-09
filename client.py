import socket
import pyaudio
from _socket import SOCK_DGRAM, AF_INET
import threading

UDP_IP = '127.0.0.1'
UDP_PORT = int(input('Enter the port you will use: '))
udp = socket.socket(AF_INET, SOCK_DGRAM)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    frames_per_buffer=CHUNK, input=True)


def main():
    stream.start_stream()
    create_threads()
    pass


def send():
    frames = []
    while True:
        data = stream.read(CHUNK)
        if data:
            frames.append(data)
            pass
        udp.sendto(frames.pop(0), (UDP_IP, UDP_PORT))
        pass
    pass


def create_threads():
    threads = list()
    t = threading.Thread(target=send)
    threads.append(t)
    t.start()
    pass


main()
