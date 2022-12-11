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

        query = 'SELECT nombres, apellidos, correo FROM apirest_usuario WHERE dni::integer = '

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