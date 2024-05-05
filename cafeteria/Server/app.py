from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import base64

import sqlite3


app = Flask(__name__)
CORS(app)


def get_db_connection():
    return sqlite3.connect("Cafe.db")

@app.route("/")
def solicitudes():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM menu")
        menu = cur.fetchall()
        cur.execute("SELECT * FROM gatos")
        gatos = cur.fetchall()

    con.close()

    

    menu_con_imagenes_base64 = []
    for plati in menu:
        id = plati[0]
        nombre = plati[1]
        descripcion = plati[2]
        foto_base64 = base64.b64encode(plati[3]).decode('utf-8')
        precio = plati[4]
        menu_con_imagenes_base64.append((id, nombre, descripcion, foto_base64,precio))

    gatos_con_imagenes_base64 = []
    for gato in gatos:
        id = gato[0]
        nombre = gato[1]
        descripcion = gato[2]
        foto_base64 = base64.b64encode(gato[4]).decode('utf-8')
        raza = gato[3]
        gatos_con_imagenes_base64.append((id, nombre, descripcion, raza,foto_base64))
    
    
    return render_template("index.html", menu=menu_con_imagenes_base64, gato = gatos_con_imagenes_base64) 


@app.route("/IndexAdmin")
def IndexAdmin():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM menu")
        menu = cur.fetchall()
        cur.execute("SELECT * FROM gatos")
        gatos = cur.fetchall()

    con.close()

    

    menu_con_imagenes_base64 = []
    for plati in menu:
        id = plati[0]
        nombre = plati[1]
        descripcion = plati[2]
        foto_base64 = base64.b64encode(plati[3]).decode('utf-8')
        precio = plati[4]
        menu_con_imagenes_base64.append((id, nombre, descripcion, foto_base64,precio))

    gatos_con_imagenes_base64 = []
    for gato in gatos:
        id = gato[0]
        nombre = gato[1]
        descripcion = gato[2]
        foto_base64 = base64.b64encode(gato[4]).decode('utf-8')
        raza = gato[3]
        gatos_con_imagenes_base64.append((id, nombre, descripcion, raza,foto_base64))
    
    
    return render_template("indexAdmin.html", menu=menu_con_imagenes_base64, gato = gatos_con_imagenes_base64) 



@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/adopcion")
def adopcion():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM gatos")
        gatos = cur.fetchall()

    gatos_con_imagenes_base64 = []
    for gato in gatos:
        id = gato[0]
        nombre = gato[1]
        descripcion = gato[2]
        foto_base64 = base64.b64encode(gato[4]).decode('utf-8')
        raza = gato[3]
        gatos_con_imagenes_base64.append((id, nombre, descripcion, raza,foto_base64))

    con.close()
    return render_template("adopcion.html", gatos=gatos_con_imagenes_base64)  

@app.route('/adopcionAdmin')
def adopcionAdmin():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM adopcion")
        adopcion = cur.fetchall()

    con.close()
    return render_template("adopcionAdmin.html", adopcion=adopcion)

@app.route('/agregarAdopcion')
def agregarAdopcion():
    
    return render_template("login.html")

@app.route("/agregarPlatillo")
def agregarPlatillo():
    return render_template("AgregarPlatillo.html")

@app.route("/agregarGato")
def agregarGato():
    return render_template("AgregarGato.html")

@app.route("/agregarP", methods=['POST'])
def agregarP():
    con = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            print(nombre)
            desc = request.form['descripcion']
            precio = request.form['precio']
            foto = request.files['imagen']
            
            fottito =  foto.read()
            with get_db_connection() as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO menu (nombre, descripcion, foto, precio) VALUES ( ?, ?, ?, ?)", (nombre,desc, fottito,int(precio)))
                con.commit()
                print("record instert")

            
        except Exception as e:    
            con.rollback()
            msg = "Error in the INSERT"
            print(e)  # Imprimir la excepción para depuración

        finally:    
            con.close()    
            return IndexAdmin()
        
