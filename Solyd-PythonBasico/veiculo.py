class Veiculo:

    def __init__(self, cor, qtd_rodas, marca, tanque):
        self.cor = cor
        self.qtd_rodas = qtd_rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros