'''
1.
import math
import random

num = float(input("Digite um número para calcular a raiz quadrada: "))
print("Raiz quadrada:", math.sqrt(num))
print("Número aleatório entre 1 e 100:", random.randint(1, 100))

import platform
print("Sistema operacional:", platform.system())
print("Versão do sistema:", platform.version())
print("Arquitetura:", platform.architecture())
'''

'''
2.
import platform
print("Sistema operacional:", platform.system())
print("Versão do sistema:", platform.version())
print("Arquitetura:", platform.architecture()
'''

'''
3.
import meu_modulo
numero = int(input("Digite um número para ver o dobro: "))
print("Dobro:", meu_modulo.dobro(numero))
'''

'''
4.
frase = input("Digite uma frase: ")
vogais = "aeiou"
for vogal in vogais:
    print(f"{vogal}: {frase.lower().count(vogal)}")
print("Frase ao contrário:", frase[::-1])
print("Frase com '-' no lugar de espaços:", frase.replace(" ", "-"))
'''

'''
5.
frase = input("Digite uma frase: ")
vogais = "aeiou"
for vogal in vogais:
    print(f"{vogal}: {frase.lower().count(vogal)}")
print("Frase ao contrário:", frase[::-1])
print("Frase com '-' no lugar de espaços:", frase.replace(" ", "-"))
'''

'''
6.
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
'''

'''
7.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)
carro1.exibir_detalhes()
carro2.exibir_detalhes()
'''


'''
8.
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} de {self.autor} com {self.paginas} páginas"

    def __len__(self):
        return self.paginas

livro = Livro("Dom Casmurro", "Machado de Assis", 240)
print(livro)
print("Páginas:", len(livro))
'''



'''
9.
class Animal:
    def fazer_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

c = Cachorro()
g = Gato()
c.fazer_som()
g.fazer_som()
'''

'''
10.
def contar_pares(n):
    for i in range(0, n+1, 2):
        yield i

limite = int(input("Mostrar pares até: "))
for num in contar_pares(limite):
    print(num)
'''

'''
11.
class Contador:
    def __init__(self, max):
        self.max = max
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual <= self.max:
            val = self.atual
            self.atual += 1
            return val
        else:
            raise StopIteration

for num in Contador(5):
    print(num)
'''

'''
12.
def multiplicador(fator):
    def multiplica(numero):
        return numero * fator
    return multiplica

por_dois = multiplicador(2)
print("5 * 2 =", por_dois(5))
'''

'''
13.
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"Total de linhas: {len(linhas)}")
    for linha in linhas:
        print(linha.strip())
'''

'''
14.
import pickle
numeros = [1, 2, 3, 4, 5]
with open("dados.bin", "wb") as f:
    pickle.dump(numeros, f)

with open("dados.bin", "rb") as f:
    dados = pickle.load(f)
    print("Números lidos do binário:", dados)
'''

'''
15.
import os
import time
import datetime
import calendar

print("Diretório atual:", os.getcwd())
print("Data e hora atual:", datetime.datetime.now())
print("Calendário do mês atual:")
print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))
print("Esperando 3 segundos...")
time.sleep(3)
print("Fim da pausa.")
'''
