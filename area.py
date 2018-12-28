#!/usr/bin/python
# coding=utf-8


nome = raw_input('Digite seu nome: ')

print('Olá {}, essa é uma ferramenta feita por Everton com intuito de calcular áreas de polígonos!  \n\n'.format(nome))

print('############## Calcular áreas  #######################\n')
print('                  Figuras: \n\n\n')
print('Quadrado: 1, Círculo: 2, Retângulo: 3, Trapézio: 4\n')



perg = input('Qual figura deseja calcular a área: ')

if perg == 1:
	lado = input('Qual o valor do lado: ')
	quad = lado**2
	print ("Área do Quadrado: {} ".format(quad))
	
elif perg == 2:
	raio = input('Qual o valor do raio: ')
	cir = 3 * raio*raio
	print('Área do Círculo: {} '.format(cir))
	
elif perg == 3:
	base = input('Qual o valor da base: ')
	altura = input('Qual o valor da altura: ')
	multi = base * altura
	print('Área do Retângulo: {} '.format(multi))
	
elif perg == 4:
	b = input('Qual o valor da base: ')
	a = input('Qual o valor da altura: ')
	multi = b * a
	print('Área do Trapézio: {} '.format(multi))
	
	
