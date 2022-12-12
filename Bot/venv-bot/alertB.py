# Configuraciones / Tokens
from config import *
# TeleBot
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
# Utils
import os
import errno
from pathlib import Path
from datetime import datetime, timezone
import pytz
import pandas as pd
from dbhelper import *
from report_to_PDF import rep_to_pdf

# Instanciando bot
bot = telebot.TeleBot(ALERTB_TOKEN)

# Variable para almacenar las respuestas:
respuestas = {}

# Comandos para el bot
# /start - comando inicial.
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Hola! Me da gusto verte aquí!\n\nTal y como pudiste leer en mi descripción, soy un bot con el que puedes contar si deseas hablar acerca de como te sientes en tu institución educativa.\nMis creadores están trabajando en mejores respuestas para cuando desees conversar, pero por ahora me gustaría que respondas algunas preguntas😊\n\nPodemos empezar cuando gustes, solo da clic en el comando /conversar y estaré a tu servicio^^")

# /help - comando de ayuda
@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id, 'Veo que necesitas algo de ayuda. No te preocupes! Aquí están todos los comandos que puedes ejecutar conmigo:\n\n<b>/conversar</b> - Con este comando puedes informarme sobre como te sientes en tu institución educativa, es decir, relaciones con tus compañeros de clase o profesores.',parse_mode='html')

# /conversar - inicia la conversación preguntando el nombre de usuario del estudiante.
@bot.message_handler(commands=['conversar'])
def cmd_conversar(message):
    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "Primero que nada me gustaría saber tu DNI con el que te encuentras registrado en nuestro <a href='https://www.google.com/'>sitio web</a>", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta1)

def act_pregunta1(message):
    # comprobar si el usuario realmente ingresó un dato válido
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "Hey, yo no creo que eso sea tu DNI 🤨\nIngresa tu DNI por favor:")
        bot.register_next_step_handler(msg, act_pregunta1)
    else:
        # verificar si el dni ingresado existe en la bd
        input = str(message.text)
        datos = auth_estudiante(dni=input)

        if datos is None:
            markup = ForceReply()
            msg = bot.send_message(message.chat.id, "Este DNI no corresponde a ningún usuario, verifica que esté correctamente escrito 😓")
            bot.register_next_step_handler(msg, act_pregunta1)
        else:
            # agregar nombre de usuario al diccionario
            idEstudiante = datos[0]
            nombres = datos[1]
            apellidos = datos[2]
            correo = datos[3]

            respuestas['idEstudiante'] = idEstudiante
            respuestas['nombres'] = nombres
            respuestas['apellidos'] = apellidos
            respuestas['correo'] = correo
            respuestas['telegram_user'] = "@"+str(message.chat.username)
            markup = ForceReply()
            msg = bot.send_message(
                message.chat.id, f"Bien <b>{nombres}</b> un gusto tenerte aquí! Ahora me gustaría que me cuentes algo\n\n¿Cómo te has sentido últimamente en tu institución educativa?", parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(msg, act_pregunta2)

def act_pregunta2(message):
    # resultado de pregunta 1
    res_preg1 = message.text
    # guardar resultado
    respuestas['pregunta1'] = res_preg1

    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "¿Y qué me puedes contar acerca de tus compañeros de clase o de otros salones?", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta3)

def act_pregunta3(message):
    # resultado pregunta 2
    res_preg2 = message.text
    # guardar resultado
    respuestas['pregunta2'] = res_preg2

    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ahora podemos pasar a los profesores ¿Son ellos buenos contigo? Si alguna vez observaste o sufriste un caso de acoso escolar ¿ellos actuaron adecuadamente? déjame saber que piensas respecto a eso.", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta4)

def act_pregunta4(message):
    # resultado pregunta 3
    res_preg3 = message.text
    # guardar resultado
    respuestas['pregunta3'] = res_preg3

    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "¿Qué hay del resto del personal de tu institución? por ejemplo los directores, personal de seguridad o limpieza ¿cómo te sientes con ellos?", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta5)

def act_pregunta5(message):
    # resultado pregunta 4
    res_preg4 = message.text
    # guardar resultado
    respuestas['pregunta4'] = res_preg4

    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Anotado, ahora me gustaría preguntarte acerca de algo muy importante: ¿Cómo te sientes contigo mismo/a? olvídate de tus compañeros, profesores y el resto del personal. Solo quisiera saber acerca de ti y cómo te sientes", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta6)

def act_pregunta6(message):
    # resultado pregunta 5
    res_preg5 = message.text
    # guardar resultado
    respuestas['pregunta5'] = res_preg5

    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Bien, ya estamos por terminar!\n\nDado que ya respondiste todas las preguntas, lo último que queda es si deseas comentarme algo. Puede ser respecto a esta pequeña sesión o algo que quizás no pudo ser respondido con las preguntas anteriores.\nClaro, si no deseas comentar nada, puedes escribir <b>NO</b>", parse_mode='html', reply_markup=markup)

    if msg.text.lower() == 'no':
        bot.register_next_step_handler(msg, act_final)
    else:
        bot.register_next_step_handler(msg, act_final)

def act_final(message):
    # resultado pregunta 6
    res_preg6 = message.text
    # guardar resultado
    respuestas['pregunta6'] = res_preg6

    bot.send_message(message.chat.id, "Listo! Hemos acabado. Muchas gracias por tu tiempo 🌸 registraré y enviaré tus respuestas al tutor de tu institución, si lo ve conveniente se estará contactando contigo pronto.")

    # data
    idEstudiante = respuestas['idEstudiante']
    estudiante = (str(respuestas['nombres'])).replace(' ','')
    dt = datetime.now(timezone.utc)
    now_bot = dt.strftime('%y-%m-%d %H:%M:%S.%f%z')
    time = (str(dt.strftime('%m%d%Y%H%M%S')))
    filename = estudiante + "_" + time + '.csv'

    # imprime en consola las respuestas obtenidos como diccionario
    print("Diccionario: \n\n",respuestas,"\n")

    # transforma el diccionario a csv
    df = pd.DataFrame([respuestas])

    ## exporta el csv
    dirname = os.path.dirname(__file__)
    path = Path(dirname+'/outputreports/'+estudiante+'/')
    path.mkdir(parents=True, exist_ok=True)

    df.to_csv(dirname+'/outputreports/'+estudiante+'/'+filename, index=False, sep=',', encoding='utf-8')

    insert_report(filename, now_bot , 'En atención', idEstudiante)

    respuestas.clear()

# Filtro de comandos que no existen.
@bot.message_handler(content_types=['text'])
def bot_unknown_commands(message):
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Lo siento no te entendí 😔\nEjecuta /help si quieres saber que comandos puedo ejecutar.')

# incialización del bot
if __name__ == '__main__':
    print("Alert-B está en ejecución! 🍀")
    bot.infinity_polling()