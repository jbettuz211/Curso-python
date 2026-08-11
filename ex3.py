#Conversor de medidas

#Lendo a medida em metros
metros= float(input('Digite a medida em metros: '))

#Criando variaves para os cálculos
km= float(0)
hm= float(0)
dam= float(0)
dm= float(0)
cm= float(0)
mm= float(0)

#Fazendo os cálculos
km= (metros/1000)
hm= (metros/100)
dam= (metros/10)
dm= (metros*10)
cm= (metros*100)
mm= (metros*1000)

#Printando os resultados
print(f'O valor de {metros} metro(s) em outras unidades de medida são: {km}km(s), {hm}hm(s), {dam}dam(s, {dm}dm(s), {cm}cm(s), {mm}mm(s)')