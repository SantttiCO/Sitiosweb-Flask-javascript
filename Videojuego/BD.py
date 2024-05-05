import sqlite3, json

conexion = sqlite3.connect("videojuego.db")
cursor = conexion.cursor()

def createadmin():
    cursor.execute("""
    CREATE TABLE administrador(
            id_admin INTEGER primary key, 
            nombre varchar(30), 
            correo  varchar(50), 
            contraseña varchar(10)
                   );
                   """)



def createjugador():
    cursor.execute("""
        CREATE TABLE jugadores(
            id_jugador INT primary key, 
            nombre varchar(30), 
            user_name varchar(30),
            edad INT, 
            sexo bool
                   
    );
    """)

def createsesion():
    cursor.execute("""
    CREATE TABLE sesion (
        id_sesion INTEGER PRIMARY KEY,
        id_jugador INTEGER,
        tiempo_juego INTEGER,
        puntaje INTEGER,
        progreso INTEGER,

        FOREIGN KEY (id_jugador) REFERENCES jugadores (id_jugador)
    );
    """)


def createnivel():
    cursor.execute("""
    CREATE TABLE nivel (
        id_nivel INTEGER PRIMARY KEY,
        id_sesion INTEGER,
        puntaje_n INTEGER,
        acabado_n INTEGER,
        nombre varchar(20),
        tiempo_n INTEGER,

        
        FOREIGN KEY (id_sesion) REFERENCES sesion (id_sesion)
    );
    """)

def createlog():
    cursor.execute("""
    CREATE TABLE log (
        id_log INTEGER PRIMARY KEY,
        descripcion TEXT,
        id_sesion INTEGER,
        FOREIGN KEY (id_sesion) REFERENCES sesion (id_sesion)
    );
    """)

def createpreguntas():
    cursor.execute("""
    CREATE TABLE preguntas (
        id_preguntas INTEGER PRIMARY KEY,
        texto TEXT,
        id_nivel INTEGER,
        FOREIGN KEY (id_nivel) REFERENCES nivel (id_nivel)
    );
    """)

createadmin()
createjugador()
createsesion()
createnivel()
createlog()
#createpreguntas()

conexion.commit()

def insert_jugadores():
    jugadores = [
        
        (100, 'prueba', 'pruebita', 100, 0)

    ]
    cursor.executemany("INSERT INTO jugadores VALUES (?, ?, ?, ?, ?)", jugadores)
    conexion.commit()

def insert_sesion():
    sesiones = [
        
        (100, 100, 0, 0, 0)

    ]
    cursor.executemany("INSERT INTO sesion VALUES (?, ?, ?, ?, ?)", sesiones)
    conexion.commit()

def insert_nivel():
    niveles = [
    
    (100, 100, 0, 0, 'Nivel 0', 0)

    ]
    cursor.executemany("INSERT INTO nivel VALUES (?, ?, ?, ?, ?, ?)", niveles)
    conexion.commit()



def insert_preguntas():
    preguntas = [
        (1, '¿Cuál es la capital de Francia?', 1),
        (2, '¿Cuál es el río más largo del mundo?', 2),
        (3, '¿En qué año comenzó la Segunda Guerra Mundial?', 3),
        (4, '¿Cuál es el océano más grande del mundo?', 4),
        (5, '¿Quién escribió "Don Quijote de la Mancha"?', 5)
    ]
    cursor.executemany("INSERT INTO preguntas VALUES (?, ?, ?)", preguntas)
    conexion.commit()

def insertar_administradores():
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin1", "admin1@example.com", "contraseña1"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin2", "admin2@example.com", "contraseña2"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin3", "admin3@example.com", "contraseña3"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin4", "admin4@example.com", "contraseña4"))
    cursor.execute("INSERT INTO administrador (nombre, correo, contraseña) VALUES (?, ?, ?)", ("Admin5", "admin5@example.com", "contraseña5"))
    conexion.commit()

def cannon():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS CannonLevel(id_question INTEGER primary key, pregunta varchar(300), respuesta_a varchar(100),"
        "respuesta_b varchar(100), respuesta_c varchar(100), correct_answer int(1))")

# el valor de correct se le restara -1 con el fin de tener el indice para saber que cañon no va a disparar
def tobogan():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ToboganLevel(id_question INTEGER primary key, pregunta varchar(300), respuesta_a varchar(100),"
        "respuesta_b varchar(100), respuesta_c varchar(100), correct_answer int(1))")

