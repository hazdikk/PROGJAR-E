import socket
import os

TARGET_IP = "127.0.0.2"
TARGET_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

namafile="bart.png"
ukuran = os.stat(namafile).st_size


fp = open('bart.png','rb')
k = fp.read()
terkirim=0
for x in k:
   sock.sendto(x, (TARGET_IP, TARGET_PORT))
   terkirim = terkirim + 1
   print "\r terkirim {} of {} " . format(terkirim,ukuran)
