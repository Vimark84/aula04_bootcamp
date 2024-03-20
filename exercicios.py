#   Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
#   
#   lista_de_numeros = list(range(1 , 11))
#   for numero in lista_de_numeros:
#       print(numero**2)
#   
###############################################################################################################
#   Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
#   
#   lista_linguagens= ["Python", "Java", "C++", "JavaScript"]
#   lista_linguagens.remove("C++")
#   lista_linguagens.append("Ruby")
#   print(lista_linguagens)
#   
################################################################################################################
#   Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
#   
#   from typing import Dict, Any
#   
#   livro_01: Dict[str, Any] = {
#       "titulo": "Harry Potter",
#       "autor": "ze da manga",
#       "ano": 2000
#   }
#   #   lista_de_elementos: list = livro.items()
#   #   for elemento in lista_de_elementos:
#   #       print(elemento)
#   
#   livro_02: Dict[str, Any] = {
#       "titulo": "Harry Potter 2",
#       "autor": "ze da manga",
#       "ano": 2003
#   }
#   
#   lista_de_livros = []
#   
#   lista_de_livros.append(livro_01)
#   lista_de_livros.append(livro_02)
#   
#   # print(lista_de_livros)
#   
#   lista_de_livros_usando_dict:dict = {
#       "livro_01": { "Titulo": "Harry Potter",
#       "Autor": "ze da manga",
#       "Ano": 2000},
#   
#       "livro_02": { "Titulo": "Harry Potter 2",
#       "Autor": "ze da manga",
#       "Ano": 2003}
#   }
#   
#   print(lista_de_livros_usando_dict["livro_01"]["Titulo"])
#   
################################################################################################################
#   Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
#   
#   def contar_caracteres(s):
#       contagem = {}
#       for caractere in s:
#           contagem[caractere] = contagem.get(caractere, 0) + 1
#       return contagem
#   
#   print(contar_caracteres("engenharia de dados"))
#   
################################################################################################################
#   Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
#   calcule o preço total da lista de compras.
#   
#   lista_de_compras =  ["maçã", "banana", "cereja"]
#   precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#   total = sum(precos[item] 
#   for item in lista_de_compras)
#   print(f"Preço total: {total}")
#   
################################################################################################################
# 6. Eliminação de Duplicatas
#   Objetivo: Dada uma lista de emails, remover todos os duplicados.
#   
#   emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#   emails_unicos = list(set(emails))
#   print(emails_unicos)
#   
################################################################################################################
#
# 7. Filtragem de Dados
#    Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
#   
#   idades: int = [15, 18, 12, 33, 5, 44, 8, 99]
#   
#   for i in idades:
#       if i >= 18:
#           print(i)
#   
#   idades = [22, 15, 30, 17, 18]
#   idades_validas = [idade for idade in idades if idade >= 18]
#   
#   print(idades_validas)
#
################################################################################################################
#
# 8. Ordenação Personalizada
#    Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
#   
#   pessoas = [
#       {"nome" : "Angello", "idade" : 35},
#       {"nome" : "Mariana", "idade" : 55},
#       {"nome" : "Gilberto", "idade" : 15}
#   ]
#   #usar o parâmetro key da função sort() para especificar uma função de comparação personalizada
#   pessoas.sort(key=lambda pessoa: pessoa['nome']) 
#   print(pessoas)
#
################################################################################################################
#
# 9. Agregação de Dados
#    Objetivo: Dado um conjunto de números, calcular a média.
#    numeros = [10, 50, 60, 80, 90, 40, 50, 60]
#    media = sum(numeros) / len(numeros)
#    print("A média é:", media)
#    
# OU #
#
#    import statistics
#    numeros = [10, 50, 60, 80, 90, 40, 50, 60]
#    media = statistics.mean(numeros)
#    print("A média é:", media)
#    
################################################################################################################
#
#  10. Divisão de Dados em Grupos
#      Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
#
#   numeros: int = [10, 55, 60, 777, 90, 5, 50, 7]
#   num_pares = []
#   num_impares = []
#   
#   for numero in numeros:
#       if numero % 2 == 0:
#           num_pares.append(numero)   
#       else:
#           num_impares.append(numero)
#   print(num_impares)
#   print(num_pares)
#    
################################################################################################################
#
#  11. Atualização de Dados
#      Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
#   
#   produtos = [
#       {"fruta": "maça" , "preço": 12.30},
#       {"fruta":"banana", "preço": 7.00},
#       {"fruta":"uva", "preço": 10.00},
#       {"fruta":"mamão", "preço": 7.80}
#   ]    
#   #Atualizar preço do produto uva para 12
#   for produto in produtos:
#       if produto["fruta"] == "uva":
#           produto["preço"] = 12.00  # Atualizando a preço
#   print(produtos)        
#    
################################################################################################################
#
#  12. Fusão de Dicionários
#      Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
#  
#   
#   produtos_1 = {"fruta1": "maça", "preço1": 12.30} 
#   produtos_2 = {"fruta2":"pera", "preço2": 8.30}
#   
#   dicionario_de_produtos = {**produtos_1 ,**produtos_2}
#   print(dicionario_de_produtos)
#   
#   
#    
################################################################################################################
# 
#  13. Filtragem de Dados em Dicionário
#      Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
#   estoque_de_produtos = {
#       "televisão": 2,
#       "geladeira": 0,
#       "fogão": 5,
#       "ventilador": 0,
#       "telefone": 1
#   }
#   estoque_positivo = {produto: quantidade for produto, quantidade in estoque_de_produtos.items() if quantidade > 0}
#   print(estoque_positivo)
#   
#   OU DENTRO DE UMA LISTA #
#   estoque_de_produtos = [
#       {"produto": "televisão", "qtde": 2},
#       {"produto": "geladeira", "qtde": 0},
#       {"produto": "fogão", "qtde": 5},
#       {"produto": "ventilador", "qtde": 0},
#       {"produto": "telefone", "qtde": 1}
#   ]
#   
#   for produto in estoque_de_produtos:
#       if produto["qtde"] > 0:
#           print(produto)
#     
################################################################################################################
#
#  14. Extração de Chaves e Valores
#      Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
#  
#   dicionario = {"a":1 , "b":2 , "c":3 , "d":4}
#   chaves = list(dicionario.keys())
#   valores = list(dicionario.values())
#   
#   print("Chaves:", chaves)
#   print("Valores:", valores)
#    
################################################################################################################
#
#  15. Contagem de Frequência de Itens
#      Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
#

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(frequencia)        


#    
################################################################################################################
