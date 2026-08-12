#Conversor de moedas

#Lendo o dinheiro da carteira em R$
dinheiroCarteira= float(input('Quanto dinheiro ha em sua carteira em R$?: '))

#Criando as variveis das moedas estrangeiras
dolar= float(5.15)
euro= float(5.95)
libra= float(6.97)

#Pritando resultados
print(f'Com {dinheiroCarteira}R$, você pode comprar em 12 de agosto de 2026 {dinheiroCarteira/dolar:.2f} dolares')
print(f'Com {dinheiroCarteira}R$, você pode comprar em 12 de agosto de 2026 {dinheiroCarteira/euro:.2f} euros')
print(f'Com {dinheiroCarteira}R$, você pode comprar em 12 de agosto de 2026 {dinheiroCarteira/libra:.2f} libras')