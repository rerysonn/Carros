from carros import Carros

carro1 = Carros("palio", "verde")
carro1.alterar_estado()
carro2 = Carros("fusca", "preto")
carro3 = Carros("nivus", "azul")
carro3.alterar_estado()

carro1.receber_avaliacao("Mario", 3.5)
carro1.receber_avaliacao("Sergio", 4.8)

carro2.receber_avaliacao("Nicolas", 5)
carro2.receber_avaliacao("Pedro", 4)




def main():
    Carros.listar_carros()

if __name__ == '__main__':
    main()