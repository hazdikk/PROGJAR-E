import socket
import time
import sys

SERVER_IP = ["127.0.0.1","127.0.0.2","127.0.0.3","127.0.0.4",];
SERVER_PORT = 9000
buf = 1024
NAMAFILE= ['gunter.jpg', 'bart.png']

for IP in SERVER_IP: 
	for file in NAMAFILE: 
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		sock.sendto(file, (IP, SERVER_PORT))
		print "mengirim %s" % file

		f = open(file, "rb")
		data = f.read()
		while(data):
		    if(sock.sendto(data, (IP, SERVER_PORT))):
		        data = f.read()

		sock.close()
		f.close()
		time.sleep(10)
