import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class NewsParser():
    address = ''
    def __init__(self):
            NewsParser .__init__(self)

    def work_thread(connection,addr):
     while(1):
        str = connection.recv(1024).decode('utf8')
        if (str[0:4] != "exit"):
            str = str[::-1]
            connection.send(str.encode('utf8'))
        else:
            break
     connection.close()

def main():
    HOST = '127.0.0.1'
    PORT = 3333
    s.bind((HOST, PORT))
    s.listen(5)
    while (1):
        connection, addr = s.accept()
        print('Connecting', addr)
        np=NewsParser()
        thread=threading.Thread(target=np.work_thread,args=(connection,addr))
        thread.start()

if __name__=='__main__':
    main()
