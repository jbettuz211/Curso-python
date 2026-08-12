#Calculando descontos

#Lendo o preço original do produto
precoOriginal= float(input('Qual o preço original do produto?: )'))

#Calculando desconto
desconto= float(precoOriginal-(5/100))

#Printando resultado
print(f'O produto que custava {precoOriginal}, após desconto de 5%, resultou em {desconto:.2f}R$')