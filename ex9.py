#Ajuste salarial

#Lendo o salário incial
salarioInicial= float(input('Digite o salário incial: '))

#Calculando aumento
porcentagem= float(salarioInicial*(15/100))
salarioAumentado= float(salarioInicial+porcentagem)

#Printando resultado
print(f'O salário inicial de {salarioInicial:2.f}R$, após aumento de 15% ficou em {salarioAumentado:.2f}R$')