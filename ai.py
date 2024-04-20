import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import webbrowser
import time

import pygame
pygame.init()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.say("hi. how can i help you today")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def rozpoznani_reci():
    with sr.Microphone() as source:
        print("poslouchám...")
        audio = recognizer.listen(source)
    try:
        hlas = recognizer.recognize_google(audio)
        print(hlas)
        return hlas
    except sr.UnknownValueError:
        print("Nerozpoznáno")
    except sr.RequestError as e:
        print("Chyba při komunikaci s Google Speech Recognition service;{0}".format(e))
        return ""

def run_jarvis():
    command = rozpoznani_reci()

    if 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'exit' in command:
        talk('goodbye')
        exit()

    elif 'play' in command:
        song = command.replace('play', "")
        talk(f'playing{song}')
        pywhatkit.playonyt(song)

    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.write(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('opening' + command)

    elif 'close' in command:
        pyautogui.hotkey('alt', 'f4')
        talk("closing sir")

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'remember that' in command:
        rememberMessage = command.replace('remember that', '')
        talk('you told me to remember that', + rememberMessage)
        remember = open('remember.txt' , "a")
        remember.write(rememberMessage)
        remember.close()

    elif 'what do yo remember' in command:
        remember = open('remember.txt' , "r")
        print(remember)
        talk("you told me to remember" + remember.read())

    elif 'clear remember file' in command:
        file = open('remember.txt' , "w")
        file.write(f"")
        talk("done sir, everything that i remember is deleted")

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(f"current time is: {time}")

    elif 'shutdown' in command:
        talk("shuting down the pc in")
        talk("3. 2. 1.")
        os.system("shutdown /s /t 1")

    elif 'restart' in command:
        talk("restarting the pc in")
        talk("3. 2. 1.")
        os.system("shutdown /r /t 1")

    elif 'search' in command:
        usercm = command.replace("search" , "")
        usercm = usercm.lower()
        webbrowser = open(f"{usercm}")
        talk("that is what i found on the internet")

    elif 'pause' in command or 'start' in command:
        pyautogui.press("k")
        talk("done sir!")

    elif 'full screen' in command:
        pyautogui.press("f")
        talk("done sir!")

    elif 'theather screen' in command:
        pyautogui.press("t")
        talk("done sir!")

    elif 'write' in command:
        command = command.replace("write" , "")
        pyautogui.write(command)
        talk("done sir!")

    elif 'terrorist' in command:
        number = command.replace("terrorist" , "")
        talk("starting terorist in")
        talk("3. 2. 1. ")
        pocet = int(number)
        for i in range(pocet):
            pyautogui.write("tohle se posila automaticky. neodpovidej. Zkousim program.")
            pygame.time.delay(250)
            pyautogui.press('enter')

    elif 'find' in command:
        command = command.replace('find', '')
        pyautogui.press('super')
        pyautogui.sleep(1)
        pyautogui.write("Microsoft Edge")
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        pyautogui.write(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')

        talk('opening' + command)

    else:
        print("Nastala chyba")
        talk("Nastala chyba")


while True:
    run_jarvis()