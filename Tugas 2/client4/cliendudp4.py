import socket
import select

CLIENT_IP = "127.0.0.4"
CLIENT_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((CLIENT_IP, CLIENT_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print "menerima file ", data
        file_name = data

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], 5)
        if ready[0]:
            data, addr = sock.recvfrom(10240)
            f.write(data)
        else:
            print "%s telah diterima" % file_name
            f.close()
            break
