from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bootstrap import Bootstrap

# creació y configuracion de la app 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:@localhost/flask_shopy_2687365' #DEFINIR  A QUE BASE DE DATOS NOS VAMOS A CONECTAR
app.config["SECRET_KEY"]="ESTODESBLOQUEATODO AJAJA 0214#$%"
bootstrap=Bootstrap(app)
# crear los objetos de sqlalchemy and migrate 
db =SQLAlchemy(app) #crear objeto de type sql 
migrate=Migrate(app, db)

#Modelos

class Cliente (db.Model):
    __tablename__="clientes" #renombrar las tablas 
    id=db.Column(db.Integer, primary_key=True) #Definir una columna y que es clave primaria
    username=db.Column(db.String(100), unique=True)#Es string y tiene longitud y valor unico
    email=db.Column(db.String(120),unique=True)
    password=db.Column(db.String(120))

class Producto (db.Model):
    __tablename__="productos" #renombrar las tablas 
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    precio=db.Column(db.Numeric(precision=10,scale=2)) #precicion numero de cifras enteras
    imagen =db.Column(db.String(100))


class Venta(db.Model):
    __tablename__="ventas" #renombrar las tablas 
    id=db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.DateTime , default =datetime.utcnow) #fecha por defecto y si no por defecto es la fecha actual
    cliente_id= db.Column(db.Integer,db.ForeignKey('clientes.id'))#hacer una llave foranea con la tabala cliente 

class Detalle(db.Model):
    __tablename__="detalles"
    id=db.Column(db.Integer,primary_key=True)
    venta_id= db.Column(db.Integer,db.ForeignKey('ventas.id'))#hacer una llave foranea con la tabala cliente 
    producto_id= db.Column(db.Integer,db.ForeignKey('productos.id'))#hacer una llave foranea con la tabala cliente 
    cantidad=db.Column(db.Integer)

#Definir el formulario de registro de productos 
class NuevoProductoForm(FlaskForm):
    nombre=StringField("Nombre de producto")
    precio=StringField("Precio del producto ")
    submit=SubmitField("Precione para enviar")




@app.route('/registrar_producto', methods=['GET','POST'] )
def registrar():
    form= NuevoProductoForm()
    #metodo para detectar cuando en el formulario se dio click en submit 
    if form.validate_on_submit():
        #registrar el producto 
        p=Producto()

        form.populate_obj(p)

        #Guardar
        db.session.add(p)
        db.session.commit()
        return "Producto Registrado"

    return render_template("registrar.html",
                           form=form)