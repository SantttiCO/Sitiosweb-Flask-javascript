from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return sqlite3.connect("videojuego.db")

admin_Logeado = []


def get_db_connection():
    return sqlite3.connect("videojuego.db")


@app.route("/")
def start():
    
    return index()

@app.route("/index")
def index():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT SUM(CASE WHEN sexo = 1 THEN 1 ELSE 0 END) as hombres, SUM(CASE WHEN sexo = 0 THEN 1 ELSE 0 END) as mujeres FROM jugadores")
        sexoresult = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top10 = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top10Neg = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top5M = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top5MN = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top5H = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top5HN = cur.fetchall()
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 1'
        """)
        topNivel1 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 1' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 1'
        );
        """)
        topNivel1Players = cur.fetchall()
        
        #nivel2
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 2'
        """)
        topNivel2 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 2' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 2'
        );
        """)
        topNivel2Players = cur.fetchall()

        #nivel3
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 3'
        """)
        topNivel3 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 3' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 3'
        );
        """)
        topNivel3Players = cur.fetchall()
        cur.execute("SELECT AVG(progreso) FROM sesion;")
        promedio = cur.fetchall()

    
    promedio_progreso = promedio[0][0]
    # Convertir el promedio en porcentaje
    porcentaje_progreso = round((promedio_progreso / 3) * 100,2)
    print(porcentaje_progreso)

    top5M = [dict(user_name=row[0], puntaje=row[1]) for row in top5M]
    top5MN = [dict(user_name=row[0], puntaje=row[1]) for row in top5MN]

    top5H = [dict(user_name=row[0], puntaje=row[1]) for row in top5H]
    top5HN = [dict(user_name=row[0], puntaje=row[1]) for row in top5HN]

    top10Neg = [dict(user_name=row[0], puntaje=row[1]) for row in top10Neg]
    top10 = [dict(user_name=row[0], puntaje=row[1]) for row in top10]
    
    con.close()


    return render_template('index.html', admin_Logeado = admin_Logeado, porcentaje_progreso = porcentaje_progreso ,topNivel3 = topNivel3, topNivel3Players = topNivel3Players ,topNivel2 = topNivel2, topNivel2Players = topNivel2Players , topNivel1 = topNivel1, topNivel1Players = topNivel1Players, sexo = sexoresult, top10=top10, top10Neg=top10Neg, top5M=top5M, top5MN=top5MN, top5H=top5H, top5HN=top5HN)


