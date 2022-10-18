class Animal:
    def __init__(self, especie: str, raza: str, peso_promedio: float, vida_promedio: float, carnivoro: bool, *crias_promedio: float):
        self.especie = especie
        self.raza = raza
        self.peso_promedio = peso_promedio
        self.vida_promedio = vida_promedio
        self.carnivoro = carnivoro
        self.crias_promedio = crias_promedio
        
    def mostrar(self):
        print("Especie: ", self.especie)
        print("Raza: ", self.raza)
        print("Peso promedio: ", self.peso_promedio)
        print("Vida promedio: ", self.vida_promedio)
        print("Carnivoro: ", self.carnivoro)    
        print("Crias promedio: ", self.crias_promedio)  
        
    def categorizar_peso(self, peso : float):
        self.peso_promedio = peso
        if(peso < 10):
            print("Liviano")
        elif(peso >= 10 and peso < 20):
            print("Mediano")
        else:
            print("Pesado")
            
                    
gato=Animal("gatos", "montes", 15.50, 7.00, True, 12.5)
gato.mostrar()
gato.categorizar_peso(50.5)