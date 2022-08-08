import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexicop import tokens
from sys import stdin

precedence = (
	('right','ID','if','while'),
	('right','def'),
	('right','ASIGNACION'),
	('left','DIFERENTE'),
	('left','MAYORQUE','MAYORIGUAL','MENORQUE','MENORIGUAL'),
	('left','SUMA','RESTA'),
	('left','PARENTESIS_A','PARENTESIS_C')
	)
	

def p_asignar(p):
	'''ASIGNAR : ID ASIGNACION NUMERO'''
	print ("Asignar un valor a una variable")

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" % files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

#directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 2/test/'
directorio = 'C:/Users/Gio/Desktop/Lenguajes Automatas/Analizador Sintactico/pruebas/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
print("A: "+test)
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)





