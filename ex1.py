#Dissecando uma variavel

#Variavel principal
var= ('Digite algo: ')

#Lendo a variavel
var= input('Digite algo: ')

#Tipo da variavel
print(f'O tipo da variavel é: {type(var)}')

#Variavel auxiliar
resultado= bool()

#Printando resultados
resultado= var.isupper()
print(f"Ela é composta só de letras maiusculas?: {'Sim' if resultado== True else 'Não'}")

resultado= var.istitle()
print(f"Ela tem a primeira letra de cada palavra em maiusculo?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isalpha()
print(f"Ela só tem letras?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isascii()
print(f"Ela só tem números e/ou letras?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isdecimal()
print(f"Ela esta na tabela ASSCI?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isdigit()
print(f"Ela é um número sem caractereses especiais?: {'Sim' if resultado== True else 'Não'}")


resultado= var.isnumeric()
print(f"Nesta variavel só tem numéros?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isidentifier()
print(f"Ela pode ser uma variavel?: {'Sim' if resultado== True else 'Não'}")

resultado= var.islower()
print(f"Só tem letras minusculas nela?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isprintable()
print(f"Ela é printavel em python?: {'Sim' if resultado== True else 'Não'}")

resultado= var.isspace()
print(f"Só ha espaços na variavel?: {'Sim' if resultado== True else 'Não'}")
