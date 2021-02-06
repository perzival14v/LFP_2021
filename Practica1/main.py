import webbrowser

import Automata


def web():
    file = open("reporte.html", "w")
    cabecera = """ <!DOCTYPE html>
                        <html>
                            <head>
                                <link rel="stylesheet" type="text/css" href="style.css">
                                <title>Reporte</title>
                            </head>
                             <body>
                                <div id=contenedor>
                                    <table class="tabla">"""
    file.write(cabecera)

    titulos = """
                                        <tr class="titulos">
                                            <td>Nombre</td>
                                            <td>Lista</td>
                                            <td>Ordenados</td>
                                            <td>Buscar</td>
                                        </tr>

        """
    file.write(titulos)

    for i in Automata.listaMochileros:
        mochila = i
        busqueda = ""

        if mochila.number_wanted != None:
            if mochila.positions != None:
                busqueda = str("Busqueda(" + str(mochila.number_wanted) + ") Posiciones = " + str(mochila.positions))
            else:
                busqueda = str("Busqueda(" + str(mochila.number_wanted) + ") = NO ENCONTRADO")

        fila = """<tr>
                    <td>""" + mochila.title + """</td>
                    """ + """<td> """ + str(mochila.numbersNoOrdered) + """ </td> 
                    """ + """<td> """ + str(mochila.numbersOrdered) + """ </td> 
                    """"""<td> """ + busqueda + """ </td> 
                    </tr>"""
        file.write(fila)

    pieDePagina = """
                                </table>
                            </div>
                        </body>
                    </html> """
    file.write(pieDePagina)

    file.close()
    webbrowser.open_new_tab("reporte.html")


opcion=0

while opcion!=6:


    print("1. Cargar Archivo de Entrada")
    print("2. Desplegar Listas Ordenadas")
    print("3. Desplegar Busquedas")
    print("4. Desplegar Todas")
    print("5. Desplegar Todas a Archivo")
    print("6. Salir")
    try:
        opcion = int(input("Ingrese un numero: "))
        print()
    except:
        print("Un error ha ocurrido")

    if(opcion==1):
        Automata.analizar()
        print("Archivo cargado y analizado con exito \n" )
    elif(opcion==2):


        for i in Automata.listaMochileros:
            mochila = Automata.mochilero()
            mochila = i
            if mochila.numbersOrdered != None:
                print(mochila.title + ": Ordenados = " + str(mochila.numbersOrdered))
        print()
    elif(opcion==3):
        for i in Automata.listaMochileros:
            mochila = Automata.mochilero()
            mochila = i
            if mochila.number_wanted != None:
                if mochila.positions != None:
                    print(mochila.title+": " + str(mochila.numbersNoOrdered) + " Busqueda(" + str(mochila.number_wanted)+") Posiciones = " + str(mochila.positions))
                else:
                    print(mochila.title+": " + str(mochila.numbersNoOrdered) + " Busqueda(" + str(mochila.number_wanted) + ") = NO ENCONTRADO" )

        print()
    elif (opcion == 4):
        #Listas Ordenadas
        for i in Automata.listaMochileros:
            mochila = Automata.mochilero()
            mochila = i
            if mochila.numbersOrdered != None:
                print(mochila.title + ": Ordenados = " + str(mochila.numbersOrdered))

        # Listas Buscadas
        for i in Automata.listaMochileros:
            mochila = Automata.mochilero()
            mochila = i
            if mochila.number_wanted != None:
                if mochila.positions != None:
                    print(mochila.title+": " + str(mochila.numbersNoOrdered) + " Busqueda(" + str(mochila.number_wanted)+") Posiciones = " + str(mochila.positions))
                else:
                    print(mochila.title+": " + str(mochila.numbersNoOrdered) + " Busqueda(" + str(mochila.number_wanted) + ") = NO ENCONTRADO" )
        print()
    elif (opcion == 5):
        web()
        print()
    elif (opcion == 6):
        break
    else:
        print("Valor no valido")
