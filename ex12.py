#Quebrando um número

#Importando biblioteca
from math import trunc

#Lendo o número
numero= float(input('Digite qualquer número: '))

#Truncando o número
numerotruncado= int(trunc(numero))

#Printando o resultado
print(f'{numero} em sua forma truncada é: {numerotruncado}')

