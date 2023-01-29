import socket

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f'Port {port} is open')
            open_ports.append(port)
        sock.close()
    return open_ports

host = input("Enter the host to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

scan_ports(host, start_port, end_port)
