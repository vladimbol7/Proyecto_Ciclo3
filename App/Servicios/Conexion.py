from flask import Flask, session
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

class Conexion:
    
    def conectar(self):
        app = Flask(__name__)
        app.secret_key = "super secret key"
        #conexion a la base de datos y session
        app.config['MYSQL_DATABASE_HOST'] = 'bltb97wngi2cqpgdjnn1-mysql.services.clever-cloud.com'
        app.config['MYSQL_DATABASE_USER'] = 'up5pi4xesi604foi'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'LJjClIiTOpajCoro2Mpk'
        app.config['MYSQL_DATABASE_DB'] = 'bltb97wngi2cqpgdjnn1'
        mysql = MySQL(cursorclass=DictCursor)
        mysql.init_app(app)
        return mysql