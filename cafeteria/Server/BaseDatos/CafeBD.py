import sqlite3

conexion = sqlite3.connect("Cafe.db")
cursor = conexion.cursor()


def read_image(filename):
    with open(filename, 'rb') as f:
        return f.read()
    
foto_menu1 = read_image('../static/assets/img/menu/Gatoccino.webp')
foto_menu2 = read_image('../static/assets/img/menu/Miau-pata.webp')
foto_menu3 = read_image('../static/assets/img/menu/miaucronizadas.webp')
foto_menu4 = read_image('../static/assets/img/menu/patas.webp')
foto_menu5 = read_image('../static/assets/img/menu/purr-fait.webp')
foto_menu6 = read_image('../static/assets/img/menu/Purrr-fe.webp')
foto_menu7 = read_image('../static/assets/img/menu/ratones.webp')
foto_menu8 = read_image('../static/assets/img/menu/Tazones.webp')


foto_gato1 = read_image('../static/assets/img/Gatos/Bengala.jpg')
foto_gato2 = read_image('../static/assets/img/Gatos/MaineCoon.jpeg')
foto_gato3 = read_image('../static/assets/img/Gatos/Siames.jpg')


def createadmin():
    cursor.execute("CREATE TABLE administrador(id_admin INTEGER primary key, nombre varchar(30), correo  varchar(50), contraseña varchar(10))")

def createGato():
    cursor.execute("""
    CREATE TABLE gatos (
        id_gato INTEGER PRIMARY KEY,
        nombre varchar(20),
        descripcion varchar(300),
        raza varchar(30),
        foto blob
        
    );
    """)


def createadopcion():
    cursor.execute("""
    CREATE TABLE adopcion (
        id_adopcion INTEGER PRIMARY KEY,
        id_gato INTEGER,
        nombre varchar(20),
        apellidoP varchar(20),
        apellidoM varchar(20),
        edad INTEGER,
        celular INTEGER,
        correo varchar(20),
        domicilio varchar(30),
                   
        parentesco varchar(20),
        nombre_ref varchar(20),
        celular_ref INTEGER,
        correo_ref varchar(20),
        domicilio_ref varchar(30),
                   
        FOREIGN KEY (id_gato) REFERENCES gatos (id_gato)
    );
    """)

def createmenu():
    cursor.execute("""
    CREATE TABLE menu (
        id_item INTEGER PRIMARY KEY,
        nombre varchar(20),
        descripcion varchar(50),
        foto blob,
        precio INTEGER
       
    );
    """)


def createusers():
    cursor.execute("""
    CREATE TABLE users (
        id_item INTEGER PRIMARY KEY,
        contraseña varchar(20),
    );
    """)    


def insertar_administradores():
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin1", "admin1@example.com", "contraseña1"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin2", "admin2@example.com", "contraseña2"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin3", "admin3@example.com", "contraseña3"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin4", "admin4@example.com", "contraseña4"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin5", "admin5@example.com", "contraseña5"))

def insertar_gatos():
    cursor.execute("INSERT INTO gatos (nombre, raza, foto, descripcion) VALUES (?, ?, ?, ?)", ("Garfield", "Persa", foto_gato1, "Descripcion1"))
    cursor.execute("INSERT INTO gatos (nombre, raza, foto, descripcion) VALUES (?, ?, ?, ?)", ("Mittens", "Siamés", foto_gato2, "Descripcion2"))
    cursor.execute("INSERT INTO gatos (nombre, raza, foto, descripcion) VALUES (?, ?, ?, ?)", ("Whiskers", "Maine Coon", foto_gato3, "Descripcion3"))

def insertar_adopciones():
    cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1, "Nombre1", "ApellidoP1", "ApellidoM1", 30, 1234567890, "correo1@example.com", "Domicilio1", "Parentesco1", "NombreRef1", 9876543210, "correoRef1@example.com", "DomicilioRef1"))
    cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (2, "Nombre2", "ApellidoP2", "ApellidoM2", 25, 2345678901, "correo2@example.com", "Domicilio2", "Parentesco2", "NombreRef2", 8765432109, "correoRef2@example.com", "DomicilioRef2"))
    cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (3, "Nombre3", "ApellidoP3", "ApellidoM3", 35, 3456789012, "correo3@example.com", "Domicilio3", "Parentesco3", "NombreRef3", 7654321098, "correoRef3@example.com", "DomicilioRef3"))
    cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1, "Nombre4", "ApellidoP4", "ApellidoM4", 28, 4567890123, "correo4@example.com", "Domicilio4", "Parentesco4", "NombreRef4", 6543210987, "correoRef4@example.com", "DomicilioRef4"))
    cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (2, "Nombre5", "ApellidoP5", "ApellidoM5", 32, 5678901234, "correo5@example.com", "Domicilio5", "Parentesco5", "NombreRef5", 5432109876, "correoRef5@example.com", "DomicilioRef5"))

def insertar_menu():
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Americano", "Un clásico café americano, preparado con espresso y agua caliente.", foto_menu1, 40))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Latte", "Un delicioso café latte, una combinación perfecta de espresso, leche vaporizada y un toque de espuma de leche.", foto_menu2, 40))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Espresso", "Un intenso café espresso, caracterizado por su sabor fuerte y aroma profundo.", foto_menu3, 50))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Mocha", "Un irresistible café mocha, una mezcla indulgente de espresso, leche vaporizada, chocolate y un toque de crema batida.", foto_menu4, 70))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Cappuccino", "Un clásico café cappuccino, equilibrado entre espresso, leche vaporizada y una generosa capa de espuma de leche.", foto_menu5, 80))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Cappuccino", "Una versión premium del café cappuccino, con espresso de calidad superior y una espuma de leche más densa.", foto_menu6, 100))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Cappuccino", "Un café cappuccino económico, perfecto para los amantes del café en busca de una opción más accesible.", foto_menu7, 4))
    cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES (?, ?, ?, ?)", ("Café Cappuccino", "Una opción de café cappuccino económica, con todo el sabor y la textura que te encanta.", foto_menu8, 4))


createadmin()
createmenu()
createGato()
createadopcion()

insertar_administradores()
insertar_gatos()
insertar_adopciones()
insertar_menu()




# Confirmar la inserción ejecutando commit en la conexión
conexion.commit()

# Cerrar la conexión con la base de datos cuando hayas terminado
conexion.close()


