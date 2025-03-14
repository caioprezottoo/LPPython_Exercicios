'''
def soma_lista():
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")
    numeros = [int(num) for num in entrada.split()]
    soma = sum(numeros)

    print("A soma dos elementos da lista é:", soma)

soma_lista()
'''

'''
def encontrar_maior_menor():
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")
    numeros = [int(num) for num in entrada.split()]

    maior = max(numeros)
    menor = min(numeros)

    print("O maior número é:", maior)
    print("O menor número é:", menor)
    
encontrar_maior_menor()
'''

'''
def remover_duplicatas():
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")

    numeros = [int(num) for num in entrada.split()]

    lista_sem_duplicatas = []
    for num in numeros:
        if num not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(num)

    print("Lista sem duplicatas:", lista_sem_duplicatas)
remover_duplicatas()
'''

'''
def inverter_lista_palavras():
    entrada = input("Digite uma lista de palavras separadas por espaço: ")

    palavras = entrada.split()
    palavras_invertidas = palavras[::-1]
    print("Lista invertida:", palavras_invertidas)

inverter_lista_palavras()
'''

'''
def contar_ocorrencias():
    entrada_lista = input("Digite uma lista de números inteiros separados por espaço: ")

    lista_numeros = [int(num) for num in entrada_lista.split()]

    numero_especifico = int(input("Digite o número específico: "))

    ocorrencias = lista_numeros.count(numero_especifico)

    print(f"O número {numero_especifico} aparece {ocorrencias} vezes na lista.")

contar_ocorrencias()
'''