#entrada de los metros del lugar que establece el usuario
largo=float(input('Ingrese en metros el largo del ambiente: '))
ancho=float(input('Ingrese en metros el ancho del ambiente: '))
#calculo metros cuadrados
m2=largo*ancho
#calculo de frigorias que son las adecuadas
frigorias=m2*100

print(f'Para un ambiente de {m2} metros cuadrados se necesita un aire acondicionado de {frigorias} aproximadamente')
