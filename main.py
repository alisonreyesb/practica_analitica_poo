#importacion de las clases
from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado
#Creacion del Menu
while True:
    print("CALCULO AREA DE FIGURAS GEOMETRICAS")
    print("1. Triangulo ")
    print("2. Circulo ")
    print("3. Rectangulo ")
    print("4. Cuadrado")
    print("5. Salir")
#Se solicita al usuario elegir la opcion que desea utilizar
    opcion=int(input("Ingrese la opcion que desea usar: "))
    
    if opcion==1:
#Se solicita las medidas para calcular el area del triangulo
        base=float(input("ingrese la medida de la base: "))
        altura=float(input("ingrese la medida de la altura: "))
        instancia=Triangulo(base,altura)
        area=instancia.area()
#Se imprime el resultado
        print("el area del triangulo es: ",area)
        
    elif opcion==2:
#Se solicita las medidas para calcular el area del circulo
        radio=float(input("Ingrese la medida del radio: "))
        instancia=Circulo(radio)
        area=instancia.area()
#Se imprime el resultado
        print("El area del circulo es: ",area)
        
    elif opcion==3:
#Se solicita las medidas para calcular el area del rectangulo
        base=float(input("ingrese la medida del ancho:" ))
        altura=float(input("ingrese la medida de la altura: " ))
        instancia=Rectangulo(base,altura)
        area=instancia.area()
#Se imprime el resultado
        print("El area del rectangulo es: ", area)
        
    elif opcion==4:
#e solicita las medidas para calcular el area del cuadrado
        lado=float(input("ingrese la medida del lado del cuadrado"))
        instancia=Cuadrado(lado)
        area=instancia.area()
#Se imprime el resultado
        print("El area del cuadrado es: ", area)
        
    elif opcion==5:
#Se rompe el ciclo
        print("Saliendo del programa...")
        break
    
        


