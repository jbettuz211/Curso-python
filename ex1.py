#Dissecando uma variavel

#Criando a variavel
var= ('Digite algo: ')

#Lendo a variavel
var= input('Digite algo: ')

#Dissecando a variavel
print(f'O tipo da variavel é: {type(var)}')
print(f'Ela é composta só de letras maiusculas?: {var.isupper()}')
print(f'Ela tem a primeira letra de cada palavra em maiusculo?: {var.istitle()}')
print(f'Ela só tem letras?: {var.isalpha()}')
print(f'Ela só tem números e/ou letras?: {var.isalnum()}')
print(f'Ela esta na tabela ASSCI?: {var.isascii()}')
print(f'Ela é um número inteiro?: {var.isdecimal()}')
print(f'Ela é um número sem caractereses especiais?: {var.isdigit()}')
print(f'Nesta variavel só tem numéros?: {var.isnumeric()}')
print(f'Ela pode ser uma variavel?: {var.isidentifier()}')
print(f'Só tem letras minusculas nela?: {var.islower()}')