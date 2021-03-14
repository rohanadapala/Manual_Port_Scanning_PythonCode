import socket
N=(input("Enter the IP Address:"))
p1=int(input("Enter a staring Port No:"))
p2=int(input("Enter ending port No:"))

for i in range (p1,p2+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((N,i))==0:
        print("port %i"%i,"---->open"," Type : ",socket.getservbyport(i) )

    else:
        print("port %i" % i, "---->closed")
    sock.close()








