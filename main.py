import pyaudio
import numpy as np
p = pyaudio.PyAudio()
devices = [p.get_device_info_by_index(i) for i in range(p.get_device_count())]

for i in devices:
    print(i)

# constants
CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 2                # single channel for microphone
RATE = 44100                 # samples per second
# create matplotlib figure and axes
# pyaudio class instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
s = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
    input_device_index=1
)

# 8
# 11

try:
    while True:
        # binary data
        data = s.read(CHUNK)    

        data_np = np.frombuffer(data, dtype='h')
        print(data_np[data_np != 0])
except:
    print("Terminating")