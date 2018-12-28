#!/usr/bin/python
# coding=utf-8


# Central

print('##########  Calcular os Ângulos.  ###############')
n1 = input('Digite o número de lados existentes em seu poligono: ')
n2 = 360

mult = n2/n1

print('Ângulo Central: {} \n\n\n' .format(mult))

# Interno


print('##########  Ângulo Interno.  ###############')

sub = 180-mult

print('Ângulo Interno: {} ' .format(sub))
