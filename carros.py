from avaliacao import Avaliacao

class Carros:
    carros = []

    def __init__(self, modelo, pintura):
        self._modelo = modelo.title()
        self._pintura = pintura.title()
        self._avaliacao = []
        self._disponivel = False

        Carros.carros.append(self)

    def __str__(self):
        return f"{self._modelo} | {self._pintura}"
    
    @classmethod
    def listar_carros(cls):
        print(f"{"Modelo do carro".ljust(20)} | {"Cor do carro".ljust(20)} | {"Avaliação".ljust(20)} | {"Status do carro"}")
        for carro in cls.carros:
            print(f"{carro._modelo.ljust(20)} | {carro._pintura.ljust(20)} | {str(carro.media_avaliacao).ljust(20)} |{carro.carro_disponivel}")

    @property
    def carro_disponivel(self):
        return 'Disponivel' if self._disponivel else 'Indisponivel'
    
    def alterar_estado(self):
        self._disponivel = not self._disponivel

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Sem Avaliação'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media




