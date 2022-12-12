import psycopg2
from config import config

def auth_estudiante(dni):
    conexion = None
    try:
        params = config(archivo='database.ini', seccion='postgresql')
        print(params)

        print('Conectando a la base de datos PostgreSQL...\n')
        conexion = psycopg2.connect(**params)

        cur = conexion.cursor()

        query = 'SELECT id, nombres, apellidos, correo FROM apirest_usuario WHERE dni::integer = '

        cur.execute(query + str(dni))
        res = cur.fetchone()

        # nombres = res[0]

        print('Resultado: ',res,'.')
        print('El tipo de resultado obtenido es: ',type(res))

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexion finalizada')
    
    return res

def insert_report(fileName, fecha_emitido, estado, id_usuario_id):
    conexion = None
    try:
        params = config(archivo='database.ini', seccion='postgresql')
        print(params)

        print('Conectando a la base de datos PostgreSQL...\n')
        conexion = psycopg2.connect(**params)

        conexion.autocommit = True

        cur = conexion.cursor()

        query = 'INSERT INTO apirest_reporte (filename, fecha_emitido, estado, id_usuario_id) values(%s, %s, %s, %s);'
        data = (fileName, fecha_emitido, estado, id_usuario_id)

        print(data)

        cur.execute(query, data)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.commit()
            conexion.close()
            print('Conexion finalizada')