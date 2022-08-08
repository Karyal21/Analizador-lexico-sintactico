import ply.lex as lex
import re
import codecs
import os
import sys
reservadas= {
    'IMPORT':'IMPORT',
    'DEF':'DEF',
    'CLASS':'CLASS',
    'IF':'IF',
    'ELSE':'ELSE',
    'FOR':'FOR',
    'IN':'IN',
    'RANGE':'RANGE',
    'SELF':'SELF',
    'WHILE':'WHILE',
    'TRY':'TRY',
    'EXCEPT':'EXCEPT',
    'RETURN':'RETURN',
    'BREAK':'BREAK',
    'NEXT':'NEXT',
    'INPUT':'INPUT',
    'PRINT':'PRINT',
    'INT':'INT',
    'FLOAT':'FLOAT',
    'BOOLEAN':'BOOLEAN',
    'STR':'STR',
    'POW':'POW',
    'MATHSQRT':'MATHSQRT',
    'AND':'AND',
    'OR':'OR',
    'NOT':'NOT'

}
tokens=[
    'ID',
    'NUMERO',
    'SUMA',
    'ASIGNACION',
    'RESTA',
    'DIVISION',
    'MULTIPLICACION',
    'IGUAL',
    'DIFERENTE',
    'MAYORQUE',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'PUNTO',
    'COMA',
    'ESPACIO',
    'DOSPUNTOS',
    'PUNTOCOMA',
    'COMILLASIMPLE',
    'COMILLADOBLE',
    'PARENTESIS_A',
    'PARENTESIS_C',
    'LLAVE_C',
    'LLAVE_A',
    'CORCHETE_A',
    'CORCHETE_C',
    'MASMAS',
    'MENOSMENOS',
]+list(reservadas.values())
#tokens=tokens+list(reservadas.values())
#print(tokens[:])
t_ignore='\t'
#OPERADOR MATEMATICOS
t_SUMA=r'\+'
t_ASIGNACION=r'\='
t_RESTA=r'\-'
t_DIVISION=r'/'
t_MULTIPLICACION=r'\*'

#OPERADORES RACIONALES
t_IGUAL=r'=='
t_DIFERENTE=r'!='
t_MAYORQUE=r'>'
t_MENORQUE=r'<'
t_MAYORIGUAL=r'>='
t_MENORIGUAL=r'<='

#VARIABLES
#t_IDENTIFICADOR
t_PUNTO=r'\.'
t_COMA=r'\,'
t_DOSPUNTOS=r'\:'
t_PUNTOCOMA=r'\;'
t_COMILLASIMPLE=r'\''
t_COMILLADOBLE=r'"'
t_PARENTESIS_A=r'\('
t_PARENTESIS_C=r'\)'
t_LLAVE_A=r'\{'
t_LLAVE_C=r'\}'
t_CORCHETE_A=r'\['
t_CORCHETE_C=r'\]'
#OPERADORES DE DECREMENTOYINCREMENTO
t_MASMAS=r'\+\+'
t_MENOSMENOS=r'\-\-'

def t_ESPACIO(t):
    r'\s+'
    pass

def t_ID(t):
 r'[a-zA-Z][a-zA-Z0-9]*'
 if t.value.upper() in reservadas:
  t.value=t.value.upper()
  t.type=t.value
 return t

def t_SALTOLINEA(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
 r'\#.*'
 pass

def t_NUMERO(t):
 r'\d+'
 t.value=int(t.value)
 return t

def t_error(t):               
 #print("caracter ilegal str(t.value[0]))
 t.lexer.skip(1)
 return "Caracter ilegal"




# def buscarFicheros(directorio):
# 	ficheros = []
# 	numArchivo = ''
# 	respuesta = False
# 	cont = 1

# 	for base, dirs, files in os.walk(directorio):
# 		ficheros.append(files)

# 	for file in files:
# 		print str(cont)+". "+file
# 		cont = cont+1

# 	while respuesta == False:
# 		numArchivo = raw_input('\nNumero del test: ')
# 		for file in files:
# 			if file == files[int(numArchivo)-1]:
# 				respuesta = True
# 				break

# 	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

# 	return files[int(numArchivo)-1]

# directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 1/test/'
# archivo = buscarFicheros(directorio)
# test = directorio+archivo
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

#analizador.input(cadena)

# while True:
# 	tok = analizador.token()
# 	if not tok : break
# 	print tok


