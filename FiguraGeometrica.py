class FiguraGeometrica:
    def __int__(self,nombre):
        self.nombre=nombre
        
    def area(self):
        raise NotImplementedError ("Este metodo debe ser calado por la subClase")
        