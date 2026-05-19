#------------------------------------------------------
# Aqui será onde vou amarzenar as minhas classes 
#------------------------------------------------------


from avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio

class Restaurante :
    restaurantes =[]

    def __init__(self, nome, categoria, status) : #__init__ é um inicializador de classe
        self._nome = nome.title()                 # ._ indica que a variável é privada, ou seja, não pode ser acessada fora da classe
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):                            #__str__ é um método mágico que é chamado quando se tenta imprimir um objeto da classe
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    

    #------------------------------------------------------
    # Agora eu vou criar meu própio método para atualizar o status do restaurante

    # Lembrando que ele estará dentro da "class restaurante"
    #------------------------------------------------------
    
    
    
    # |
    # |     "Porque" usar classmethods?
    # |     - Porque ele é um método que pertence a classe e não a instância
    # |     - Vale lembrar que esaa é uma forma de manter boas práticas de programação.
    #\ /

    @classmethod
    def listar_restaurantes(cls):       #"cls" é uma convenção para se referir a classe, ou seja, ele é um parâmetro que representa a classe, e é usado para acessar os atributos e métodos da classe.

        print(f'{"Nome:".ljust(20)} | {"Categoria:".ljust(20)} | {"Status:".ljust(20)} | {"Avaliações:".ljust(20)}') 
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo.ljust(20)} | {str(restaurante.media_das_avaliacoes)}')


    @property                           # @property é um decorador que transforma um método em um atributo, ou seja, ele pode ser acessado como se fosse um atributo, mas na verdade é um método.
    def ativo(self):
        return '☑ Ativo' if self._status else '☐ Inativo'
    
    

    #---------------------------------------ATIVO / INATIVO-----------------------------------------------
    # Agora eu vou criar uma função referente ao objeto e não a classe. 

    def atualizar_status(self):
        self._status = not self._status         # Esse é um recurso do python que inverte o valor. Famoso efeito booleano.

     #--------------------------------------------------------------------------------------






    #--------------------------------------AVALIAÇÃO------------------------------------------------
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)


    #--------------------------------------------------------------------------------------

    @property
    def media_das_avaliacoes(self):
        if not self._avaliacao:
            return "Sem avaliações"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = soma_das_notas / len(self._avaliacao)
        if media >= 5:
            return 5
        else:
            return media


 #--------------------------------------------------------------------------------------





  #---------------------------------------CARDÁPIO-----------------------------------------------
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start = 1):
            
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. nome: {item._nome} | preço: R${item._preco:.2f} | descrição: {item.descricao}'
                print(mensagem_prato) 
            else:
                mensagem_bebida = f'{i}. nome: {item._nome} | preço: R${item._preco:.2f} | tamanho: {item.tamanho}'
                print(mensagem_bebida)
    





#--------------------------------------------------------------------------------------
                                #Dados teste

#restaurante1 = Restaurante("Restaurante da Dedé", "Comida Caseira", "Aberto")
#restaurante1.atualizar_status()

#restaurante2 = Restaurante ("Resort food truck", "Comida rápida", "Aberto")

#--------------------------------------------------------------------------------------