@app.route("/IndexAdmin")
def IndexAdmin():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT SUM(CASE WHEN sexo = 1 THEN 1 ELSE 0 END) as hombres, SUM(CASE WHEN sexo = 0 THEN 1 ELSE 0 END) as mujeres FROM jugadores")
        sexoresult = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top10 = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top10Neg = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top5M = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 0
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top5MN = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje DESC
        LIMIT 5
        """)
        top5H = cur.fetchall()
        cur.execute("""
        SELECT user_name, puntaje
        FROM jugadores
        INNER JOIN sesion ON jugadores.id_jugador = sesion.id_jugador
        WHERE jugadores.sexo = 1
        ORDER BY puntaje ASC
        LIMIT 5
        """)
        top5HN = cur.fetchall()
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 1'
        """)
        topNivel1 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 1' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 1'
        );
        """)
        topNivel1Players = cur.fetchall()
        
        #nivel2
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 2'
        """)
        topNivel2 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 2' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 2'
        );
        """)
        topNivel2Players = cur.fetchall()

        #nivel3
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 3'
        """)
        topNivel3 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel 3' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel 3'
        );
        """)
        topNivel3Players = cur.fetchall()
        cur.execute("SELECT AVG(progreso) FROM sesion;")
        promedio = cur.fetchall()

    
    promedio_progreso = promedio[0][0]
    # Convertir el promedio en porcentaje
    porcentaje_progreso = round((promedio_progreso / 3) * 100,2)
    print(porcentaje_progreso)

    top5M = [dict(user_name=row[0], puntaje=row[1]) for row in top5M]
    top5MN = [dict(user_name=row[0], puntaje=row[1]) for row in top5MN]

    top5H = [dict(user_name=row[0], puntaje=row[1]) for row in top5H]
    top5HN = [dict(user_name=row[0], puntaje=row[1]) for row in top5HN]

    top10Neg = [dict(user_name=row[0], puntaje=row[1]) for row in top10Neg]
    top10 = [dict(user_name=row[0], puntaje=row[1]) for row in top10]
    
    con.close()


    return render_template('indexAdmin.html', admin_Logeado = admin_Logeado, porcentaje_progreso = porcentaje_progreso ,topNivel3 = topNivel3, topNivel3Players = topNivel3Players ,topNivel2 = topNivel2, topNivel2Players = topNivel2Players , topNivel1 = topNivel1, topNivel1Players = topNivel1Players, sexo = sexoresult, top10=top10, top10Neg=top10Neg, top5M=top5M, top5MN=top5MN, top5H=top5H, top5HN=top5HN)

@app.route("/alumnos")
def alumnos():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM jugadores")
        jugadores = cur.fetchall()

    con.close()
    return render_template('alumnos.html', jugadores = jugadores, admin_Logeado = admin_Logeado)

@app.route("/eliminarJ", methods=['POST'])
def eliminarJ():
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            print(rowid)
            # Connect to the database and DELETE a specific record based on rowid
            with get_db_connection() as con:
                    cur = con.cursor()
                    print("hola")
                    cur.execute("DELETE FROM jugadores WHERE id_jugador = ?", (rowid,))
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
            
            return alumnos()
        

@app.route("/editarJ", methods=['POST'])
def editarJ():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario HTML
        rowid = request.form['id']
        nombre = request.form['nombre']
        user = request.form['user']
        edad = request.form['edad']
        sexo = request.form['sexo']
        
        try:
            with get_db_connection() as con:
                cur = con.cursor()
                # Realizar la actualización en la tabla 'menu'
                cur.execute("UPDATE jugadores SET nombre = ?, user_name = ?, edad = ?, sexo = ? WHERE id_jugador = ?", (nombre, user, edad, sexo, rowid))
                con.commit()
                msg = "Registro actualizado correctamente"
        except Exception as e:
            print(str(e))
            msg = "Error al actualizar el registro"
            return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401

        
        # Redireccionar o renderizar una plantilla con un mensaje de éxito
        return alumnos()

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/agregar")
def agregar():
    return render_template('AgregarPlayer.html', admin_Logeado = admin_Logeado)

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
                if not admin_Logeado:  # Verifica si admin_Logeado está vacío
                    admin_Logeado.append(administrador)

                

                            
        except Exception as e:    
            con.rollback()
            msg = "Error in the INSERT"
            print(e)  # Imprimir la excepción para depuración

        finally:        
            con.close() 
            if administrador:
                return IndexAdmin()
            else:
                return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401


@app.route("/agregarP", methods=['POST'])
def agregarP():
    con = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            print(nombre)
            numero = request.form['num']
            user = request.form['user']
            edad = request.form['edad']
            sexo = request.form['sexo']
            
            with get_db_connection() as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO jugadores (id_jugador, nombre, user_name, edad, sexo) VALUES (?, ?, ?, ?, ?)", (numero,nombre,user, edad, sexo))
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
        


@app.route("/nivel1T")
def nivel1T():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT j.id_jugador, j.user_name, n.puntaje_n AS puntaje_nivel1, n.tiempo_n ,n.acabado_n AS nivel1_acabado
            FROM jugadores j
            JOIN sesion s ON j.id_jugador = s.id_jugador
            JOIN nivel n ON s.id_sesion = n.id_sesion
            WHERE n.nombre = 'Nivel 1'
            ORDER BY j.id_jugador;
        """)
        datos = cur.fetchall()

    return render_template('nivel1T.html', admin_Logeado = admin_Logeado, nivel = datos)

@app.route("/nivel2T")
def nivel2T():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT j.id_jugador, j.user_name, n.puntaje_n AS puntaje_nivel1, n.tiempo_n ,n.acabado_n AS nivel1_acabado
            FROM jugadores j
            JOIN sesion s ON j.id_jugador = s.id_jugador
            JOIN nivel n ON s.id_sesion = n.id_sesion
            WHERE n.nombre = 'Nivel 2'
            ORDER BY j.id_jugador;
        """)
        datos = cur.fetchall()
    return render_template('nivel2T.html', admin_Logeado = admin_Logeado, nivel = datos)

@app.route("/nivel3T")
def nivel3T():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT j.id_jugador, j.user_name, n.puntaje_n AS puntaje_nivel1, n.tiempo_n ,n.acabado_n AS nivel1_acabado
            FROM jugadores j
            JOIN sesion s ON j.id_jugador = s.id_jugador
            JOIN nivel n ON s.id_sesion = n.id_sesion
            WHERE n.nombre = 'Nivel 3'
            ORDER BY j.id_jugador;
        """)
        datos = cur.fetchall()
    return render_template('nivel3T.html', admin_Logeado = admin_Logeado, nivel = datos)

@app.route("/sesionF")
def sesionF():
    return render_template('sesionF.html', admin_Logeado = admin_Logeado)

@app.route("/sesionT")
def sesionT():
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT j.id_jugador, j.user_name, s.puntaje, s.tiempo_juego, s.progreso
            FROM jugadores j
            JOIN sesion s ON j.id_jugador = s.id_jugador
            JOIN nivel n ON s.id_sesion = n.id_sesion
            ORDER BY j.id_jugador;
        """)
        datos = cur.fetchall()
    return render_template('sesionT.html', admin_Logeado = admin_Logeado, sesiones = datos)




if __name__== '__main__':
    app.run(debug=True)