#Escreva um programa que pergunte o ano de nascimento de uma pessoa
# e diga se ele é maior de idade

ano = int(input('Digite o ano em que você nasceu:'))
idade = 2023 - ano
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")