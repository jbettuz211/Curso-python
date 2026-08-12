#Pintando parede

#Lendo medidas da parede
largura= float(input('Qual a largura da parede em metros?: '))
altura= float(input('Qual a altura da parede em metros?: '))

#area da parede
area= float(largura*altura)
print(f'A parede tem dimensão de {altura:.2f} X {largura:.2f} e área de {area:.2f}m²')

#Quantidade de tinta necessária
tintaPorMetroQuadrado= float(area*0.3)
print(f'Para pintar {area:.2f}m² demandara {tintaPorMetroQuadrado:.2f} litros de tinta no total')