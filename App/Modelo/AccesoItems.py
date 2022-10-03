import sys
sys.path.insert(1, 'H:\\MisionTIC\\Ciclo 3\\Proyecto\\Proyecto_Ciclo3\\App\\Servicios')
from Conexion import *

class AccesoItems:
      
    def buscarItem(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id_item=%s",(id))
        respuesta = cursor.fetchall()
        return respuesta
    
    def listarItems(self):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        respuesta = cursor.fetchall()
        return respuesta
    
    def crearItem(self, dicc):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        descripcion = dicc['descripcion']
        cantidad = dicc['cantidad']
        valorUnitario = dicc['valor_unitario']
        idProveedor = dicc['id_proveedor']
        idPersonal = dicc['id_personar']
        #consulta sql
        sql = "INSERT INTO `items` (`descripcion`, `cantidad`, `valor_unitario`, `id_proveedor`, `id_personar`) VALUES (%s, %s, %s, %s, %s);"
        #variables a asignar en su %s campo correspondiente
        datos = (descripcion, cantidad, valorUnitario, idProveedor, idPersonal)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def modificarItem(self, dicc, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        descripcion = dicc['descripcion']
        cantidad = dicc['cantidad']
        valorUnitario = dicc['valor_unitario']
        idProveedor = dicc['id_proveedor']
        idPersonal = dicc['id_personar']
        #consulta sql
        sql ="UPDATE items SET descripcion=%s, cantidad=%s, valor_unitario=%s, id_proveedor=%s, id_personar=%s WHERE id_item=%s;"
        #variables a asignar en su %s campo correspondiente
        datos = (descripcion, cantidad, valorUnitario, idProveedor, idPersonal, id)
        #parte de la conexion
        conn = mysql.connect()
        cursor= conn.cursor()
        #ejecutar la consulta con los datos
        cursor.execute(sql, datos)
        conn.commit()
        
    def eliminarItem(self, id):
        conexionSql = Conexion()
        mysql = conexionSql.conectar()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id_item=%s",(id))
        conn.commit()
        