# Token del bot de telegram
ALERTB_TOKEN = "5667543370:AAED847-MaCcr21sK_2N5xybgnbVxy-CO_4"

# preguntas
pregunta1 = "¿Cómo te has sentido últimamente en tu institución educativa?"
pregunta2 = "¿Y qué me puedes contar acerca de tus compañeros de clase o de otros salones?"
pregunta3 = "Ahora podemos pasar a los profesores ¿Son ellos buenos contigo? Si alguna vez observaste o sufriste un caso de acoso escolar ¿ellos actuaron adecuadamente?"
pregunta4 = "¿Qué hay del resto del personal de tu institución? por ejemplo los directores, personal de seguridad o limpieza ¿cómo te sientes con ellos?"
pregunta5 = "¿Cómo te sientes contigo mismo/a?"
pregunta6 = "Comentarios adicionales"

# database configurations
from configparser import ConfigParser

def config(archivo='database.ini', seccion='postgresql'):
    parser=ConfigParser()
    parser.read(archivo)

    db = {}
    if parser.has_section(seccion):
        params=parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
            print(db)
    else:
        raise Exception('Secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))

    return db