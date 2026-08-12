#Aluguel de carros

#Lendo os dados de calculo para total a pagar
diasAlugado= float(input('Por quantos dias o carro foi alugado?: '))
kmsrodados= float(input('Por quantos quilometros o carro rodou?: '))

#Calculando total a pagar
diasAlugadoMultiplicado= float(diasAlugado*60)
kmsrodadosMultiplicado= float(kmsrodados*0.15)
totalPagar= (diasAlugadoMultiplicado+kmsrodadosMultiplicado)

#Printando resultado
print(f'O total a pagar é de: {totalPagar:.2f}R$')