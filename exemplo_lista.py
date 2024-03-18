#   produto: str = "sapato"
#   produto_2: str = "camiseta"
#   produto_3: str = "videa game"
#   
#   produtos: list = []
#   
#   produtos.append(produto)
#   produtos.append(produto_2)
#   produtos.append(produto_3)
#   # produtos.pop() # remove o ultimo da lista
#   # produtos.remove(produto_2) # remove o produto setado entre parenteses
#   
#   print(produtos)
 
import json

lista: list = ["sapato", 39 , 10.38 , True]

produto_01: dict = {
    "nome": "sapato",
    "quantidade": 39,
    "preço": 10.38,
    "disponibilidade": True 
}

produto_02: dict = {
    "nome": "televisão",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}     

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

#fazendo a coversão para JSON (não esquecer de realizar o import da função>: import json )
carrinho_json = json.dumps(carrinho)
print(carrinho_json)