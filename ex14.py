#Sorteando um aluno da lista

#Importando bilbioteca
from random import randint

#Lendo os nomes dos alunos
aluno1= input('Qual o nome do primeiro aluno?: ')
aluno2= input('Qual o nome do segundo aluno?: ')
aluno3= input('Qual o nome do terceiro aluno?: ')
aluno4= input('Qual o nome do quarto aluno?: ')

#Sorteando 1 aluno
sorteado= ''
sorteio= int(randint(1,4))


if sorteio== 1:
    sorteado= aluno1
elif sorteio== 2:
    sorteado= aluno2
elif sorteio== 3:
    sorteado= aluno3
else:
    sorteado= aluno4

#Printando resultado
#print(sorteio) -- DEBUG
print(f'O aluno escolhido foi: {sorteado}')
