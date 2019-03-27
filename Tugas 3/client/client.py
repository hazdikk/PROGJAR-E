import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
namafile=["gunter2.jpg"]

asd = '1'
sock.send(asd)
msg = sock.recv(1024) 
print 'File yang terdapat pada server'       
print msg

try:
    print "Menu : 1. Request File 2. Send File 3. Close"
    while True:
        req = raw_input('masukkan pilihan : ')
        sock.send(req)
        
        if(req== '1'):
            namanya = raw_input('nama file yang direquest : ')
            sock.send(namanya)
            counter = sock.recv(32)
            print counter
            if(counter == '1'):
                while True:
                    data = sock.recv(32)
                    if(data[0:5]=="START"):
                        print data[12:]
                        fp = open(data[12:],'wb+')
                        ditulis=0
                    elif(data[0:4]=="DONE"):
                        print data[0:5]
                        fp.close()
                        break
                    elif(data[0:3]=="END"):
                        print data[0:5]
                        break
                    else:
                        print "blok ", len(data), data[0:10]
                        fp.write(data)
            else :
                print "nama tidak ada"
            
        elif(req=='2'):
            nama = raw_input('nama file yang akan dikirim : ')
            sock.send("START {}" . format(nama))
            ukuran = os.stat(nama).st_size
            fp = open(nama,'rb')
            k = fp.read()
            terkirim=0
            for x in k:
                sock.send(x)
                terkirim = terkirim + 1
                print "\r terkirim {} of {} " . format(terkirim,ukuran)
            fp.close()
            sock.send("DONE")
            sock.send("END")
        elif(req=='3'):
            break
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()