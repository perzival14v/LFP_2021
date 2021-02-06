from tkinter import filedialog
from tkinter import *
from Ordenamiento import Burbuja
import os


#Nombre = conjunto alphanumerico, debe iniciar con una letra
#Numero = conjunto de numeros del 0-9

listaMochileros =[]

class mochilero():
    def __init__(self):
        self.numbersNoOrdered = []
        self.numbersOrdered = None
        self.title = ""
        self.positions = None
        self.number_wanted=None





#Simbolos terminales
T=[" ",",","=","\n","\t"]
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

        mochila = mochilero()
        indice =-1
        for letter in line:
            indice+=1
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
                    mochila.numbersNoOrdered = numbers.copy()

                    group=""
                    type=""

            #Palabra
            elif type == "nombre":

                if letter.lower() in A or letter in N:
                    group = group + letter
                elif letter in T or letter == line[len(line)-1]:

                    #COMANDO
                    if group.lower() in C:
                        type = "comando"

                        if group.lower() == "ordenar":
                            #numbersOrdered=numbers.copy()
                            #numbersOrdered.sort()
                            numbersOrdered = Burbuja(numbers.copy())

                            mochila.numbersOrdered=numbersOrdered

                            group = ""
                            type = ""


                    elif letter == "=":
                        title = group
                        mochila.title = title

                        group = ""
                        type = ""

            elif type == "comando":
                if group.lower() == "buscar":
                    if letter in N:
                        numberWanted = numberWanted+letter
                        aux = []
                        position=1


                        if indice+1 == len(line):

                            mochila.number_wanted=numberWanted

                            for i in numbers:
                                if i == numberWanted:
                                    aux.append(position)
                                    position += 1
                                else:
                                    position += 1
                            if len(aux) != 0:
                                mochila.positions = aux
                            else:
                                mochila.positions = None

                            numberWanted = ""

                    elif letter in T:

                        mochila.number_wanted = numberWanted

                        for i in numbers:
                            if i==numberWanted:
                                aux.append(position)
                                position += 1
                            else:
                                position+=1
                        if len(aux)!=0:
                            mochila.positions=aux
                        else:
                            mochila.positions=None
                        numberWanted = ""
                        group = ""
                        type = ""



            if letter == "\n" or indice+1==len(line):

                if group.lower() in C:
                    type = "comando"

                    if group.lower() == "ordenar":
                        # numbersOrdered=numbers.copy()
                        # numbersOrdered.sort()
                        numbersOrdered = Burbuja(numbers.copy())

                        mochila.numbersOrdered = numbersOrdered

                        group = ""
                        type = ""


                listaMochileros.append(mochila)
                group = ""
                type = ""
                numbers=[]



    file.close()
