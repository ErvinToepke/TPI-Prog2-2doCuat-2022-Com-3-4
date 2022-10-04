import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("1- Cargar Automovil")
            print("2- Modificar Automovil")
            print("3- Borrar Automovil")
            print("4- Cargar disponibilidad")
            print("5- Listar Automoviles")
            print("6- Cargar Motocicleta")
            print("7- Aumentar precios Motocicletas")
            print("8- Mostrar registros Motocicletas")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
            # if nro==3: borrar auto
            # if nro==4: cargar disponibilidad
            # if nro==5: listar automoviles
            # if nro==6: cargar motocicleta
            # if nro==7: aumentar precio motocicletas
            # if nro==8: mostrar registros motocicletas
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        #Elimina la tabla si exite
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS") 
        # Crea la tabla motocicleta
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY, modelo VARCHAR(30), marca VARCHAR(30), cilindrada VARCHAR(30), precio INTEGER, color VARCHAR(30), fechaUltimoPrecio datetime)")
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automoviles(self, precio: float, marca: str, modelo:str):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{precio}' where marca='{marca}' and modelo='{modelo}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  

    # def borrar_automovil(self):
        # conexion = Conexiones()
        # conexion.abrirConexion()
        # try:
        #     conexion.miCursor.execute("")
        #     conexion.miConexion.commit()
        #     print("Automovid borrado exitosamente")
        # except:
        #     print("Error al borrar un automovil")
        # finally:
        #     conexion.cerrarConexion()

    # def cargar_disponibilidad(self):

    # def listado_automoviles(self):


class Motocicleta:   
 
    def __init__(self,modelo, marca, cilindrada, color, precio = None , fechaUltimoPrecio= None):
        self.modelo = modelo
        self.marca = marca
        self.cilindrada = cilindrada
        self.color = color
        self.precio = precio
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(modelo,marca,cilindrada,precio,fechaUltimoPrecio) VALUES('{}', '{}','{}','{}','{}')".format(self.modelo,self.marca,self.cilindrada,self.precio,self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar una motocicleta")
        finally:
            conexion.cerrarConexion()

    # def aumentar_precios(self):

    # def mostrar_registros(self):
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
# programa.abrirConexion()