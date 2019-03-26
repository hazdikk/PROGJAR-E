import socket


SERVER_IP = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4']
SERVER_PORT = 9000
NAMAFILE=['gunter.jpg']
folder='client'


for IP in SERVER_IP:
    for file in NAMAFILE:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((IP, SERVER_PORT))

        fp = open(folder + '-' + IP + '/' + file,'wb+')
        ditulis=0

        while True:
            data, addr = sock.recvfrom(1024)
            print "blok ", len(data), data[0:10]
            fp.write(data)

        fp.close()
