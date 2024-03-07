from carros import Carros

carro1 = Carros("palio", "verde")
carro1.alterar_estado()
carro2 = Carros("fusca", "preto")
carro3 = Carros("nivus", "azul")
carro3.alterar_estado()


def main():
    Carros.listar_carros()

if __name__ == '__main__':
    main()