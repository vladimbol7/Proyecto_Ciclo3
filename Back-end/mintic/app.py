from flask import Flask,session
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
app.secret_key = "super secret key"
#conexion a la base de datos y session
app.config['MYSQL_DATABASE_HOST'] = 'bltb97wngi2cqpgdjnn1-mysql.services.clever-cloud.com'
app.config['MYSQL_DATABASE_USER'] = 'up5pi4xesi604foi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'LJjClIiTOpajCoro2Mpk'
app.config['MYSQL_DATABASE_DB'] = 'bltb97wngi2cqpgdjnn1'
mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)

#index
@app.route('/')
def index():
    return render_template('empleados/index.html')

@app.route('/editar/<int:id>')
def editar(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal WHERE id_personar=%s",(id))
    empleados = cursor.fetchall()

    return render_template('empleados/editarempleado.html',empleado = empleados[0])

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualiza(id):
    nombres = request.form['txtnombres']
    apellidos = request.form['txtapellidos']
    correo = request.form['txtcorreo']
    documento = request.form['txtdocumento']
    telefono = request.form['txttelefono']
    #consulta sql
    sql ="UPDATE personal SET nombres=%s,apellidos=%s,email=%s,documento=%s,telefono=%s,clave=%s WHERE id_personar=%s;"
    #variables a asignar en su %s campo correspondiente
    datos = (nombres,apellidos,correo,documento,telefono,documento,id)
    #parte de la conexion
    conn = mysql.connect()
    cursor= conn.cursor()
    #ejecutar la consulta con los datos
    cursor.execute(sql,datos)
    conn.commit()
    #redirigir a agregar empleados denuevo
    return redirect('/crearnuevoempleado')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personal WHERE id_personar=%s",(id))
    conn.commit()
    return redirect('/crearnuevoempleado')

#pagina de /crearnuevoempleado 
@app.route('/crearnuevoempleado')
def crearnuevoempleado():
    #validacion de si existe el user para no poder entrar a traves del buscador
    if not session.get('user'):
        #redirecciona a index (formulario de inicio de sesion)
        return render_template('empleados/index.html')
    else:
        #redirecciona a pagina de crear nuevo empleado
        sql = "SELECT * FROM `personal` WHERE rol='Empleado';"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        empleados = cursor.fetchall()
        return render_template('empleados/crearnuevoempleado.html', empleados = empleados)

@app.route('/empleado', methods=['POST'])
def insertarEmpleado():
    #toma de datos a partir del formulario de crearnuevoempleado.html
    nombres = request.form['txtnombres']
    apellidos = request.form['txtapellidos']
    correo = request.form['txtcorreo']
    documento = request.form['txtdocumento']
    telefono = request.form['txttelefono']
    #consulta sql
    sql ="INSERT INTO `personal`(`nombres`, `apellidos`, `documento`, `telefono`, `email`, `rol`,`clave`) VALUES (%s,%s,%s,%s,%s,'Empleado',%s);"
    #variables a asignar en su %s campo correspondiente
    datos = (nombres,apellidos,documento,telefono,correo,documento)
    #parte de la conexion
    conn = mysql.connect()
    cursor= conn.cursor()
    #ejecutar la consulta con los datos
    cursor.execute(sql,datos)
    conn.commit()
    #redirigir a agregar empleados denuevo
    return redirect('/crearnuevoempleado')

@app.route('/iniciarsesion', methods=['POST'])
def login():
    #validación de si se esta usando el metodo post
    if request.method == 'POST':
        #recibe los datos del formulario de index.html
        email = request.form['email']
        clave = request.form['clave']
        #datos que se introduciran a la consulta
        datos =(email,clave)
        conn = mysql.connect()
        cursor= conn.cursor()
        #preparar la consulta
        cursor.execute("SELECT * FROM personal WHERE email=%s AND clave=%s",datos)
        #se guarda la información de la consulta en la variable user
        user = cursor.fetchone()
        conn.commit()
        #pregunta si user no es NULL (es null cuando la consulta no devuelte ninguna fila)
        if user is not None:
            #guarda en variables de sesion los datos
            if user['rol'] == 'ADMIN':
                session['user'] = user['nombres'] +" " + user['apellidos']
                session['email'] = user['email']
                session ['id'] = user['id_personar']
                session['rol'] = user ['rol']
                #devuelve a la página de
                return  '''<h1>''' + "Bienvenido "+ session['rol'] + " "+session['user'] +'''</h1>'''+ render_template('empleados/seleccion.html')
        else:
            return "Correo y/o contraseña incorrectos" + render_template('empleados/index.html')
    else:
        return render_template('empleados/index.html')

if __name__== '__main__':
    app.run(debug=True)