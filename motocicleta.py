from datetime import date
from conexiones import Conexiones

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
            print("Error al cargar datos de la motocicleta")
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