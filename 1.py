#Faça um programa que leia 2 notas de um aluno, calcule a média
# e imprima aprovado ou reprovado(para ser aprovado a média deve ser no mínimo 6

n1= float(input('Digite a primeira nota:'))
n2= float(input('Digite a segunda nota:'))
m= (n1 + n2)/2

if m <=6 :
    print('Aluno(a) reprovado(a)')
else:
    print('Aluno(a) aprovado(a)')
