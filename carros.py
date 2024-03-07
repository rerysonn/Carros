class Carros:
    carros = []

    def __init__(self, modelo, pintura):
        self.modelo = modelo.title()
        self.pintura = pintura.title()
        self._disponivel = False

        Carros.carros.append(self)

    def __str__(self):
        return f"{self.modelo} | {self.pintura}"
    
    @classmethod
    def listar_carros(cls):
        print(f"{"Modelo do carro".ljust(20)} | {"Cor do carro".ljust(20)} | {"Status do carro"}")
        for carro in cls.carros:
            print(f"{carro.modelo.ljust(20)} | {carro.pintura.ljust(20)} | {carro.carro_disponivel}")

    @property
    def carro_disponivel(self):
        return 'Disponivel' if self._disponivel else 'Indisponivel'
    
    def alterar_estado(self):
        self._disponivel = not self._disponivel




