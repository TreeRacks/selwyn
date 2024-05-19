"""PyAudio Example: Record a few seconds of audio and save to a wave file."""

import wave
import sys
import numpy as np

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

with wave.open('rightbowie.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = s = p.open(
                        format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=1
                        )

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        sdata = stream.read(CHUNK)
        data = np.fromstring(sdata, dtype=np.uint16)
        print(data.shape)
        ch_data = data[1::2]
        wf.writeframes(ch_data.tostring())
    print('Done')

    stream.close()
    p.terminate()