#Calculando descontos

#Lendo o preço original do produto
<<<<<<< HEAD
precoOriginal= float(input('Qual o preço original do produto?: '))
=======
precoOriginal= float(input('Qual o preço original do produto?: )'))
>>>>>>> 89dbcbe2b68f57a59abc862c9c3448be82274846

#Calculando desconto
porcentagem= float(precoOriginal*(5/100))
desconto= float(precoOriginal-porcentagem)

#Printando resultado
print(f'O produto que custava {precoOriginal}, após desconto de 5%, resultou em {desconto:.2f}R$')