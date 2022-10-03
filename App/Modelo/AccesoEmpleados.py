import sys
sys.path.insert(1, 'H:\\MisionTIC\\Ciclo 3\\Proyecto\\Proyecto_Ciclo3\\App\\Servicios')
from Conexion import *

class AccesoEmpleados:
      
    def buscarEmpleado(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personal WHERE id_personar=%s",(id))
        respuesta = cursor.fetchall()
        return respuesta
    
    def listarEmpleados(self):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personal")
        respuesta = cursor.fetchall()
        return respuesta
    
    def crearEmpleados(self, dicc):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        nombres = dicc['nombres']
        apellidos = dicc['apellidos']
        documento = dicc['documento']
        telefono = dicc['telefono']
        correo = dicc['email']
        clave = dicc['documento'] 
        #consulta sql
        sql = "INSERT INTO `personal` (`nombres`, `apellidos`, `documento`, `telefono`, `email`, `rol`, `clave`) VALUES (%s, %s, %s, %s, %s,'Empleado', %s);"
        #variables a asignar en su %s campo correspondiente
        datos = (nombres, apellidos, documento, telefono, correo, clave)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def modificarEmpleados(self, dicc, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        nombres = dicc['nombres']
        apellidos = dicc['apellidos']
        documento = dicc['documento']
        telefono = dicc['telefono']
        correo = dicc['email']
        rol = dicc['rol']
        clave = dicc['clave'] 
        #consulta sql
        sql ="UPDATE personal SET nombres=%s, apellidos=%s, documento=%s, telefono=%s, email=%s, rol=%s, clave=%s WHERE id_personar=%s;"
        #variables a asignar en su %s campo correspondiente
        datos = (nombres, apellidos, documento, telefono, correo, rol, clave, id)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def eliminarEmpleados(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM personal WHERE id_personar=%s",(id))
        conn.commit()
        
    def iniciarsesion(self, user, clave):
        datos = (user, clave)
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personal WHERE email=%s AND clave=%s", datos)
        user = cursor.fetchone()
        conn.commit()
        return user
        