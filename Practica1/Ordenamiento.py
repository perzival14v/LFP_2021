
def Burbuja(lista):

    resultado=[]
    longitud=len(lista)
    min=None

    while longitud!=len(resultado):
        for i in lista:
            if min==None:
                min=int(i)
            elif int(i)<min:
                min=int(i)
        resultado.append(str(min))
        lista.remove(str(min))
        min=None


    return resultado
