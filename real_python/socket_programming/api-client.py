import socket

HOST = "147.182.246.164"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    f = open("README.md", "rb")
    l = f.read(1024)
    # s.sendall(b"Hello, world")
    while l:
        s.send(l)
        l = f.read(1024)
    data = s.recv(1024)

print(f"Received {data!r}")
