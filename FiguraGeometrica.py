class FiguraGeometrica:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def area(self):
        raise NotImplementedError ("Este metodo debe ser calado por la subClase")
        