@app.route("/agregarG", methods=['POST'])
def agregarG():
    con = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            print(nombre)
            desc = request.form['descripcion']
            raza = request.form['raza']
            foto = request.files['imagen']
            
            fotito =  foto.read()
            with get_db_connection() as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO gatos (nombre, descripcion, raza, foto) VALUES ( ?, ?, ?, ?)", (nombre,desc, raza,fotito))
                con.commit()
                print("record instert")

            
        except Exception as e:    
            con.rollback()
            msg = "Error in the INSERT"
            print(e)  # Imprimir la excepción para depuración

        finally:    
            con.close()    
            return IndexAdmin()

@app.route("/eliminarA", methods=['POST'])
def eliminarA():
    con = None
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id_adopcion']
            print(rowid)
            # Connect to the database and DELETE a specific record based on rowid
            with get_db_connection() as con:
                    cur = con.cursor()
                    print("hola")
                    cur.execute("DELETE FROM adopcion WHERE id_adopcion = ?", (rowid,))
                    print("borrado")
                    con.commit()
                    msg = "Record successfully deleted from the database"

            
        except:
            if con:
                con.rollback()
            msg = "Error in the DELETE"

        finally:
            if con:
                con.close()
            # Send the transaction message to result.html
            return adopcionAdmin()



@app.route("/eliminarP", methods=['POST'])
def eliminarP():
    con = None
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            print(rowid)
            # Connect to the database and DELETE a specific record based on rowid
            with get_db_connection() as con:
                    cur = con.cursor()
                    print("hola")
                    cur.execute("DELETE FROM menu WHERE id_item = ?", (rowid,))
                    print("borrado")
                    con.commit()
                    msg = "Record successfully deleted from the database"

            
        except:
            if con:
                con.rollback()
            msg = "Error in the DELETE"

        finally:
            if con:
                con.close()
            # Send the transaction message to result.html
            return IndexAdmin()
        
@app.route("/eliminarG", methods=['POST'])
def eliminarG():
    con = None
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            print(rowid)
            # Connect to the database and DELETE a specific record based on rowid
            with get_db_connection() as con:
                    cur = con.cursor()
                    print("hola")
                    cur.execute("DELETE FROM gatos WHERE id_gato = ?", (rowid,))
                    print("borrado")
                    con.commit()
                    msg = "Record successfully deleted from the database"

            
        except:
            if con:
                con.rollback()
            msg = "Error in the DELETE"

        finally:
            if con:
                con.close()
            # Send the transaction message to result.html
            return IndexAdmin()

@app.route("/editarPlatillo", methods=['POST'])
def editarPlatillo():
    row=None
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['id']
            print(id)
            
            with get_db_connection() as con:
                cur = con.cursor()
                print("hola")
                cur.execute("SELECT * FROM menu WHERE id_item = ?", (id,))
                row = cur.fetchall()
                msg = "Record successfully deleted from the database"
        except:
            id=None
            return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401

        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("EditarPlatillo.html",rows=row)

@app.route("/editarGato", methods=['POST'])
def editarGato():
    row=None
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['id']
            print(id)
            
            with get_db_connection() as con:
                cur = con.cursor()
                print("hola")
                cur.execute("SELECT * FROM gatos WHERE id_gato = ?", (id,))
                row = cur.fetchall()
                msg = "Record successfully deleted from the database"
        except:
            id=None
            return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401

        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("EditarGato.html",rows=row)

@app.route("/editarP", methods=['POST'])
def editarP():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario HTML
        rowid = request.form['id']
        nuevo_nombre = request.form['nombre']
        nuena_descricpcion = request.form['descripcion']
        nuevo_precio = request.form['precio']
        foto = request.files['imagen']
        
        try:
            with get_db_connection() as con:
                cur = con.cursor()
                # Realizar la actualización en la tabla 'menu'
                cur.execute("UPDATE menu SET nombre = ?, descripcion = ?, precio = ? WHERE id_item = ?", (nuevo_nombre, nuena_descricpcion, nuevo_precio, rowid))
                con.commit()
                msg = "Registro actualizado correctamente"
        except Exception as e:
            print(str(e))
            msg = "Error al actualizar el registro"
            return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401

        
        # Redireccionar o renderizar una plantilla con un mensaje de éxito
        return IndexAdmin()

