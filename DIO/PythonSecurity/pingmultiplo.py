import os, time

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    #print(dump)

    for ip in dump:
        print("Verificando o IP ou Host: " + ip)
        os.system("ping -c 2 {}".format(ip))
        print("-" * 60)
        time.sleep(3)