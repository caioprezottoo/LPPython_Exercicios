'''
1.
def divisao_segura():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

divisao_segura()
'''

'''
2.
def abertura_segura_de_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

abertura_segura_de_arquivo()
'''

'''
3.
def conversao_entrada():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"O dobro do número é: {numero * 2}")
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

conversao_entrada()
'''

'''
4.
def acesso_lista():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite o índice (0 a 4) para acessar o valor da lista: "))
        print(f"Valor no índice {indice}: {lista[indice]}")
    except IndexError:
        print("Erro: Índice inválido. A lista possui índices de 0 a 4.")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

acesso_lista()
'''

'''
5.
class SaldoInsuficienteError(Exception):
    pass

def operacoes_bancarias():
    saldo = 1000.00
    try:
        saque = float(input(f"Saldo disponível: R$ {saldo}. Quanto deseja sacar? R$ "))
        if saque > saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para o saque.")
        saldo -= saque
        print(f"Saque realizado com sucesso. Saldo restante: R$ {saldo}")
    except SaldoInsuficienteError as e:
        print(e)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um valor numérico.")

operacoes_bancarias()
'''
