'''
1.

alunos = {}

print("=== Cadastro de Alunos ===")

while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ").strip()
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
    print(f"Aluno {nome} cadastrado com nota {nota}.\n")

while True:
    continuar = input("Deseja cadastrar mais um aluno? (s/n): ").strip().lower()
    if continuar == 's':
        nome = input("Digite o nome do aluno: ").strip()
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
        print(f"Aluno {nome} cadastrado com nota {nota}.\n")
    else:
        break

print("\n=== Lista de Alunos Cadastrados ===")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
'''

'''
2.

palavra = input("Digite uma palavra: ").strip()

contagem_caracteres = {}

for letra in palavra:
    if letra in contagem_caracteres:
        contagem_caracteres[letra] += 1
    else:
        contagem_caracteres[letra] = 1

print("\nContagem de caracteres:")
for caractere, quantidade in contagem_caracteres.items():
    print(f"'{caractere}': {quantidade}")
'''

'''
3. 

tradutor = {
    "casa": "house",
    "livro": "book",
    "carro": "car",
    "gato": "cat",
    "cachorro": "dog",
    "escola": "school",
    "amor": "love",
    "comida": "food",
    "água": "water",
    "sol": "sun"
}

palavra_pt = input("Digite uma palavra em português para traduzir: ").strip().lower()

if palavra_pt in tradutor:
    traducao = tradutor[palavra_pt]
    print(f"A tradução de '{palavra_pt}' para o inglês é '{traducao}'.")
else:
    print(f"Tradução para '{palavra_pt}' não encontrada no dicionário.")
'''

'''
4.

frase = input("Digite uma frase: ").strip().lower()

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print("\nContagem de palavras na frase:")
for palavra, quantidade in contagem_palavras.items():
    print(f"'{palavra}': {quantidade}")
'''

'''
5.

catalogo = {
    101: ("Notebook", 3500.00),
    102: ("Smartphone", 2200.00),
    103: ("Fone de Ouvido", 150.00),
    104: ("Monitor", 800.00),
    105: ("Teclado", 120.00)
}

print("=== Catálogo de Produtos ===")
print("Códigos disponíveis:", ', '.join(map(str, catalogo.keys())))

codigo = int(input("\nDigite o código do produto que deseja consultar: "))

if codigo in catalogo:
    nome, preco = catalogo[codigo]
    print(f"\nProduto encontrado:")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco:.2f}")
else:
    print("Código não encontrado no catálogo.")
}
'''
