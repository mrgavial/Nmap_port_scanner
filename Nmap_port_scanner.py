import socket

target = input("Ip address: ")
port_range = input("Port Range to Scan (example. 1-100): ")

start_port, end_port = port_range.split("-")
start_port = int(start_port.strip())
end_port = int(end_port.strip())


for port in range(start_port, end_port+1):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Açık")
    else:
        print(f"Port {port}: Kapalı")
    s.close()
