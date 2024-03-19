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
#   total = sum(precos[item] for item in lista_de_compras)
#   print(f"Preço total: {total}")
