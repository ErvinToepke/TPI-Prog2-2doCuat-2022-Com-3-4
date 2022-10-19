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
                    marca = self.validarStr(input("Por favor ingrese la marca del automovil: "))
                    modelo = self.validarStr(input("Por favor ingrese el modelo del automovil:"))    

                    validar = False    
                    while(not validar):
                        try:
                            precio = float(input("Por favor ingrese el precio del automovil: "))
                        except TypeError:
                            print("Error! Debe ingresar un valor numerico")
                        finally:
                            validar = self.validarPrecio(precio)
                            
                    validar = False    
                    while(not validar):
                        try:
                            cantidadDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
                        except TypeError:
                            print("Error! Debe ingresar un número entero")
                        finally:
                            validar = self.validarCantidad(cantidadDisponibles)

                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                
                if n == 2:
                    marca = self.validarStr(input("Por favor ingrese la marca de la motocicleta: ")) 
                    modelo = self.validarStr(input("Por favor ingrese el modelo de la motocicleta: "))
                    cilindrada = self.validarStr(input("Por favor ingrese la cilindrada de la motocicleta: "))
                    color =  self.validarStr(input("Por favor ingrese el color de la motocicleta: "))
                    validar = False    
                    while(not validar):
                        try:
                            precio = float(input("Por favor ingrese el precio de la motocicleta: "))
                        except TypeError:
                            print("Error! Debe ingresar un valor numerico")
                        finally:
                            validar = self.validarPrecio(precio)
                    nueva_motocicleta = Motocicleta(modelo,marca,cilindrada,color,precio)
                    nueva_motocicleta.cargar_motocicleta()
                    
            if nro ==2:
                print("1- modificar automovil")
                # print("2- modificar motocicleta")
                n = int(input("Por favor ingrese una opcion"))
                
                if n == 1:
                    marca = self.validarStr(input("Por favor ingrese el nombre de la marca: "))
                    modelo = self.validarStr(input("Por favor ingrese el nombre del modelo: "))
                    validar = False    
                    while(not validar):
                        try:
                            precio = float(input("Por favor ingrese el nuevo precio: "))
                        except TypeError:
                            print("Error! Debe ingresar un valor numerico")
                        finally:
                            validar = self.validarPrecio(precio)
                    automovil_a_modificar = Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                    
                # if n == 2:
            
            if nro==3:
                print("1- borrar automovil")
                # print("2- Borrar motocicleta")
                n = int(input("Por favor ingrese una opcion"))
                
                if n == 1:
                    marca = self.validarStr(input("Por favor ingrese el nombre de la marca: "))
                    modelo = self.validarStr(input("Por favor ingrese el nombre del modelo: "))
                    autoABorrar=Automovil(marca, modelo)
                    autoABorrar.borrar_automovil()

                # if n == 2:
                
            if nro==4:  #cargar marca y modelo e incremetnar su valor en la base de datos
                marca = self.validarStr(input("Por favor ingrese marca del auto: "))
                modelo = self.validarStr(input("Por favor ingrese modelo del auto: "))
                automovil_a_incrementar=Automovil(marca,modelo)
                automovil_a_incrementar.cargar_disponibilidad()

            if nro==5:    
                Automovil.listado_automoviles(Automovil)    

            if nro==6: #aumentar precio motocicletas
                Motocicleta.aumentar_precios(Motocicleta)
            
            if nro==7: #mostrar registros motocicletas
                validar = False
                while validar:
                    try:
                        dia = int(input("Por favor ingrese día: "))
                        mes = int(input("Por favor ingrese mes: "))
                        anio = int(input("Por favor ingrese año: "))
                    except TypeError:
                        print("Error! Debe ingresar un numero entero")
                    finally:
                        validar = self.validarFecha(dia,mes, anio)
                Motocicleta.mostrar_registros(Motocicleta, date(anio,mes, dia))

            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miCursor.execute("DROP TABLE MOTOCICLETAS") 
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY, modelo VARCHAR(30), marca VARCHAR(30), cilindrada VARCHAR(30), color VARCHAR(30), precio INTEGER, fechaUltimoPrecio date)")
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETAS") 
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETAS (id_moto INTEGER PRIMARY KEY, modelo VARCHAR(30), marca VARCHAR(30), cilindrada VARCHAR(30), color VARCHAR(30), precio INTEGER, fechaUltimoPrecio date)")
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def validarStr(self, cadena):
        while True:
            if(len(cadena)>=30):
                print("Error! No se pueden exceder los 30 caracteres")
                cadena = input("Por favor ingrese nuevamente: ")
                continue
            break   
        return cadena
    
    def validarPrecio(self,precio):
        if(precio <= 0):
            print("Error! El precio no puede ser menor o igual a 0")
            return False
        return True

    def validarCantidad(self,cantidad):
        if(cantidad <= 0):
            print("Error! La cantidad no puede ser menor o igual a 0")
            return False
        return True

    def validarFecha(self,dia,mes,anio):
        if(not(0<dia<=31) or not(0<mes<=12) or not(0000<anio<=9999)):
            print("Error! Debe ingresar fecha con formato dd-mm-yyyy")
            return False
        return True

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        try:
            self.validar()
        except:
            print("Error al cargar datos del automovil")
        else:
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

    def validar(self):
        if(len(self.marca)>=30 or len(self.modelo)>=30 or self.precio <= 0 or self.cantidadDisponibles <=0):
            raise Exception
        elif(not type(self.marca) is str or not type(self.modelo) is str or not type(self.precio) is float or not type(self.cantidadDisponibles) is int):
            raise TypeError


