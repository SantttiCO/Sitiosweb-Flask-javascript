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
            WHERE nombre = 'Nivel de Tobogan'
        """)
        topNivel1 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Tobogan' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Tobogan'
        );
        """)
        topNivel1Players = cur.fetchall()
        
        #nivel2
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Cañon'
        """)
        topNivel2 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Cañon' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Cañon'
        );
        """)
        topNivel2Players = cur.fetchall()

        #nivel3
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Figuras'
        """)
        topNivel3 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Figuras' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Figuras'
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
            WHERE nombre = 'Nivel de Tobogan'
        """)
        topNivel1 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Tobogan' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Tobogan'
        );
        """)
        topNivel1Players = cur.fetchall()
        
        #nivel2
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Cañon'
        """)
        topNivel2 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Cañon' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Cañon'
        );
        """)
        topNivel2Players = cur.fetchall()

        #nivel3
        cur.execute("""
        SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Figuras'
        """)
        topNivel3 = cur.fetchall()

        cur.execute("""
        SELECT j.user_name
        FROM nivel n
        JOIN sesion s ON n.id_sesion = s.id_sesion
        JOIN jugadores j ON s.id_jugador = j.id_jugador
        WHERE n.nombre = 'Nivel de Figuras' AND n.puntaje_n = (
            SELECT MAX(puntaje_n)
            FROM nivel
            WHERE nombre = 'Nivel de Figuras'
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
            WHERE n.nombre = 'Nivel de Tobogan'
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
            WHERE n.nombre = 'Nivel de Cañon'
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
            WHERE n.nombre = 'Nivel de Figuras'
            ORDER BY j.id_jugador;
        """)
        datos = cur.fetchall()
    return render_template('nivel3T.html', admin_Logeado = admin_Logeado, nivel = datos)



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


@app.route('/loginGame', methods=['POST'])
def loginGame():
    numero_de_lista = request.form.get('numero_de_lista')
    username = request.form.get('username')

    conexion = sqlite3.connect("videojuego.db")
    try:
        cursor = conexion.cursor()

        # Verificar si el usuario existe en la tabla de jugadores
        cursor.execute(
            "SELECT * FROM jugadores WHERE id_jugador = ? AND user_name = ?",
            (numero_de_lista, username)
        )
        usuario = cursor.fetchone()

        # Si el usuario no existe, no permitimos el login
        if usuario is None:
            return jsonify({"message": "Usuario no registrado", "status": "fail"}), 401

        # Verificar si ya existe una sesión para ese número de lista
        cursor.execute(
            "SELECT * FROM Sesion WHERE id_jugador = ?",
            (numero_de_lista,)
        )
        sesion_existente = cursor.fetchone()

        # Si ya existe una sesión, no se hace nada
        if sesion_existente:
            return jsonify({"message": "Sesión ya existente", "status": "succes 2"}), 201

        # Si no existe una sesión, se crea una nueva
        cursor.execute(
            "INSERT INTO Sesion(id_sesion, id_jugador, tiempo_juego, puntaje, progreso) VALUES (?, ?, 0, 0, 0)",
            (numero_de_lista, numero_de_lista)  # Asumimos que el id de sesión e id del jugador son el mismo
        )

        # Guardar los cambios en la base de datos
        conexion.commit()
        return jsonify({"message": "Sesión iniciada exitosamente", "status": "success"}), 200

    except sqlite3.Error as e:
        print(f"Ocurrió un error: {e}")
        return jsonify({"message": "Error en la base de datos", "status": "error"}), 500
    finally:
        # Cerrar la conexión a la base de datos
        conexion.close()



@app.route('/update_score', methods=['POST'])
def update_score():
    numero_de_lista = request.form.get('numero_de_lista')
    nuevo_puntaje = request.form.get('puntaje')
    nivel = request.form.get('name_level')
    timer = request.form.get('global_timer')

    try:
        numero_de_lista = int(numero_de_lista)  # Asegurarse de que es un entero
        nuevo_puntaje = int(nuevo_puntaje)  # Asegurarse de que es un entero
        timer = int(timer)

        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()

        # Obtener el puntaje actual del jugador en la sesión
        cursor.execute("SELECT puntaje FROM Sesion WHERE id_sesion = ?", (numero_de_lista,))
        fila = cursor.fetchone()

        if fila:
            puntaje_actual = fila[0]
            puntaje_total = puntaje_actual + nuevo_puntaje  # Sumar el nuevo puntaje al actual
            # Actualizar el puntaje del jugador con el nuevo total
            cursor.execute("UPDATE Sesion SET puntaje = ?, tiempo_juego = ? WHERE id_sesion = ?", (puntaje_total, timer, numero_de_lista))

            # Verificar si existe una entrada en la tabla nivel para el nivel y id_sesion específicos
            cursor.execute("SELECT puntaje_n FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
            fila_nivel = cursor.fetchone()

            if fila_nivel:
                # Actualizar la entrada existente
                cursor.execute("UPDATE nivel SET puntaje_n = ?, tiempo_n = ? WHERE id_sesion = ? AND nombre = ?", (nuevo_puntaje, timer, numero_de_lista, nivel))

            else:
                # Crear una nueva entrada
                cursor.execute("INSERT INTO nivel (nombre, puntaje_n, id_sesion,tiempo_n) VALUES (?, ?, ?,?)", (nivel, nuevo_puntaje, numero_de_lista, timer))
        else:
            return jsonify({"message": "Jugador no encontrado", "status": "fail"}), 404

        conexion.commit()
        return jsonify({"message": "Puntaje actualizado exitosamente", "status": "success"}), 200

    except ValueError:
        return jsonify({"message": "Input inválido, se esperaban números", "status": "fail"}), 400
    except sqlite3.Error as e:
        return jsonify({"message": f"Error en la base de datos: {e}", "status": "fail"}), 500

    finally:
        conexion.close()




@app.route('/create', methods=['POST'])
def create_user():
    received_value = request.form['score']
    print(f"Valor recibido: {received_value}")
    return jsonify({"value": received_value}), 200



@app.route('/update_tobogan_score', methods=['POST'])
def update_score_tobogan():
    numero_de_lista = request.form.get('numero_de_lista')
    puntaje = request.form.get('puntaje')

    # Convertir los valores a los tipos de datos correctos, si es necesario
    numero_de_lista = int(numero_de_lista)  # Convertir a entero si es necesario
    puntaje = int(puntaje)  # Convertir a entero si es necesario

    # Conexión a la base de datos
    conexion = sqlite3.connect("videojuego.db")
    cursor = conexion.cursor()

    # Comprobar si el alumno ya existe en la base de datos
    cursor.execute("SELECT * FROM AlumnosLogin WHERE num_lista = ?", (numero_de_lista,))
    if cursor.fetchone():
        # Si el alumno existe, actualiza su puntaje de cannon
        cursor.execute("UPDATE AlumnosLogin SET score_tobogan = ? WHERE num_lista = ?", (puntaje, numero_de_lista))
    else:
        # Si el alumno no existe, inserta una nueva fila con su puntaje
        cursor.execute("INSERT INTO AlumnosLogin (num_lista, score_tobogan) VALUES (?, ?)", (numero_de_lista, puntaje))

    # Guarda los cambios y cierra la conexión
    conexion.commit()
    conexion.close()

    return jsonify({"message": "Puntaje actualizado o creado", "status": "success"}), 200





@app.route('/prueba', methods=['GET'])
def prueba():
    return "se actualizo "





@app.route("/Cannon_question", methods=['POST', 'GET'])
def preguntas_cannon():
    try:
        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer FROM CannonLevel ORDER BY RANDOM() LIMIT 1")
            question_data = cur.fetchone()
            if question_data:
                return jsonify({
                    'pregunta': question_data[0],
                    'respuesta_a': question_data[1],
                    'respuesta_b': question_data[2],
                    'respuesta_c': question_data[3],
                    'correct_answer': question_data[4]
                    
                })
            else:
                return jsonify({'error': 'No hay pregunta disponible'}), 404
    except Exception as e:
        return jsonify({'error': 'Server Error: ' + str(e)}), 500

@app.route("/Tobogan_question", methods=['POST', 'GET'])
def preguntas_tobogan():
    try:
        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer FROM ToboganesLevel ORDER BY RANDOM() LIMIT 1")
            question_data = cur.fetchone()
            if question_data:
                return jsonify({
                    'pregunta': question_data[0],
                    'respuesta_a': question_data[1],
                    'respuesta_b': question_data[2],
                    'respuesta_c': question_data[3],
                    'correct_answer': question_data[4]
                })
            else:
                return jsonify({'error': 'No hay pregunta disponible'}), 404
    except Exception as e:
        return jsonify({'error': 'Server Error: ' + str(e)}), 500


@app.route('/get_cannon_level_score', methods=['POST'])
def get_cannon_level_score():
    numero_de_lista = request.form.get('numero_de_lista')
    nombre_nivel = "Nivel de Cañon"
    try:
        numero_de_lista = int(numero_de_lista)
        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT puntaje_n FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nombre_nivel))
        puntaje = cursor.fetchone()
        if puntaje:
            return jsonify({"puntaje": puntaje[0], "nombre_nivel": nombre_nivel}), 200
        else:
            return jsonify({"puntaje": 0, "nombre_nivel": nombre_nivel}), 200
    except ValueError:
        return jsonify({"error": "Input inválido"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

@app.route('/get_tobogan_level_score', methods=['POST'])
def get_tobogan_level_score():
    numero_de_lista = request.form.get('numero_de_lista')
    nombre_nivel = "Nivel de Tobogan"
    try:
        numero_de_lista = int(numero_de_lista)
        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT puntaje_n FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nombre_nivel))
        puntaje = cursor.fetchone()
        if puntaje:
            return jsonify({"puntaje": puntaje[0], "nombre_nivel": nombre_nivel}), 200
        else:
            return jsonify({"puntaje": 0, "nombre_nivel": nombre_nivel}), 200
    except ValueError:
        return jsonify({"error": "Input inválido"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

@app.route('/get_figuras_level_score', methods=['POST'])
def get_figuras_level_score():
    numero_de_lista = request.form.get('numero_de_lista')
    nombre_nivel = "Nivel de Figuras"
    try:
        numero_de_lista = int(numero_de_lista)
        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT puntaje_n FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nombre_nivel))
        puntaje = cursor.fetchone()
        if puntaje:
            return jsonify({"puntaje": puntaje[0], "nombre_nivel": nombre_nivel}), 200
        else:
            return jsonify({"puntaje": 0, "nombre_nivel": nombre_nivel}), 200
    except ValueError:
        return jsonify({"error": "Input inválido"}), 400
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()


@app.route('/get_player_score', methods=['POST'])
def get_player_score():
    id_jugador = request.form.get('id_jugador')
    try:
        # Convertir id_jugador a entero para asegurar validez
        id_jugador = int(id_jugador)

        # Conexión a la base de datos
        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()

        # Ejecutar consulta para obtener el puntaje del jugador especificado
        cursor.execute("SELECT puntaje FROM sesion WHERE id_jugador = ?", (id_jugador,))
        puntaje = cursor.fetchone()

        if puntaje:
            # Si se encuentra el puntaje, devolverlo
            return jsonify({"puntaje": puntaje[0]}), 200
        else:
            # Si no se encuentra el puntaje, devolver 0 como valor predeterminado
            return jsonify({"puntaje": 0}), 200
    except ValueError:
        # Manejo de error si id_jugador no es un número
        return jsonify({"error": "Input inválido, se esperaba un número"}), 400
    except sqlite3.Error as e:
        # Manejo de errores relacionados con la base de datos
        return jsonify({"error": "Error en la base de datos: " + str(e)}), 500
    finally:
        # Cerrar siempre la conexión a la base de datos
        conexion.close()


@app.route("/Formas_question", methods=['GET'])
def Formas_question():
    try:
        with get_db_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT pregunta, matriz, tipo FROM FormasLevel")
            question_data = cur.fetchall()

            # Wrap the list of questions in a "preguntas" property
            response_json = {"preguntas": []}

            if question_data:
                for pregunta in question_data:
                    response_json["preguntas"].append({
                        'pregunta': pregunta[0],
                        'matriz': pregunta[1],
                        'tipo': pregunta[2]
                    })
            else:
                return jsonify({'error': 'No hay pregunta disponible'}), 404

            return jsonify(response_json), 200  # Return the entire response_json

    except Exception as e:
        return jsonify({'error': 'Server Error: ' + str(e)}), 500




@app.route('/finish_level', methods=['POST'])
def finish_level():
    numero_de_lista = request.form.get('numero_de_lista')
    nivel = request.form.get('name_level')

    try:
        numero_de_lista = int(numero_de_lista)  # Convertir a entero

        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()

        # Verificar si existe una entrada en la tabla nivel para el nivel y número de lista específicos
        cursor.execute("SELECT * FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
        fila_nivel = cursor.fetchone()

        if fila_nivel:
            # Actualizar la entrada existente
            cursor.execute("SELECT progreso FROM sesion WHERE id_sesion = ?", (numero_de_lista,))
            fila_progreso = cursor.fetchone()
            if fila_progreso:
                fila_progreso=fila_progreso[0]+1
                cursor.execute("UPDATE nivel SET acabado_n = 1 WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
                cursor.execute("UPDATE sesion SET progreso = fila_progreso WHERE id_sesion = ? ", (numero_de_lista))

            else:
                fila_progreso=1
                cursor.execute("UPDATE nivel SET acabado_n = 1 WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
                cursor.execute("UPDATE sesion SET progreso = fila_progreso WHERE id_sesion = ? ", (numero_de_lista))

        else:
            # Crear una nueva entrada
            cursor.execute("INSERT INTO nivel (nombre, acabado_n, id_sesion) VALUES (?, 1, ?)", (nivel, numero_de_lista))

        conexion.commit()
        return jsonify({"message": "Operación realizada correctamente", "status": "success"}), 200

    except ValueError:
        return jsonify({"message": "Input inválido, se esperaban números", "status": "fail"}), 400
    except sqlite3.Error as e:
        return jsonify({"message": f"Error en la base de datos: {e}", "status": "fail"}), 500

    finally:
        conexion.close()


@app.route('/unfinish_level', methods=['POST'])
def unfinish_level():
    numero_de_lista = request.form.get('numero_de_lista')
    nivel = request.form.get('name_level')

    try:
        numero_de_lista = int(numero_de_lista)  # Convertir a entero

        conexion = sqlite3.connect("videojuego.db")
        cursor = conexion.cursor()

        # Verificar si existe una entrada en la tabla nivel para el nivel y número de lista específicos
        cursor.execute("SELECT * FROM nivel WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
        fila_nivel = cursor.fetchone()

        if fila_nivel:
            # Actualizar la entrada existente
            cursor.execute("UPDATE nivel SET acabado_n = 0 WHERE id_sesion = ? AND nombre = ?", (numero_de_lista, nivel))
        else:
            # Crear una nueva entrada
            cursor.execute("INSERT INTO nivel (nombre, acabado_n, id_sesion) VALUES (?, 0, ?)", (nivel, numero_de_lista))

        conexion.commit()
        return jsonify({"message": "Operación realizada correctamente", "status": "success"}), 200

    except ValueError:
        return jsonify({"message": "Input inválido, se esperaban números", "status": "fail"}), 400
    except sqlite3.Error as e:
        return jsonify({"message": f"Error en la base de datos: {e}", "status": "fail"}), 500

    finally:
        conexion.close()



if __name__== '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)