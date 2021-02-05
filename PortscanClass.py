import socket
from IPy import IP

class Portscan():
    def __init__(self, target, portnum):
        self.target = target
        self.portnum = portnum



    def scan(self, ):
        converted_ip = check_ip(target)
        print('\n' + f'[-_0 Scanning Target[{target}]')
        for port in range(1,100):
            scan_port(converted_ip, port)


    def check_ip(self):
        try:
            return IP(ip)
        except ValueError:
            return socket.gethostbyname(ip)


    def scan_port(self):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ipaddr, port))
            try:
                banner = s.recv(9999)
                print(f'[+] port {str(port)} is LIVE :  {str(banner.decode())}')
            except:
                print(f'[+] Port {port} is LIVE')
        except:
            pass


