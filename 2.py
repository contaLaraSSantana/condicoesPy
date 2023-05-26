#Faça um programa que peça dois números ao usuário e mostre
#qual o maior e qual o menor

n1= int(input('Digite o primeiro numero:'))
n2= int(input('Digite o segundo numero:'))

if n1 < n2:
    print('O número',n1, "é menor que o", n2)
elif n1 == n2:
    print("Os numeros são iguais")
else:
    print('O número', n2, "é menor que o", n1)