def formas():
    cursor.execute("""
    CREATE TABLE FormasLevel (
        id_question INTEGER PRIMARY KEY,
        pregunta varchar(100),
        matriz TEXT,
        tipo INTEGER
    );
    """)




def insertar_cannon():
    preguntas = [
        (1, "¿Cuánto es 2 + 2?", "4", "3", "5", 1),
        (2, "¿Cuánto es 3 x 1?", "1", "3", "2", 2),
        (3, "¿Cuánto es 5 + 3?", "6", "9", "8", 3),
        (4, "¿Cuánto es 6 x 2?", "12", "11", "10", 1),
        (5, "¿Cuánto es 7 + 1?", "6", "8", "9", 2),
        (6, "¿Cuánto es 8 x 1?", "7", "9", "8", 3),
        (7, "¿Cuánto es 1 + 9?", "10", "11", "8", 1),
        (8, "¿Cuánto es 2 x 5?", "9", "10", "11", 2),
        (9, "¿Cuánto es 4 + 4?", "7", "9", "8", 3),
        (10, "¿Cuánto es 3 x 3?", "9", "8", "10", 1),
        (11, "¿Cuánto es 5 + 2?", "6", "7", "8", 2),
        (12, "¿Cuánto es 4 x 2?", "9", "8", "7", 3),
        (13, "¿Cuánto es 6 + 1?", "7", "6", "8", 1),
        (14, "¿Cuánto es 3 x 4?", "12", "11", "13", 1),
        (15, "¿Cuánto es 7 + 3?", "10", "11", "9", 1),
        (16, "¿Cuánto es 2 x 6?", "11", "12", "13", 2),
        (17, "¿Cuánto es 8 + 2?", "10", "9", "11", 1),
        (18, "¿Cuánto es 5 x 2?", "11", "9", "10", 3),
        (19, "¿Cuánto es 9 + 1?", "10", "11", "9", 1),
        (20, "¿Cuánto es 4 x 3?", "13", "12", "11", 2),
        (21, "¿Cuánto es 3 + 3?", "7", "5", "6", 3),
        (22, "¿Cuánto es 6 x 2?", "12", "13", "11", 1),
        (23, "¿Cuánto es 5 + 4?", "8", "9", "10", 2),
        (24, "¿Cuánto es 2 x 7?", "14", "13", "15", 3),
        (25, "¿Cuánto es 6 + 3?", "9", "10", "8", 1),
        (26, "¿Cuánto es 3 x 5?", "14", "15", "16", 2),
        (27, "¿Cuánto es 7 + 2?", "8", "10", "9", 3),
        (28, "¿Cuánto es 4 x 4?", "16", "15", "17", 1),
        (29, "¿Cuánto es 8 + 1?", "10", "9", "8", 2),
        (30, "¿Cuánto es 5 x 3?", "14", "16", "15", 3),
        (31, "¿Cuánto es 9 + 0?", "9", "10", "8", 1),
        (32, "¿Cuánto es 2 x 8?", "15", "16", "17", 2),
        (33, "¿Cuánto es 6 + 4?", "11", "9", "10", 3),
        (34, "¿Cuánto es 7 x 2?", "14", "13", "15", 1),
        (35, "¿Cuánto es 8 + 3?", "10", "11", "12", 2),
        (36, "¿Cuánto es 9 x 2?", "17", "19", "18", 3),
        (37, "¿Cuánto es 1 + 9?", "10", "11", "9", 1),
        (38, "¿Cuánto es 2 x 9?", "17", "18", "19", 2),
        (39, "¿Cuánto es 7 + 4?", "13", "10", "11", 3),
        (40, "¿Cuánto es 3 x 6?", "18", "17", "19", 1)
    ]

    cursor.executemany("""
            INSERT INTO CannonLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, preguntas)




def insertar_tobogan():

    #aqui van las preguntas
    cursor.execute("INSERT INTO ToboganLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (1,"PreguntaPrueba 1", "a) respuesta 1a)", "b) respuesta b)", "c) ambas", 3 ))
    # el valor de correct se le restara -1 con el fin de tener el indice para saber que cañon no va a disparar

    cursor.execute("INSERT INTO ToboganLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (2,"PreguntaPrueba 2", "a) respuesta 2a)", "b) respuesta b)", "c) ambas", 1 ))


    cursor.execute("INSERT INTO ToboganLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (3,"Pregunta 3", "a) respuesta 3a)", "b) respuesta b)", "c) ambas", 2 ))
    conexion.commit()

def insertar_formas():
    arreglo_2d = [
    [False, True, True, True, True, True, True, False],
    [False, True, True, True, True, True, True, False],
    [False, True, True, True, True, True, True, False],
    [False, True, True, True, True, True, True, False],
    [False, True, True, True, True, True, True, False],
    [False, True, True, True, True, True, True, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d1 = [
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]]


    arreglo_2d2 = [
    [False, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]]


    arreglo_2d3 = [

    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True]]



    arreglo_2d4 = [
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False], 
    [False, False, False, False, False, False, False, False]]




    arreglo_2d5 = [
    [False, False, True, True, True, False, False, False],
    [False, False, True, True, True, False, False, False],
    [False, False, True, True, True, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]]



    arreglo_2d6 = [
    [True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True]]


    arreglo_2d7 = [
    [False, True, True, True, True, True, False, False],
    [False, True, False, False, False, True, False, False],
    [False, True, False, False, False, True, False, False],
    [False, True, False, False, False, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]]

    arreglo_2d8 = [
    [False, False, True, True, True, False, False, False],
    [False, False, True, False, True, False, False, False],
    [False, False, True, True, True, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]]

    arreglo_2d9 = [
    [True, True, True, True, True, True, True, False],
    [True, False, False, False, False, False, True, False],
    [True, False, False, False, False, False, True, False],
    [True, False, False, False, False, False, True, False],
    [True, False, False, False, False, False, True, False],
    [True, False, False, False, False, False, True, False],
    [True, True, True, True, True, True, True, False], 
    [False, False, False, False, False, False, False, False]]


    arreglo_2d10 = [
    [False, True, True, True, True, True, True, False],
    [False, True, False, False, False, False, True, False],
    [False, True, True, True, True, True, True, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]
    ]

    arreglo_2d11 = [
    [True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True], 
    [False, False, False, False, False, False, False, False]

    ]
    
    arreglo_2d12 = [
    [False, False, True, True, True, True, False, False],
    [False, False, True, False, False, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d13 = [
    [True, True, True, True, True, True, True, False],
    [True, False, False, False, False, False, True, False],
    [True, False, False, False, False, False, True, False],
    [True, True, True, True, True, True, True, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d14 = [
    [False, True, True, True, True, True, True, False],
    [False, True, False, False, False, False, True, False],
    [False, True, False, False, False, False, True, False],
    [False, True, True, True, True, True, True, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d15 = [
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d16 = [
    [False, False, True, True, True, True, False, False],
    [False, False, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]
    ]
    arreglo_2d17 = [
    [False, True, True, True, True, True, False, False],
    [False, True, True, True, True, True, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d18 = [
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d19 = [
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False]

    ]
    arreglo_2d20 = [
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [False, False, False, False, False, False, False, False]

    ]
    
    arreglo_1d = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False]

    arreglo_1d1 = [ 
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True]


    arreglo_1d2 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False]

    arreglo_1d3 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False]

    arreglo_1d4 = [
    False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d5 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d6 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d7 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d8 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d9 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d10 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False]

    arreglo_1d11 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False]

    arreglo_1d12 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False]

    arreglo_1d13 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False]

    arreglo_1d14 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False]







    arreglo_1d15 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False]


    arreglo_1d16 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False]

    arreglo_1d17 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True,True, True, True, True, True, True, True, True, True, True, False, False, False, True, True,True, True, True, True, True, True, True, True, True, True, True, False, True, True, True,True, True, True, True, True, True, True, True, True, True, True, True]

    arreglo_1d18 = [
    False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False]

    arreglo_1d19 = [
    False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]


    arreglo_json = json.dumps(arreglo_2d)
    arreglo_json1 = json.dumps(arreglo_2d1)
    arreglo_json2 = json.dumps(arreglo_2d2)
    arreglo_json3 = json.dumps(arreglo_2d3)
    arreglo_json4 = json.dumps(arreglo_2d4)
    arreglo_json5 = json.dumps(arreglo_2d5)
    arreglo_json6 = json.dumps(arreglo_2d6)
    arreglo_json7 = json.dumps(arreglo_2d7)
    arreglo_json8 = json.dumps(arreglo_2d8)
    arreglo_json9 = json.dumps(arreglo_2d9)

    arreglo_json10 = json.dumps(arreglo_2d10)
    arreglo_json11 = json.dumps(arreglo_2d11)
    arreglo_json12 = json.dumps(arreglo_2d12)
    arreglo_json13 = json.dumps(arreglo_2d13)
    arreglo_json14 = json.dumps(arreglo_2d14)
    arreglo_json15 = json.dumps(arreglo_2d15)
    arreglo_json16 = json.dumps(arreglo_2d16)
    arreglo_json17 = json.dumps(arreglo_2d17)
    arreglo_json18 = json.dumps(arreglo_2d18)
    arreglo_json19 = json.dumps(arreglo_2d19)
    arreglo_json20 = json.dumps(arreglo_2d20)
    arreglo_json21 = json.dumps(arreglo_1d)
    arreglo_json22 = json.dumps(arreglo_1d1)
    arreglo_json23 = json.dumps(arreglo_1d2)
    arreglo_json24 = json.dumps(arreglo_1d3)
    arreglo_json25 = json.dumps(arreglo_1d4)
    arreglo_json26 = json.dumps(arreglo_1d5)
    arreglo_json27 = json.dumps(arreglo_1d6)
    arreglo_json28 = json.dumps(arreglo_1d7)
    arreglo_json29 = json.dumps(arreglo_1d8)
    arreglo_json30 = json.dumps(arreglo_1d9)
    arreglo_json31 = json.dumps(arreglo_1d10)
    arreglo_json32 = json.dumps(arreglo_1d11)
    arreglo_json33 = json.dumps(arreglo_1d12)
    arreglo_json34 = json.dumps(arreglo_1d13)
    arreglo_json35 = json.dumps(arreglo_1d14)
    arreglo_json36 = json.dumps(arreglo_1d15)
    arreglo_json37 = json.dumps(arreglo_1d16)
    arreglo_json38 = json.dumps(arreglo_1d17)
    arreglo_json39 = json.dumps(arreglo_1d18)
    arreglo_json40 = json.dumps(arreglo_1d19)
    



    


    formas = [
        
        (1,"Dibuja un cuadrado con un área de 36",arreglo_json, 2),
        (2,"Dibuja un cuadrado con un área de 16",arreglo_json1, 2),
        (3,"Dibuja un cuadrado con un área de 25",arreglo_json2, 2),
        (4,"Dibuja un cuadrado con un área de 64",arreglo_json3, 2),
        (5,"Dibuja un cuadrado con un área de 49",arreglo_json4, 2),
        (6,"Dibuja un cuadrado con un área de 9",arreglo_json5, 2),
        (7,"Dibuja un cuadrado con un perímetro de 32",arreglo_json6, 2),
        (8,"Dibuja un cuadrado con un perímetro de 20",arreglo_json7, 2),
        (9,"Dibuja un cuadrado con un perímetro de 12",arreglo_json8, 2),
        (10,"Dibuja un cuadrado con un perímetro de 28",arreglo_json9, 2),
        (11, "Dibuja un rectángulo con un perímetro de 18 con un lado de 3", arreglo_json10, 2),
        (12, "Dibuja un rectángulo con un perímetro de 30 con un lado de 8", arreglo_json11, 2),
        (13, "Dibuja un rectángulo con un perímetro de 14  con un lado de 4", arreglo_json12, 2),
        (14, "Dibuja un rectángulo con un perímetro de 22 con un lado de 7", arreglo_json13, 2),
        (15, "Dibuja un rectángulo con un perímetro de 20 con un lado de 6", arreglo_json14, 2),
        (16, "Dibuja un rectángulo con un área de 12 con un lado de 3", arreglo_json15, 2),
        (17, "Dibuja un rectángulo con un área de 8 con un lado de 4", arreglo_json16, 2),
        (18, "Dibuja un rectángulo con un área de 10 con un lado de 2", arreglo_json17, 2),
        (19, "Dibuja un rectángulo con un área de 48 con un lado de 8", arreglo_json18, 2),
        (20, "Dibuja un rectángulo con un área de 28 con un lado de 4", arreglo_json19, 2),
        (21, "Dibuja un rectángulo con un área de 56 con un lado de 7", arreglo_json20, 2),

        (22, "Dibuja un triángulo equilátero que ocupe un área de 8", arreglo_json21, 1),
        (23, "Dibuja un triángulo equilátero cuyo perímetro sea de 21 con un lado", arreglo_json22, 1),
        (24, "Dibuja un triángulo equilátero con un área de 18", arreglo_json23, 1),
        (25, "Dibuja un triángulo equilátero cuyo perímetro sea de 15", arreglo_json24, 1),
        (26, "Dibuja un triángulo equilátero con área de 32", arreglo_json25, 1),
        (27, "Dibuja un trapecio con perímetro de 22 con base mayor de 8", arreglo_json26, 1),
        (28, "Dibuja un trapecio con perímetro de 22 con base menor de 4", arreglo_json27, 1),
        (29, "Dibuja un trapecio con área de 30", arreglo_json28, 1),
        (30, "Dibuja un trapecio con área de 26", arreglo_json29, 1),
        (31, "Dibuja un trapecio con perímetro de 21 con una base mayor de 8", arreglo_json30, 1),
        (32, "Dibuja un hexágono con perímetro de 18", arreglo_json31, 1),
        (33, "Dibuja un hexágono con área de 22.5 con apotema de 2.5", arreglo_json32, 1),
        (34, "Dibuja un hexágono con área de 22.5 con lado de 6", arreglo_json33, 1),
        (35, "Dibuja un hexágono con un perímetro de 24", arreglo_json34, 1),
        (36, "Dibuja un hexágono con un área de 42 con apotema de 3.5", arreglo_json35, 1),

        (37, "Dibuja un prisma hexagonal con un área de la base de 22.5", arreglo_json36, 3),
        (38, "Dibuja un prisma triangular con un volumen de 36", arreglo_json37, 3),
        (39, "Dibuja un prisma trapezoidal con un área de la base de 30", arreglo_json38, 3),
        (40, "Dibuja un prisma hexagonal con un volumen de 84", arreglo_json39, 3),
        (41, "Dibuja un prisma triangular con un área de la base de 35", arreglo_json40, 3)


        


    ]
    cursor.executemany("INSERT INTO FormasLevel VALUES (?, ?, ?, ?)", formas)
    conexion.commit()


def tobogan():
    cursor.execute(
        "CREATE TABLE ToboganesLevel(id_question INTEGER primary key, pregunta varchar(300), respuesta_a varchar(100), respuesta_b varchar(100), respuesta_c varchar(100), correct_answer int(1))")

def insertar_tobogan():

    #aqui van las preguntas
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (1,"¿Cuántos lados tiene un hexágono?", "6", "8", "9", 1 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (2,"Fórmula para calcular el área de un círculo", "2πr", "πr*r", "πd", 2 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (3,"Fórmula para calcular el perímetro de un cuadrado", "2L", "4L", "LxL", 2 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (4,"¿Cuántos lados tiene un decágono?", "8", "10", "12", 2 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (5,"¿Cuántos vértices tiene un cubo?", "4", "6", "8", 3 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (6,"Figura geométrica con al menos un ángulo recto", "Rectangulo", "Pentagono", "Octagono", 1 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (7,"¿Cuántos lados tiene un octágono?", "5", "7", "8", 3 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (8,"Medida de un ángulo interior de un pentágono", "108", "90", "120", 1 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (9,"¿Cuántos lados tiene un cuadrilátero convexo?", "3", "5", "4", 3 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (10,"Triángulo con tres ángulos agudos", "Obtusangulo", "Acutangulo", "Escaleno", 2 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (11,"Fórmula para el área de un triángulo escaleno", "(BxA)/2", "(BxA)/3", "(BxA)/4", 1 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (12,"¿Cuántos lados tiene un enéagono?", "9", "10", "11", 1 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (13,"¿Cuántos vértices tiene un heptágono?", "9", "13", "7", 3 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (14,"¿Cuántos lados tiene un trapezoide?", "5", "6", "4", 3 ))
    cursor.execute("INSERT INTO ToboganesLevel (id_question, pregunta, respuesta_a, respuesta_b, respuesta_c, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
                   (15,"Medida de un ángulo interior de un hexágono", "120", "150", "180", 1 ))
  

tobogan()
insertar_tobogan()


cannon()
insertar_cannon()


formas()
insertar_formas()

insert_jugadores()
insert_sesion()
insert_nivel()
#insert_log()
#insert_preguntas()
insertar_administradores()

# Cerrar la conexión con la base de datos cuando hayas terminado
conexion.close()


