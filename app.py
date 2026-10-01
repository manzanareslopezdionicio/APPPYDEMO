from flask import Flask, render_template
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuracion de la base de datos
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)  

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ventas")
def ventas():
    return render_template("ventas.html")

@app.route("/login  ")
def login():
    return render_template("login.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/trabajo")
def trabajo():
    return render_template("trabajo.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

# Funcion de Login
@app.route("/login")

    

if __name__ == "__main__":
    app.run(debug=True)