@app.route("/editarG", methods=['POST'])
def editarG():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario HTML
        rowid = request.form['id']
        nuevo_nombre = request.form['nombre']
        nuena_descricpcion = request.form['descripcion']
        nuevo_raza = request.form['raza']
        
        try:
            with get_db_connection() as con:
                cur = con.cursor()
                # Realizar la actualización en la tabla 'menu'
                cur.execute("UPDATE gatos SET nombre = ?, descripcion = ?, raza = ? WHERE id_gato = ?", (nuevo_nombre, nuena_descricpcion, nuevo_raza, rowid))
                con.commit()
                msg = "Registro actualizado correctamente"
        except Exception as e:
            print(str(e))
            msg = "Error al actualizar el registro"
            return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401
        
        # Redireccionar o renderizar una plantilla con un mensaje de éxito
        return IndexAdmin()

@app.route('/validar', methods=['POST'])
def validar():
    if request.method == 'POST':
        try:
            email = request.form['username']
            contraseña = request.form['password']
            with get_db_connection() as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM administrador WHERE correo=? AND contraseña=?", (email, contraseña))
                administrador = cursor.fetchone()
                cursor.execute("SELECT * FROM menu")
                menu = cursor.fetchall()  # Cambiado de cur a cursor
                cursor.execute("SELECT * FROM gatos")
                gatos = cursor.fetchall()

                menu_con_imagenes_base64 = []
                for plati in menu:
                    id = plati[0]
                    nombre = plati[1]
                    descripcion = plati[2]
                    foto_base64 = base64.b64encode(plati[3]).decode('utf-8')
                    precio = plati[4]
                    menu_con_imagenes_base64.append((id, nombre, descripcion, foto_base64, precio))

                gatos_con_imagenes_base64 = []
                for gato in gatos:
                    id = gato[0]
                    nombre = gato[1]
                    descripcion = gato[2]
                    foto_base64 = base64.b64encode(gato[4]).decode('utf-8')
                    raza = gato[3]
                    gatos_con_imagenes_base64.append((id, nombre, descripcion, raza, foto_base64))
            
        except Exception as e:    
            con.rollback()
            msg = "Error in the INSERT"
            print(e)  # Imprimir la excepción para depuración

        finally:        
            con.close() 
            if administrador:
                return render_template("indexAdmin.html", user=administrador, menu=menu_con_imagenes_base64, gato=gatos_con_imagenes_base64)
            else:
                return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401

@app.route("/agregarA", methods=['POST'])
def agregarA():
    con = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            print(nombre)
            apellidoP = request.form['apellidoPat']
            apellidoM = request.form['apellidoMat']
            edad = request.form['edad']
            celular = request.form['cel']
            correo = request.form['correo']
            domicilio = request.form['dom']
            

            gato = request.form['gato']
            print(gato)
            parenezco = request.form['paren']
            nombreO = request.form['nombrecom']
            
            celularO = request.form['celO']
            correoO = request.form['corr']
            domicilioO = request.form['domO']
            
            with get_db_connection() as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO adopcion (id_gato, nombre, apellidoP, apellidoM, edad, celular, correo, domicilio, parentesco, nombre_ref, celular_ref, correo_ref, domicilio_ref) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1,nombre,apellidoP, apellidoM, edad, celular, correo, domicilio, parenezco, nombreO, celularO, correoO, domicilioO))
                con.commit()
                print("record instert")
            
                       
        except Exception as e:    
            con.rollback()
            msg = "Error in the INSERT"
            print(e)  
            return jsonify({'message': 'SOLICITUD FALLIDA'}), 401# Imprimir la excepción para depuración

        finally:    
            con.close()    
            return jsonify({'message': 'SOLICITUD EXCITOSA'}), 201
        





if __name__ == '__main__':
    app.run(debug=True)
