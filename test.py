from main import filto_livros

filto_livros_1 = {"autor": "J.K. Rowling"}
filto_livros_2 = {"ano": 1960}
filto_livros_3 = {"titulo": "Memórias Póstumas de Brás Cubas"}
filto_livros_4 = {"autor": "Franz Kafka"}

Lista_Livros_1 = filto_livros(filto_livros_1)
if Lista_Livros_1: print("Sucesso!! Livros filtrados e encontrados.")
print("Resultado Filtro 1:", Lista_Livros_1, "\n")

Lista_Livros_2 = filto_livros(filto_livros_2)
if Lista_Livros_2: print("Sucesso!! Livros filtrados e encontrados.")
print("Resultado Filtro 2:", Lista_Livros_2, "\n")

Lista_Livros_3 = filto_livros(filto_livros_3)
if Lista_Livros_3: print("Sucesso!! Livros filtrados e encontrados.")
print("Resultado Filtro 3:", Lista_Livros_3, "\n")

Lista_Livros_4 = filto_livros(filto_livros_4)
if Lista_Livros_4: print("Sucesso!! Livros filtrados e encontrados.")
print("Resultado Filtro 4:", Lista_Livros_4)