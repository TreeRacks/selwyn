# Welcome to PyShine
# This is client code to receive video and audio frames over UDP

import socket
import threading, wave, pyaudio, time, queue
import numpy as np
from led import initMatrix, animateFrame

initMatrix()

host_name = socket.gethostname()
host_ip = '192.168.4.1'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9633
# For details visit: www.pyshine.com
q = queue.Queue(maxsize=2000)

def audio_stream_UDP():
	BUFF_SIZE = 65536
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
	# p = pyaudio.PyAudio()
	CHUNK = 10*1024
	# stream = p.open(format=p.get_format_from_width(2),
	# 				channels=2,
	# 				rate=44100,
	# 				output=True,
	# 				frames_per_buffer=CHUNK)
					
	# create socket
	message = b'Hello'
	client_socket.settimeout(5)
	client_socket.sendto(message,(host_ip,port))
	socket_address = (host_ip,port)
	def getAudioData():
		while True:
			frame,_= client_socket.recvfrom(BUFF_SIZE)
			q.put(frame)
			print(f"Queue size: {q.qsize()}")
	t1 = threading.Thread(target=getAudioData, args=())
	t1.start()
	time.sleep(5)
	print('Now Playing...')
	print("")

	ralen = 5

	ral = [0] * ralen
	rar = [0] * ralen
	
	while True:
		frame = q.get()
		data = np.fromstring(frame, dtype=np.uint16)
		left_ch = data[0::2]
		right_ch = data[1::2]
		
		coeff = 10
		
		def getVol(ch):
			return coeff * np.log10(np.vdot(ch, ch) / len(ch))
		left_vol =  getVol(left_ch)
		right_vol = getVol(right_ch)
		
		ral.pop(0)
		ral.append(left_vol)

		rar.pop(0)
		rar.append(right_vol)

		lva = np.sum(ral) / ralen
		rva = np.sum(rar) / ralen

		animateFrame(lva, rva)
		# total_vol = left_vol + right_vol

		# lvp = left_vol/total_vol
		# rvp = right_vol/total_vol

		# bvp = (rvp - lvp) * 100
		print(f"{left_vol:.2f}, {right_vol:.2f}")
		# print(f"{lvp:.2f}, {rvp:.2f}")
		# print(f"{bvp:.2f}", end="\r")
		# stream.write(frame)

	client_socket.close()
	print('Audio closed')
	os._exit(1)



t1 = threading.Thread(target=audio_stream_UDP, args=())
t1.start()

