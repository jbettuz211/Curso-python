#Cateto e hipotenusa

#Importando a biblioteca
from math import hypot

#Lendo os dados do triangulo para calcular hipotenusa
catetoOposto= float(input('Qual a medida do cateto oposto em metros?: '))
catetoAdjacente= float(input('Qual a medida do cateto adjacente em metros?: '))

#Calculando a hipotenusa
hipotenusa= hypot(catetoOposto, catetoAdjacente)

#Printando o resultado
print(f'O resultado da hipotenusa dos catetos {catetoOposto}m e {catetoAdjacente}m é: {hipotenusa:.2f}m')
