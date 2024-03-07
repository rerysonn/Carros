class Carros:
    carros = []

    def __init__(self, modelo, pintura):
        self.modelo = modelo.title()
        self.pintura = pintura.title()
        self.disponivel = False

        Carros.carros.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.pintura}"
    
    @classmethod
    def listar_carros(cls):
        print(f"{"Modelo do carro".ljust(20)} | {"Cor do carro".ljust(20)}")
        for carro in cls.carros:
            print(f"{carro.modelo.ljust(20)} | {carro.pintura.ljust(20)}")


carro1 = Carros("palio", "verde")
carro2 = Carros("fusca", "preto")
carro3 = Carros("nivus", "azul")

Carros.listar_carros()
