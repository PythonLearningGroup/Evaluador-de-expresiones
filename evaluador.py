# -*- coding: utf-8 -*-
"""
Creado 10 de Diciembre del 2017
@author: Domingo
"""

from tkinter import*

#configuracion ventana principal
ventana = Tk()
ventana.geometry("300x240")
ventana.title("evaluador")
ventana.configure(bg="orange")

#widget de entrada de datos y salida
numero_a = StringVar()
numero_1 = Entry(ventana, textvariable = numero_a,width=22)
numero_1.focus_set()

resultado = StringVar()

# definicion funciones botones

def evaluar():
	x=(numero_a.get())
	n = -1 # seteo inicial de un contador
	numeros =[]
	simbolos = []
	ubicacion_numeros = []
	ubicacion_simbolos = []
	error = []
	for z in x:
		if z in ["1","2","3","4","5","6","7","8","9","0"]: # evaluo si z es un numero
			n = n + 1
			numeros.append(int(z))# si es valido lo agrego a la lista numeros
			ubicacion_numeros.append(n)
		elif z in ["+","-","/","*","(",")"]:# evaluo si z es un operador valido
			n = n + 1
			simbolos.append(z)# si es valido lo agrego a la lista simbolos
			ubicacion_simbolos.append(n)
		else:
			n = n + 1
			error.append(z) # agrega los caracteres que no cumplen las condiciones anteriores

	caracteres = numeros + simbolos # creo una lista con los numeros y operadores
	ubicacion = ubicacion_numeros + ubicacion_simbolos # creo una lista con el orden de los numeros y operandos
	diccionario = dict(zip(ubicacion,caracteres)) # creo un diccionario combinando las dos listas anteriores
	ubicacion.sort() # ordeno la lista para recorrerla posteriormemte

	final = []
	for x in ubicacion: # ordeno los valores del diccionario para crear una lista nueva
		for z in diccionario:
			if z == x:
				final.append(diccionario[z])
	salida = "".join(str(x) for x in final)# creo un string con la lista final

# descartando caracteres invalidos uso eval() para evaluar el string

	if error == []:
		try:
			resultado.set(eval(salida))
		except SyntaxError:
			resultado.set("Error de Sintaxis")
		except ZeroDivisionError:
			resultado.set("Division por cero")
	else:
		resultado.set("Error Datos no validos")


def reset():
	numero_a.set("")
	resultado.set("")

#botones de comandos

boton_suma = Button(ventana,text="EVALUAR",command=evaluar ,width=15)

boton_reset = Button(ventana,text="RESET",command=reset, width=15)
boton_salir = Button(ventana, text="SALIR",command=ventana.quit,width=15)

#salida de datos
res = Label(ventana,textvariable=resultado,bg="yellow",width=19,relief = SUNKEN)

#posicionamiento widgets

Label(ventana,text="",bg="orange").grid(row=0)
Label(ventana,text="INGRESE EXPRESION",bg="orange").grid(row=1)
numero_1.grid(row = 1,column=1)

Label(ventana,text="",bg="orange").grid(row=3)

boton_suma.grid(row = 4,column=0)


Label(ventana,text="",bg="orange").grid(row=6)

Label(ventana,text="RESULTADO").grid(row=7)
res.grid(row = 7, column=1)

Label(ventana,text="",bg="orange").grid(row=8)

boton_reset.grid(row =9,column=0)
boton_salir.grid(row = 9,column=1)

ventana.mainloop()
