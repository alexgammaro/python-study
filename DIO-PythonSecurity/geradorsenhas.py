import random, string

tamanho = int(input("Digite um número para o tamanho da sua senha: "))
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;:/?"
rnd = random.SystemRandom()
print("".join(rnd.choice(chars) for i in range (tamanho)))