import portscanner as p

targets_ip = input ('[+] Enter Target to Scan: ')
port_num = int(input('[+] Enter the amount of ports you want to scan (500 - first 500 ports): '))
vul_file = input('[+] * Enter path to the file with vulnerable softwares: ')
print ('\n')

target = p.PortScan(targets_ip, port_num)
target.scan()


with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print (f'[!!] VULNERABLE BANNER: {banner} ON PORT: {target.open_ports[count]} ')




