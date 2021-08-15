import getpass

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha: ")
if usuario == "alexgammaro" and senha == "Hello":
    print("Acesso validado, seja bem-vindo!")
else:
    print("Acesso não autorizado!")