#Antecessor e Sucessor

#Lendo e conferindo o número
testador= bool('')
while testador is not True:
    numero= input('Digite um número inteiro: ')
    testador= numero.isdigit()
        
#Convertendo string em inteiro
numero= int(numero)

#Fazendo antecessor e sucessor
print(f'O antecessor de {numero} é {numero-1} e o sucessor é {numero+1}')
