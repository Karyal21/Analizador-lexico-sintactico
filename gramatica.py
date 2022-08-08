from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import filedialog
import tkinter
from turtle import bgcolor
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import scrolledtext
from tokenize import String
import ply.yacc as yacc
from analizadorLexicop import tokens,reservadas
from sys import stdin

root=Tk()
gtex=StringVar()
result=StringVar()
lines=String
arreglo=[]
precedence = (
	('right','WHILE','ID','IF'),
	('right','DEF'),
	('right','ASIGNACION'),
	('left','DIFERENTE'),
	('left','MAYORQUE','MAYORIGUAL','MENORQUE','MENORIGUAL'),
	('left','SUMA','RESTA'),
	('left','PARENTESIS_A','PARENTESIS_C')
	)

def p_asignar(p):
    '''ASIGNAR : ID ASIGNACION NUMERO
               | ID ASIGNACION NUMERO ASIGNAR 
               | ID ASIGNACION NUMERO DEFINIR'''
    arreglo.append("Regla -> Asignar un valor a una variable")

def p_def(p):
    '''DEFINIR : DEF ID PARENTESIS_A PARENTESIS_C DOSPUNTOS WHILES'''
    arreglo.append("Regla -> Definir un metodo")
def p_while(p):
    '''WHILES : WHILE ID DOSPUNTOS ASIGNARVV'''
    arreglo.append("Regla -> Definir un ciclo While")

def p_asignarV(p):
    '''ASIGNARVV : ID ASIGNACION INPUT PARENTESIS_A COMILLADOBLE ID ID ID ID ID DOSPUNTOS COMILLADOBLE PARENTESIS_C CASTEOINT'''
    print("Regla -> Ingresar valor en una variable")
    arreglo.append("Regla -> Ingresar valor en una variable")

def p_casteoInt(p):
    '''CASTEOINT : ID ASIGNACION INT PARENTESIS_A ID PARENTESIS_C RETORNAR'''
    arreglo.append("Regla -> Convertir valor a entero")

def p_retorno(p):
    '''RETORNAR : RETURN ID INVOCAR'''
    arreglo.append("Regla -> Retornar valor")

def p_llamaF(p):
    '''INVOCAR : ID ASIGNACION ID PARENTESIS_A PARENTESIS_C CONDICIONAL'''
    arreglo.append("Regla -> Invoca una funcion y la guarda en una variable")

def p_condicionF(p):
    '''CONDICIONAL : IF ID MAYORQUE NUMERO DOSPUNTOS IMPRIMIR'''
    arreglo.append("Regla -> Condicion para saber si un numero es mayor")

def p_imprimir(p):
    '''IMPRIMIR : PRINT PARENTESIS_A COMILLADOBLE NUMERO COMILLADOBLE PARENTESIS_C COMPROBAR
                | PRINT PARENTESIS_A COMILLADOBLE NUMERO COMILLADOBLE PARENTESIS_C ASIGNAR2'''
    arreglo.append("Regla -> Imprimir un caracter en especifico")
def p_ifasignar(p):
    '''COMPROBAR : IF ID ASIGNACION ASIGNACION NUMERO DOSPUNTOS IMPRIMIR'''
    arreglo.append("Regla -> Comprobar la asignacion de una variable")
def p_asignar2(p):
    '''ASIGNAR2 : ID ASIGNACION ID RESTA NUMERO CICLO1'''
    arreglo.append("Regla -> Asignar un valor a una variable y restarla")
    
def p_ciclofor(p):
    '''CICLO1 : FOR ID IN RANGE PARENTESIS_A ID PARENTESIS_C DOSPUNTOS SUMAVAR'''
    arreglo.append("Regla -> Asignar un valor a una variable y restarla")

def p_sumavar(p):
    '''SUMAVAR : ID ASIGNACION ID SUMA ID IMPRIMIRVAR'''
    arreglo.append("Regla -> Asignar un valor de la suma de variables")
