from datetime import date
from enum import auto
from conexiones import Conexiones
from motocicleta import Motocicleta
from automovil import Automovil

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("1- Cargar vehiculo")
            print("2- Modificar vehiculo")
            print("3- Borrar vehiculo")
            print("4- Cargar disponibilidad")
            print("5- Listar vehiculo")
            print("6- Aumentar precios Motocicletas")
            print("7- Mostrar registros Motocicletas")
            print("0- Salir de menu")

            try:
                nro = int(input("Por favor ingrese un número: "))
            except:
                print("Error! Debe ingresar un valor numerico")    
                continue

            if (nro<0 or nro>7):
                print("Error! Debe ingresar un número que corresponda con las opciones de menú")
                continue

            if nro == 1: #cargar automovil o motocicleta
                  
                while True:
                    print("1- Cargar Automovil")
                    print("2- Cargar Motocicleta")
                    try:
                        n = int(input("Por favor ingrese una opcion: "))
                    except:
                        print("Error! Debe ingresar un valor numerico")    
                        continue
                    if (n<1 or n>2):
                        print("Error! Debe ingresar un número que corresponda con las opciones de menú")
                        continue
                    break
                
                if n == 1: #cargar automovil
                    marca = self.validarStr(input("Por favor ingrese la marca del automovil: "))
                    modelo = self.validarStr(input("Por favor ingrese el modelo del automovil:"))    

                    validar = False    
                    while(not validar):
                        try:
                            precio = float(input("Por favor ingrese el precio del automovil: "))
                        except:
                            print("Error! Debe ingresar un valor numerico")
                            continue
                        validar = self.validarPrecio(precio)
                            
                    validar = False    
                    while(not validar):
                        try:
                            cantidadDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
                        except:
                            print("Error! Debe ingresar un número entero")
                            continue
                        validar = self.validarCantidad(cantidadDisponibles)

                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                
                if n == 2: #cargar motocicleta
                    marca = self.validarStr(input("Por favor ingrese la marca de la motocicleta: ")) 
                    modelo = self.validarStr(input("Por favor ingrese el modelo de la motocicleta: "))
                    cilindrada = self.validarStr(input("Por favor ingrese la cilindrada de la motocicleta: "))
                    color =  self.validarStr(input("Por favor ingrese el color de la motocicleta: "))
                    validar = False    
                    while(not validar):
                        try:
                            precio = int(input("Por favor ingrese el precio de la motocicleta: "))
                        except:
                            print("Error! Debe ingresar un valor numerico")
                            continue
                        validar = self.validarPrecio(precio)
                    nueva_motocicleta = Motocicleta(modelo,marca,cilindrada,color,precio)
                    nueva_motocicleta.cargar_motocicleta()
                    
            if nro ==2: #modificar automovil
                marca = self.validarStr(input("Por favor ingrese el nombre de la marca: "))
                modelo = self.validarStr(input("Por favor ingrese el nombre del modelo: "))
                validar = False    
                while(not validar):
                    try:
                        precio = float(input("Por favor ingrese el nuevo precio: "))
                    except:
                        print("Error! Debe ingresar un valor numerico")
                        continue
                    validar = self.validarPrecio(precio)
                automovil_a_modificar = Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
                    
            
            if nro==3: #borrar automovil
                marca = self.validarStr(input("Por favor ingrese el nombre de la marca: "))
                modelo = self.validarStr(input("Por favor ingrese el nombre del modelo: "))
                autoABorrar=Automovil(marca, modelo)
                autoABorrar.borrar_automovil()
                
            if nro==4:  #cargar marca y modelo e incremetnar su valor en la base de datos
                marca = self.validarStr(input("Por favor ingrese marca del auto: "))
                modelo = self.validarStr(input("Por favor ingrese modelo del auto: "))
                automovil_a_incrementar=Automovil(marca,modelo)
                automovil_a_incrementar.cargar_disponibilidad()

            if nro==5: #mostrar listado de automoviles
                Automovil.listado_automoviles(Automovil)    

            if nro==6: #aumentar precio motocicletas
                Motocicleta.aumentar_precios(Motocicleta)
            
            if nro==7: #mostrar registros motocicletas
                validar = False
                while (not validar):
                    try:
                        dia = int(input("Por favor ingrese día: "))
                        mes = int(input("Por favor ingrese mes: "))
                        anio = int(input("Por favor ingrese año: "))
                    except:
                        print("Error! Debe ingresar un numero entero")
                        continue
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

programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
    
