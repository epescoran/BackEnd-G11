class Silla:
    def __init__(self, ancho, alto, num_patas):
        self.ancho= ancho
        self.alto= alto
        self.num_patas=num_patas
    def listar_propiedades(self):
        return{
            'ancho': self.ancho,
            'alto':self.alto,
            'num_patas': self.num_patas
        }

silleta=Silla(ancho=40, alto=80, num_patas=4)
print(silleta.listar_propiedades())
sillon = Silla(ancho=200, alto=50, num_patas=6)
print(sillon.listar_propiedades())