class Motocicleta:   

    def __init__(self,modelo, marca, cilindrada, color, precio = None,fechaUltimoPrecio = date.today()):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.color = color
        self.precio = precio
        self.fechaUltimoPrecio = fechaUltimoPrecio
        

    def cargar_motocicleta(self):
        try:
            self.validar()
        except:
            print("Error al cargar datos del automovil")
        else:
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

    def guardar_registros(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            conexion.miCursor.executemany("INSERT INTO HISTORICO_MOTOCICLETAS VALUES(?,?,?,?,?,?,?)", motocicletas)
            conexion.miConexion.commit()
            print("Registros guardados exitosamente")
        except:
            print("Error al guardar registros")
        finally:
            conexion.cerrarConexion()

    def guardar_registros(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            conexion.miCursor.executemany("INSERT INTO HISTORICO_MOTOCICLETAS VALUES(?,?,?,?,?,?,?)", motocicletas)
            conexion.miConexion.commit()
            print("Registros guardados exitosamente")
        except:
            print("Error al guardar registros")
        finally:
            conexion.cerrarConexion()

    def aumentar_precios(self):
        self.guardar_registros(self)
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio = precio + precio * 0.1, fechaUltimoPrecio = '{}'".format(date.today()))
            conexion.miConexion.commit()
            print("Precios actualizados exitosamente")
        except:
            print("Error al actualizar precios")
        finally:
            conexion.cerrarConexion()

    def mostrar_registros(self, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS WHERE fechaUltimoPrecio = '{}'".format(fecha))
            registros = conexion.miCursor.fetchall()
            if(registros):
                for registro in registros:
                    print("ID:", registro[0]," Marca:",registro[1]," Modelo:",registro[2]," Cilindrada:",registro[3]," Color:",registro[4]," Precio:", registro[5]," Fecha ultimo precio:", registro[6])
            else:
                print("No se encuentran registros con fecha = ", date.strftime(fecha, "%d-%m-%Y"))
        except:
            print("Error al mostrar registros")
        finally: 
            conexion.cerrarConexion

    def validar(self):
        if(len(self.marca)>=30 or len(self.modelo)>=30 or len(self.cilindrada)>=30 or len(self.color)>=30 or self.precio <= 0):
            raise Exception
        elif(not type(self.marca) is str or not type(self.modelo) is str or not type(self.cilindrada) is str or not type(self.color) is str or not type(self.precio) is int):
            raise TypeError
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()