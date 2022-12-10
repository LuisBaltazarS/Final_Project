# Configuraciones / Tokens
from config import *
# TeleBot
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
# Utils
# import json
import os
import errno
from pathlib import Path
import datetime
import pandas as pd

# Instanciando bot
bot = telebot.TeleBot(ALERTB_TOKEN)

# Variable para almacenar las respuestas:
respuestas = {}

# Comandos para el bot
# /start - comando inicial.
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Hola! Me da gusto verte aquí!\n\nTal y como pudiste leer en mi descripción, soy un bot con el que puedes contar si deseas hablar acerca de como te sientes en tu institución educativa.\nMis creadores están trabajando en mejores respuestas para cuando desees conversar, pero por ahora me gustaría que respondas algunas preguntas😊\n\nPodemos empezar cuando gustes, solo da clic en el comando /conversar y estaré a tu servicio^^")

# /conversar - inicia la conversación preguntando el nombre de usuario del estudiante.
@bot.message_handler(commands=['conversar'])
def cmd_conversar(message):
    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "Primero que nada me gustaría saber el nombre de usuario con el que te encuentras registrado en nuestro <a href='https://www.google.com/'>sitio web</a>", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta1)

def act_pregunta1(message):
    # nombre de usuario
    user_name = message.text
    # agregar nombre de usuario al diccionario
    respuestas['nombre'] = user_name

    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, f"Bien <b>{user_name}</b>, ahora me gustaría que me cuentes algo\n\n¿Cómo te has sentido últimamente en tu institución educativa?", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta2)

def act_pregunta2(message):
    # resultado de pregunta 1
    res_preg1 = message.text
    # guardar resultado
    respuestas[pregunta1] = res_preg1

    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "¿Y qué me puedes contar acerca de tus compañeros de clase o de otros salones?", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta3)

def act_pregunta3(message):
    # resultado pregunta 2
    res_preg2 = message.text
    # guardar resultado
    respuestas[pregunta2] = res_preg2

    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ahora podemos pasar a los profesores ¿Son ellos buenos contigo? Si alguna vez observaste o sufriste un caso de acoso escolar ¿ellos actuaron adecuadamente? déjame saber que piensas respecto a eso.", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta4)

def act_pregunta4(message):
    # resultado pregunta 3
    res_preg3 = message.text
    # guardar resultado
    respuestas[pregunta3] = res_preg3

    markup = ForceReply()
    msg = bot.send_message(
        message.chat.id, "¿Qué hay del resto del personal de tu institución? por ejemplo los directores, personal de seguridad o limpieza ¿cómo te sientes con ellos?", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta5)

def act_pregunta5(message):
    # resultado pregunta 4
    res_preg4 = message.text
    # guardar resultado
    respuestas[pregunta4] = res_preg4

    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Anotado, ahora me gustaría preguntarte acerca de algo muy importante: ¿Cómo te sientes contigo mismo/a? olvídate de tus compañeros, profesores y el resto del personal. Solo quisiera saber acerca de ti y cómo te sientes", parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, act_pregunta6)

def act_pregunta6(message):
    # resultado pregunta 5
    res_preg5 = message.text
    # guardar resultado
    respuestas[pregunta5] = res_preg5

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
    respuestas[pregunta6] = res_preg6

    bot.send_message(message.chat.id, "Listo! Hemos acabado, estaremos registrando tus respuestas. Muchas gracias por tu tiempo 🌸, si tu tutor lo ve conveniente se estará contactando contigo pronto.")

    # data
    username = (str(respuestas['nombre']))
    now = datetime.datetime.now()
    time = (str(now.strftime('%m%d%Y%H%M%S')))
    filename = username + "_" + time

    # imprime en consola las respuestas obtenidos como diccionario
    print("\n",respuestas,"\n")

    # transforma el diccionario a csv
    df = pd.DataFrame([respuestas])

    ## exporta el csv
    dirname = os.path.dirname(__file__)
    path = Path(dirname+'/outputreports/'+username+'/')
    path.mkdir(parents=True, exist_ok=True)

    df.to_csv(dirname+'/outputreports/'+username+'/'+filename+'.csv', index=False, sep=',', encoding='utf-8')

    respuestas.clear()

# incialización del bot
if __name__ == '__main__':
    print("Alert-B está en ejecución! 🍀")
    bot.infinity_polling()