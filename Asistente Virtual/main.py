import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro microfono y devolver el audio en texto
def transformar_audio_en_texto():
    # almacenar el reconocedor en una variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera para que se active el microfono
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # guardar lo que escuche
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar e imprimir el texto
            print("Dijiste " + pedido)

            # devolver pedido
            return pedido

        # En caso de que no reconozca el audio
        except sr.UnknownValueError:
            # Prueba de que no comprendió el audio
            print("Ups no entendí")

            # devolver error
            return "Sigo esperando"

        # En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendió el audio
            print("Ups no hay servicio")

            # devolver error
            return "Sigo esperando"

        # Error inesperado
        except:
            # Prueba de que no comprendió el audio
            print("Ups, algo salió mal.")

            # devolver error
            return "Sigo esperando"

# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)