from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# creació y configuracion de la app 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:@localhost/flask_shopy_2687365' #DEFINIR  A QUE BASE DE DATOS NOS VAMOS A CONECTAR

# crear los objetos de sqlalchemy and migrate 
db =SQLAlchemy(app) #crear objeto de type sql 
migrate=Migrate(app, db)

#Modelos

class Cliente (db.Model):
    id=db.Column(db.Integer, primary_key=True) #Definir una columna y que es clave primaria
    username=db.Column(db.String(100), unique=True)#Es string y tiene longitud y valor unico
    email=db.Column(db.String(120),unique=True)
    password=db.Column(db.String(120))

class Producto (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    precio=db.Column(db.Numeric(precision=10,scale=2)) #precicion numero de cifras enteras
    imagen =db.Column(db.String(100))


class Venta(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.DateTime , default =datetime.utcnow) #fecha por defecto y si no por defecto es la fecha actual
    cliente_id= db.Column(db.Integer,db.ForeignKey('cliente.id'))#hacer una llave foranea con la tabala cliente 

class Detalle(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    venta_id= db.Column(db.Integer,db.ForeignKey('venta.id'))#hacer una llave foranea con la tabala cliente 
    producto_id= db.Column(db.Integer,db.ForeignKey('producto.id'))#hacer una llave foranea con la tabala cliente 
    cantidad=db.Column(db.Integer)
