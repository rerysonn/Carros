class Carros:
    carros = []

    def __init__(self, modelo, pintura):
        self.modelo = modelo
        self.pintura = pintura
        self.disponivel = False

        Carros.carros.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.pintura}"
    
    @classmethod
    def listar_carros(cls):
        for carro in cls.carros:
            print(f"{carro.modelo} | {carro.pintura}")


carro1 = Carros("palio", "verde")
carro2 = Carros("fusca", "preto")
carro3 = Carros("nivus", "azul")

Carros.listar_carros()
