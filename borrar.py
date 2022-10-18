class Vehiculo:
    def __init__(self, marca: str, ruedas: int, color: str, en_macha: bool):
      self.marca = marca
      self.ruedas = ruedas 
      self.color = color
      self.en_marcha = False
  
      
    def arrancar(self) -> bool:
        self.en_marcha = True
        return self.en_marcha

    def tipo_vehiculo(self):
        if(self.ruedas == 4):
            print("Es Un auto")
        else:
            print("Es una moto")
        
    def mostrar(self):
         print(self.marca)
         print(self.ruedas)
         print(self.color)
    
auto_bere=Vehiculo("chevorlet",4,"gris",True)
auto_bere.mostrar()