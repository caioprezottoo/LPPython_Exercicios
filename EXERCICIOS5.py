'''
def calcular_fatorial(numero):

    if numero == 0:
        return 1  
    elif numero < 0:
        return "Fatorial não definido para números negativos"
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero_usuario = int(input("Digite um número inteiro para calcular o fatorial: "))

resultado = calcular_fatorial(numero_usuario)

if isinstance(resultado, int):
  print(f"O fatorial de {numero_usuario} é: {resultado}")
else:
  print(resultado)
'''

'''
def eh_primo(numero):

    if numero <= 1:
        return False 

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False 

    return True 

numero_usuario = int(input("Digite um número inteiro: "))

if eh_primo(numero_usuario):
    print(f"{numero_usuario} é um número primo.")
else:
    print(f"{numero_usuario} não é um número primo.")'
'''

'''
def calcular_media(lista_numeros):

    if not lista_numeros: 
        return 0  

    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

entrada_usuario = input("Digite uma lista de números separados por espaço: ")

lista_usuario = [float(num) for num in entrada_usuario.split()]

media_calculada = calcular_media(lista_usuario)

print(f"A média dos números é: {media_calculada}")'
'''

'''
def contar_vogais(palavra):

    vogais = "aeiouAEIOU" 
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

palavra_usuario = input("Digite uma palavra: ")

numero_vogais = contar_vogais(palavra_usuario)

print(f"A palavra '{palavra_usuario}' tem {numero_vogais} vogais.")'
'''

'''
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print(f"{temperatura_celsius:.2f} graus Celsius equivalem a {temperatura_fahrenheit:.2f} graus Fahrenheit.")'
'''