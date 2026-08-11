#Média aritmética

#Lendo os número
numero1= float(input('Digite um número: '))
numero2= float(input('Digite outro número: '))
numero3= float(input('Digite outro número: '))

#Variaveis para os cálculos
media= float(0)

#Cáculos
media= float((numero1 + numero2 + numero3) // 3)

#Printando o resultado
print(f'A média aritimética entre {numero1} + {numero2} + {numero3} resulta em {media:.2f}')