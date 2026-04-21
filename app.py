#--------------------------------------------------------------------------------

from modelo.restaurante import Restaurante

#--------------------------------------------------------------------------------


restaurante4 = Restaurante('Alison Burguer', 'hamburgueria','')
restaurante5 = Restaurante('Pizza do Zé', 'pizzaria','')

restaurante_teste = Restaurante('Teste', 'Teste','')
restaurante_teste.receber_avaliacao('Cliente 1', 4)
restaurante_teste.receber_avaliacao('Cliente 2', 5) 

#restaurante4.atualizar_status()
#restaurante5.atualizar_status()





#--------------------------------------------------------------------------------

def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
    
#--------------------------------------------------------------------------------