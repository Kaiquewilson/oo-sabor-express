from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida

restaurante1 = Restaurante("Sabor Express", "Comida Rápida", status=True)
bebida1 = Bebida("Refrigerante", 5.00, ' grande')
prato1 = Prato("Hambúrguer", 15.00, 'Hambúrguer')
#restaurante1.adicionar_item_cardapio(bebida1)
restaurante1.adicionar_item_cardapio(prato1)    

def main():
    restaurante1.exibir_cardapio





if __name__ == "__main__":
    main()