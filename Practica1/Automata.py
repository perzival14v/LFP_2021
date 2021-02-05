from tkinter import filedialog
from tkinter import *
import os

#Nombre = conjunto alphanumerico, debe iniciar con una letra
#Numero = conjunto de numeros del 0-9


#Simbolos terminales
T=[" ",",","="]
#Alfabeto
A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
N=["0","1","2","3","4","5","6","7","8","9"]
#Comandos
C=["ordenar","buscar"]
numWithOutOrder=[]

def load():
    file = filedialog.askopenfile(mode="r",title = "Choose a file.")
    return file

def analizar():

    file = load()
    print()


    group=""
    type=""

    #Para organizar despues
    numbers=[]
    numbersOrdered=[]
    title=""

    #numero buscado de el comando buscar
    numberWanted = ""




    for line in file:
        for letter in line:
#Determinar el tipo inicial
            if group == "" and type=="":
                #numero
                if letter in N:
                    group = group + letter
                    type="numero"
                #palabra
                elif letter.lower() in A:
                    group = group + letter
                    type = "nombre"
#agregar el numero a una lista
            elif type=="numero":
                if letter in N:
                    group = group + letter
                elif letter in T:

                    numbers.append(group)

                    group=""
                    type=""

            #Palabra
            elif type == "nombre":

                if letter.lower() in A or letter in N:
                    group = group + letter
                elif letter in T or letter == line[len(line)-1]:

                    #COMANDO
                    if group.lower() in C:
                        type == "comando"

                        if group.lower() == "ordenar":
                            numbersOrdered=numbers.copy()
                            numbersOrdered.sort()



                    else:
                        title = group

                        group = ""
                        type = ""

            elif type == "comando":
                if group.lower() == "buscar ":
                    if letter in N:
                        numberWanted = letter

            if letter == line[len(line)-1]:
                print("Organizar info")


