class Palabras ():
    def __init__(self, palabra):
        self.palabra =["Mi", "Diario", "Python"]
        
    def convertir(self):
        for pala in (self.palabra,):
            print self.palabra [::-1]
mipalabra=Palabras(0)
mipalabra.convertir()