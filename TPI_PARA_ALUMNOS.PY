from datetime import date
from enum import auto
import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("1- Cargar vehivulo")
            print("2- Modificar vehiculo")
            print("3- Borrar vehiculo")
            print("4- Cargar disponibilidad")
            print("5- Listar vehiculo")
            print("6- Aumentar precios Motocicletas")
            print("7- Mostrar registros Motocicletas")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número: "))

            if nro == 1:
                print("1- Cargar Automovil")
                print("2- Cargar Motocicleta")
                n = int(input("Por favor ingrese una opcion: "))
                
                if n == 1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio = input("Por favor ingrese el precio del automovil:  ")
                    cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                
                if n == 2:
                    marca = input("Por favor ingrese la marca de la motocicleta: ") 
                    modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                    cilindrada = input("Por favor ingrese la cilindrada de la motocicleta: ")
                    color = input("Por favor ingrese el color de la motocicleta: ")
                    precio = input("Por favor ingrese el precio de la motocicleta: ") 
                    nueva_motocicleta = Motocicleta(modelo,marca,cilindrada,color,precio)
                    nueva_motocicleta.cargar_motocicleta()
                    
            if nro ==2:
                print("1- modificar automovil")
                print("2- modificar motocicleta")
                nr = int(input("Por favor ingrese una opcion"))
                
                if nr == 1:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = input("Por favor ingrese el nuevo precio: ")
                    automovil_a_modificar = Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                    
                if nr == 2:
                    marca = input("Por favor ingrese la marca: ")
                    modelo = input("Por favor ingrese el modelo: ")
                    cilindrada = input("Por favor ingresar la cilindrada: ")
                    precio = input("Por favor ingrese el nuevo precio: ")
                    color = input("Por favor ingrese el color: ")
                    motocicleta_a_modificar = Motocicleta(marca,modelo,cilindrada,precio,color)
                    motocicleta_a_modificar.modificar_motocicletas()
            
            if nro==3:
                print("1- borrar automovil")
                print("2- Borrar motocicleta")
                num = int(input("Por favor ingrese una opcion"))
                
                if num == 1:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    autoABorrar=Automovil(marca, modelo)
                    autoABorrar.borrar_automovil()
                if num == 2:
                    marca = input("Por favor ingrese la marca: ")
                    modelo = input("Por favor ingrese el modelo: ")
                    cilindrada = input("Por favor ingrese la cilindrada: ")
                    motoABorrar=Motocicleta(marca, modelo)
                    motoABorrar.borrar_Motocicleta()
                
            if nro==4:  #cargar marca y modelo e incremetnar su valor en la base de datos
                marca = input("Ingrese marca del auto: ")
                modelo = input("Ingrese modelo del auto: ")
                automovil_a_incrementar=Automovil(marca,modelo)
                automovil_a_incrementar.cargar_disponibilidad()
                
            if nro==5: 
                    Automovil.listado_automoviles(Automovil)                    
            # if nro==6: aumentar precio motocicletas
            # if nro==7: mostrar registros motocicletas
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        #Elimina la tabla si exite
        conexion.miCursor.execute("DROP TABLE MOTOCICLETAS") 
        # Crea la tabla motocicleta si no existe
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY, modelo VARCHAR(30), marca VARCHAR(30), cilindrada VARCHAR(30), color VARCHAR(30), precio INTEGER, fechaUltimoPrecio date)")
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    # def validar():

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        # validar()
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo, self.precio, self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
            
            
    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            sql = "select * from AUTOMOVILES where marca = '"+ self.marca + "' and modelo = '" + self.modelo + "'"
            conexion.miCursor.execute(sql)
            rows = conexion.miCursor.fetchall()
            if  rows:
                sql = "update AUTOMOVILES SET cantidadDisponibles = cantidadDisponibles + 1 where marca = '" + self.marca + "' and modelo = '" + self.modelo + "'"
                conexion.miCursor.execute(sql) 
                conexion.miConexion.commit()
                print("Automovil cargado exitosamente")
    
            else:
                print ('no existen un automovil  marca ' + self.marca + ' -  modelo = ' + self.modelo )           
            
        except:
            print("Error al cargar automovil")
        finally:
            conexion.cerrarConexion()

    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}'" .format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil borrado exitosamente")
        except:
            print("Error al borrar un automovil")
        finally:
            conexion.cerrarConexion()

    def listado_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            if(autos):
                for auto in autos:
                    print("ID:",auto[0]," Marca:",auto[1]," Modelo:",auto[2]," Precio:",auto[3]," Cantidad disponible:", auto[4])
            else:
                print("No se han encontrado registros de automoviles")
        except:
            print("Error al listar automoviles")
        finally: 
            conexion.cerrarConexion
        

    # def validar():


class Motocicleta:   
 
    def __init__(self,modelo, marca, cilindrada, color, precio = None,fechaUltimoPrecio = date.today()):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.color = color
        self.precio = precio
        self.fechaUltimoPrecio = fechaUltimoPrecio
        

    def cargar_motocicleta(self):
        # Validar datos
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(modelo,marca,cilindrada,color,precio,fechaUltimoPrecio) VALUES('{}', '{}','{}','{}','{}','{}')".format(self.modelo,self.marca,self.cilindrada,self.color,self.precio,self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar una motocicleta")
        finally:
            conexion.cerrarConexion()

    # def aumentar_precios(self):

    # def mostrar_registros(self):

    # def validar():
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()