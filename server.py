# This is server code to send video and audio frames over TCP

import socket
import threading, wave, pyaudio,pickle,struct

host_name = socket.gethostname()
host_ip = '192.168.4.1'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9633

CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 2                # single channel for microphone
RATE = 44100  

def audio_stream():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host_ip, port))

    # server_socket.listen(5)
    p = pyaudio.PyAudio()
    print('server listening at',(host_ip, (port)))
   
    
    s = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
    input_device_index=1
)


             

    message,addr = server_socket.recvfrom(1024)
 
    data = None
    while True:
        data = s.read(CHUNK)
        server_socket.sendto(data, addr)
                
t1 = threading.Thread(target=audio_stream, args=())
t1.start()

