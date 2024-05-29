import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyowm
import webbrowser
import time as ti
import requests
import pyautogui

wikipedia.set_lang('de')

def open_website(url):
    webbrowser.open_new_tab(url)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
owm = pyowm.OWM('1c99c4cab8b7cca5ff1561808164fdd7')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Ich höre zu...')
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio, language="de-DE")
            print(command)
            if 'Alexa' in command:
                return command
            else:
                return None
    except:
        return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    # Deine Anfrage an die OpenWeatherMap-API
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid={DEIN API KEY}'
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        # WetterAPI wenn sie mal Funktionieren würde AMK
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        return f"In {city} ist das Wetter {description}. Die Temperatur beträgt {temperature_celsius:.2f} Grad Celsius."
    else:
        return "Fehler beim Abrufen des Wetters."




# Hier passiert die ganze Magie

def alexa_starten():
    while True:
        befehl = take_command()
        if befehl:


            if 'Spiele das Lied' in befehl:
                song = befehl.replace('spiele das Lied', '')
                talk(song + 'Bitte sehr!')
                pywhatkit.playonyt(song)


            elif'stop' in befehl:
                pyautogui.press(" ")
            elif'aus' in befehl:
                pyautogui.hotkey('alt' , 'f4')
            elif 'wie spät ist es' in befehl:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Aktuelle Uhrzeit: ' + time)
            elif 'suche' in befehl:
                suchbegriff = befehl.replace('Alexa suche', '')
                info = wikipedia.summary(suchbegriff, sentences=10)
                talk(info)
            elif 'Suche' in befehl:
                suchbegriff = befehl.replace('Alexa Suche', '')
                info = wikipedia.summary(suchbegriff, sentences=10)
                talk(info)               
            elif 'Websuche' in befehl:
                suchbegriff = befehl.replace('Alexa Websuche', '')
                info = wikipedia.summary(suchbegriff, sentences=10)
                talk(info)
            elif 'erzähl mir einen Witz' in befehl:
                talk(pyjokes.get_joke())
            elif 'Wetter' in befehl:
                wetterbericht = get_weather('Berlin')
                talk(wetterbericht)
            elif 'Musik' in befehl:
                talk('Tech SVC Radio! Ich spiele es von Stream Laut FM. Der Assistent wird nun Beendet.')
                ti.sleep(0.1)
                open_website("https://stream.laut.fm/techsvc")
            elif 'wetter' in befehl:
                talk(wetterbericht)
            elif 'Computer' in befehl:
                talk('Computer sagt JA! ')
            elif 'ja oder nein' in befehl:
                talk('Computer sagt nö! ')
            elif 'tschüss' in befehl:
                talk('Auf Wiedersehen!')
                break

            elif 'beenden' in befehl:
                talk('Auf Wiedersehen!')
                break

            else:
                continue
        else:
            continue







# Supercooles Logo
print("""
 ____                       _                   _     _             _   
/ ___| _ __  _ __ __ _  ___| |__   __ _ ___ ___(_)___| |_ ___ _ __ | |_ 
\___ \| '_ \| '__/ _` |/ __| '_ \ / _` / __/ __| / __| __/ _ \ '_ \| __|
 ___) | |_) | | | (_| | (__| | | | (_| \__ \__ \ \__ \ ||  __/ | | | |_ 
|____/| .__/|_|  \__,_|\___|_| |_|\__,_|___/___/_|___/\__\___|_| |_|\__|
      |_|                                                               
                             Gecodet von Ruebel 
""")



# Das Herzstück des ganzen
alexa_starten()
