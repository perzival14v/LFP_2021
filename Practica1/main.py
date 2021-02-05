import Automata

print("1. Cargar Archivo de Entrada")
print("2. Desplegar Lista Ordenadas")
print("3. Desplegar Busquedas")
print("4. Desplegar Todas")
print("5. Desplegar Todas a Archivo")
print("6. Salir")
try:
    opcion = int(input("Ingrese un numero: "))
except:
    print("Un error ha ocurrido")

if(opcion==1):
    Automata.analizar()
elif(opcion==2):
    print()
elif(opcion==3):
    print()
elif (opcion == 4):
    print()
elif (opcion == 5):
    print()
elif (opcion == 6):
    print()
else:
    print("Valor no valido")