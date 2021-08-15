import ipaddress

ip = "192.168.0.1"
endereco = ipaddress.ip_address(ip)
print(endereco)
print(endereco + 100)
print(endereco + 257)
print(endereco + 256)
print(endereco + 2000)

ip_rede = "192.168.0.0/30"
rede = ipaddress.ip_network(ip_rede, strict=False)
print(rede)

for ip in rede:
    print(ip)