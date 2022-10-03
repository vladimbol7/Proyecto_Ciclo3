import sys
sys.path.insert(1, 'H:\\MisionTIC\\Ciclo 3\\Proyecto\\Proyecto_Ciclo3\\App\\Servicios')
from Conexion import *

class AccesoProveedores:
      
    def buscarProveedor(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proveedores WHERE id_proveedores=%s",(id))
        respuesta = cursor.fetchall()
        return respuesta
    
    def listarProveedores(self):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proveedores")
        respuesta = cursor.fetchall()
        return respuesta
    
    def crearProveedor(self, dicc):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        nombre = dicc['nombre']
        nit = dicc['nit']
        telefono = dicc['telefono']
        email = dicc['email']
        #consulta sql
        sql = "INSERT INTO `proveedores` (`nombre`, `nit`, `telefono`, `email`) VALUES (%s, %s, %s, %s);"
        #variables a asignar en su %s campo correspondiente
        datos = (nombre, nit, telefono, email)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def modificarProveedor(self, dicc, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        nombre = dicc['nombre']
        nit = dicc['nit']
        telefono = dicc['telefono']
        email = dicc['email']
        #consulta sql
        sql ="UPDATE proveedores SET nombre=%s, nit=%s, telefono=%s, email=%s WHERE id_proveedores=%s;"
        #variables a asignar en su %s campo correspondiente
        datos = (nombre, nit, telefono, email, id)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def eliminarProveedor(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proveedores WHERE id_proveedores=%s",(id))
        conn.commit()
        