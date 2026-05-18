from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida

restaurante1 = Restaurante("Sabor Express", "Comida Rápida", status=True)
bebida1 = Bebida("Refrigerante", 5.00, "500ml")
prato1 = Prato("Hambúrguer", 15.00, "Hambúrguer com queijo, alface e tomate")

def main():
    print(restaurante1)
    print(bebida1)
    print(prato1)





if __name__ == "__main__":
    main()