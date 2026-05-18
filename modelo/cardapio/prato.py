from cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def  __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return f"Prato: {self._nome}, Preço: R${self._preco:.2f}, Descrição: {self._descricao}"