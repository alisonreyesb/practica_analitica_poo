from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo

print("CALCULO AREA DE FIGURAS GEOMETRICAS")
print("1. Triangulo ")
print("2. Circulo ")
print("3. Rectangulo ")
print("4. Cuadrado")
print("5. Salir")

opcion=int(input("Ingrese la opcion que desea usar: "))

while True:
    if opcion==1:
        base=float(input("ingrese la medida de la base: "))
        altura=float(input("ingrese la medida de la altura: "))
        instancia=Triangulo(base,altura)
        area=instancia.area()
        print("el area del triangulo es: ",area)
        
    elif opcion==2:
        radio=float(input("Ingrese la medida del radio: "))
        instancia=Circulo(radio)
        area=instancia.area()
        print("El area del circulo es: ",area)
        
    elif opcion==3:
        base=float(input("ingrese la medida del ancho:" ))
        altura=float(input("ingrese la medida de la altura: " ))
        instancia=Rectangulo(base,altura)
        area=instancia.area()
        print("El area del rectangulo es: ", area)
        
        


