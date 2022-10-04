import sys
sys.path.insert(2, 'H:\\MisionTIC\\Ciclo 3\\Proyecto\\Proyecto_Ciclo3\\App\\Modelo')
from AccesoEmpleados import *
from AccesoItems import *
from AccesoProveedores import *
from flask import Flask, session
from flask import render_template,request,redirect
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "super secret key"

@app.route('/')
def index():
    return render_template('empleados/index.html')

@app.route('/buscarEmpleado', methods=['GET'])
def buscarEmpleado():
    id = request.args.get('id')
    empleado = AccesoEmpleados()
    usuario = empleado.buscarEmpleado(id)
    return usuario[0]

@app.route('/listarEmpleados', methods=['GET'])
def listarEmpleados():
    empleado = AccesoEmpleados()
    usuarios = empleado.listarEmpleados()
    return json.dumps(usuarios)

@app.route('/crearEmpleado', methods=['POST'])
def crearEmpleado():
    nombres = request.form['txtnombres']
    apellidos = request.form['txtapellidos']
    correo = request.form['txtcorreo']
    documento = request.form['txtdocumento']
    telefono = request.form['txttelefono']
    dicc = {'nombres':nombres, 'apellidos': apellidos, 'documento': documento, 'telefono': telefono, 'email': correo}
    empleado = AccesoEmpleados()
    usuarios = empleado.crearEmpleados(dicc)
    return "creacion exitosa"

@app.route('/modificarEmpleado/<int:id>', methods=['PUT'])
def modificarEmpleado(id):
    nombres = request.form['txtnombres']
    apellidos = request.form['txtapellidos']
    correo = request.form['txtcorreo']
    documento = request.form['txtdocumento']
    telefono = request.form['txttelefono']
    rol = request.form['txtrol']
    clave = request.form['txtclave']
    dicc = {'nombres':nombres, 'apellidos': apellidos, 'documento': documento, 'telefono': telefono, 'email': correo, 'rol': rol, 'clave': clave}
    empleado = AccesoEmpleados()
    usuarios = empleado.modificarEmpleados(dicc, id)
    return "actualización exitosa"

@app.route('/eliminarEmpleado/<int:id>', methods=['DELETE'])
def eliminarEmpleado(id):
    empleado = AccesoEmpleados()
    usuarios = empleado.eliminarEmpleados(id)
    return "eliminación exitosa"

@app.route('/iniciarsesion', methods=['POST'])
def login():
    #validación de si se esta usando el metodo post
    #recibe los datos del formulario de index.html
    email = request.form['email']
    clave = request.form['clave']
    empleado = AccesoEmpleados()
    user = empleado.iniciarsesion(email, clave)
    #pregunta si user no es NULL (es null cuando la consulta no devuelte ninguna fila)
    if user is not None:
        #guarda en variables de sesion los datos
        session['user'] = user['nombres'] + " " + user['apellidos']
        session['email'] = user['email']
        session ['id'] = user['id_personar']
        session['rol'] = user ['rol']
        #devuelve a la página de
        return  '''<h1>''' + "Bienvenido "+ session['rol'] + " "+session['user'] +'''</h1>'''
    else:
        return "Correo y/o contraseña incorrectos"

@app.route('/buscarItem', methods=['GET'])
def buscarItem():
    id = request.args.get('id')
    item = AccesoItems()
    elemento = item.buscarItem(id)
    return elemento[0]

@app.route('/listarItems', methods=['GET'])
def listarItems():
    item = AccesoItems()
    elemento = item.listarItems()
    return json.dumps(elemento)

@app.route('/crearItem', methods=['POST'])
def crearItem():
    descripcion = request.form['txtdescripcion']
    cantidad = request.form['txtcantidad']
    valorUnitario = request.form['txtvalorUnitario']
    idProveedor = request.form['txtidProveedor']
    idPersonal = request.form['txtidPersonal']
    dicc = {'descripcion':descripcion, 'cantidad': cantidad, 'valor_unitario': valorUnitario, 'id_proveedor': idProveedor, 'id_personar': idPersonal}
    item = AccesoItems()
    elemento = item.crearItem(dicc)
    return "creacion exitosa"

@app.route('/modificarItem/<int:id>', methods=['PUT'])
def modificarItem(id):
    descripcion = request.form['txtdescripcion']
    cantidad = request.form['txtcantidad']
    valorUnitario = request.form['txtvalorUnitario']
    idProveedor = request.form['txtidProveedor']
    idPersonal = request.form['txtidPersonal']
    dicc = {'descripcion':descripcion, 'cantidad': cantidad, 'valor_unitario': valorUnitario, 'id_proveedor': idProveedor, 'id_personar': idPersonal}
    item = AccesoItems()
    elemento = item.modificarItem(dicc, id)
    return "actualización exitosa"

@app.route('/eliminarItem/<int:id>', methods=['DELETE'])
def eliminarItem(id):
    item = AccesoItems()
    elemento = item.eliminarItem(id)
    return "eliminación exitosa"

@app.route('/buscarProveedor', methods=['GET'])
def buscarProveedor():
    id = request.args.get('id')
    proveedores = AccesoProveedores()
    proveedor = proveedores.buscarProveedor(id)
    return proveedor[0]

@app.route('/listarProveedores', methods=['GET'])
def listarProveedores():
    proveedores = AccesoProveedores()
    proveedor = proveedores.listarProveedores()
    return json.dumps(proveedor)

@app.route('/crearProveedor', methods=['POST'])
def crearProveedor():
    nombre = request.form['txtnombre']
    nit = request.form['txtnit']
    telefono = request.form['txttelefono']
    email = request.form['txtemail']
    dicc = {'nombre':nombre, 'nit': nit, 'telefono': telefono, 'email': email}
    proveedores = AccesoProveedores()
    proveedor = proveedores.crearProveedor(dicc)
    return "creacion exitosa"

@app.route('/modificarProveedor/<int:id>', methods=['PUT'])
def modificarProveedor(id):
    nombre = request.form['txtnombre']
    nit = request.form['txtnit']
    telefono = request.form['txttelefono']
    email = request.form['txtemail']
    dicc = {'nombre':nombre, 'nit': nit, 'telefono': telefono, 'email': email}
    proveedores = AccesoProveedores()
    proveedor = proveedores.modificarProveedor(dicc, id)
    return "actualización exitosa"

@app.route('/eliminarProveedor/<int:id>', methods=['DELETE'])
def eliminarProveedor(id):
    proveedores = AccesoProveedores()
    proveedor = proveedores.eliminarProveedor(id)
    return "eliminación exitosa"

if __name__ == '__main__':
    app.run()    