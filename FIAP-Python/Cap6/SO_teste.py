import platform, getpass
from datetime import datetime

print("Nome máquina:..........", platform.node())
print("Arquitetura:...........", platform.architecture())
print("Sistema Operacional:...", platform.system())
print("Versão do SO:..........", platform.release())
print("Processador:...........", platform.processor())
print("Versão do Python:......", platform.python_version())

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)

print(getpass.getuser())
print(getpass.getpass("Digite sua senha: "))