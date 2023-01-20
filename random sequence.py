import random
a= str(input('digite o primeiro nome'))
b= str(input('digite o segundo nome'))
c= str(input('digite o terceiro nome'))
d= str(input('digite o nome do quarto aluno'))
e= [a,b,c,d]
f= random.shuffle(e)
print('a sequencia será')
print(e)