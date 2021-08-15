from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print("Piloto: {} Km: {}".format(piloto, trajeto))

t_carro1 = Thread(target=carro, args=[1, "Luke"])
t_carro2 = Thread(target=carro, args=[1.5, "Tuca"])
t_carro1.start()
t_carro2.start()

# def carro1(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print("Carro 1", trajeto)
#         trajeto+=velocidade
#
# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print("Carro 2", trajeto)
#         trajeto+=velocidade
#
# carro1(10)
# carro2(20)