def p_imprimirvar(p):
    '''IMPRIMIRVAR : PRINT PARENTESIS_A ID PARENTESIS_C
                   | PRINT PARENTESIS_A ID PARENTESIS_C ASIGNAR'''
    arreglo.append("Regla -> Imprimir el valor de una variable")

def p_asiganrentrevariables(p):
    '''ASIGNAR : ID ASIGNACION ID
               | ID ASIGNACION ID ASIGNAR'''
    arreglo.append("Regla -> Asignar el valor de una variable a otra variable")

def p_error(p):
    arreglo.append("Error de sintaxis ", p)

#---------------------------Funciones--------------------------------
def borrar():
    texto.delete(1.0,tk.END)
    texto1.delete(1.0,tk.END)
def gramatica():
    texto1.delete("1.0", tkinter.END)
    gtex=texto.get("1.0",tk.END)
    parser = yacc.yacc()
    result = parser.parse(gtex)
    aux=String
    s=0
    arreglo2=[]
    for cont in arreglo:
        arreglo2=arreglo[s]
        aux="".join(arreglo2)
        aux=aux+"\n"
        s=s+1
        texto1.insert(1.0, aux)
    while len(arreglo):
        arreglo.pop()  

def abrirtext():
    nombrearch=filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    cadena=nombrearch
    print(cadena)
    direc.config(text=cadena)
    if nombrearch!='':
        archi1=open(nombrearch, "r", encoding="utf-8")
        contenido=archi1.read()
        archi1.close()
        texto.delete("1.0", tkinter.END) 
        texto.insert("1.0", contenido)
#------------------------------Frame de la interfaz---------------------------------------
miFrame=Frame(root, width=600, height=800)
miFrame1=Frame(miFrame,width=600,height=150)
root.title("Analizador sintactico")
root.config(bg="Grey")
root.config(bd=10)
root.config(relief="groove")
miFrame.pack(fill="y", expand=True)
miFrame.config(bg="lavender")
#miFrame.config(width=650, height=350)
miFrame.config(bd=10)
miFrame.config(relief="sunken")
miFrame.config(cursor="arrow")
#Abrir imagen
miImagen=Image.open("ic.png")
#Resize imagen
resized=miImagen.resize((150, 150), Image.ANTIALIAS)
#miImagen=PhotoImage(file="img.png")
new_pic=ImageTk.PhotoImage(resized)
#---------------------------Label--------------------------------
milabel_imag=Label(miFrame, image=new_pic, bg="lavender").place(x=10,y=0)
miLabel= Label(miFrame, text="Analizador Sintáctico", bg="lavender", font=("Franklin Gothic Medium", 18, "italic"))
miLabel.place(x=190, y=40)
miLabel2= Label(miFrame, text="Escriba el codigo a analizar:", bg="lavender", font=("Arial", 14, "italic"))
miLabel2.place(x=10, y=130)
miLabel3= Label(miFrame, text="Resultado obtenido:", bg="lavender", font=("Arial", 14, "italic"))
miLabel3.place(x=10, y=420)
direc=Label(miFrame, bg="lavender", fg="lavender", font=("Arial", 8, "italic"), justify=LEFT)#label para imprimir la cadena
direc.place(x=50, y=650,  width=320,height=25)
#---------------------------ScrollText--------------------------------
texto=scrolledtext.ScrolledText(miFrame,font=("Arial", 10, "italic"))
texto.place(x=50, y=170,width=450,height=180)
texto1=scrolledtext.ScrolledText(miFrame,font=("Arial", 10, "italic"))
texto1.place(x=50, y=470,width=450,height=180)
#---------------------------Button--------------------------------
boton=Button(miFrame,text="Abrir archivo",font=("Arial", 13, "italic"),bg="Grey",command=abrirtext)
boton.place(x=120, y=370,height=35)
boton1=Button(miFrame,text="Verificar",font=("Arial", 13, "italic"),bg="Grey",command=gramatica)
boton1.place(x=250, y=370,height=35)
boton2=Button(miFrame,text="Borrar",font=("Arial", 13, "italic",),bg="Grey",command=borrar)
boton2.place(x=350, y=370,height=35)
root.mainloop()