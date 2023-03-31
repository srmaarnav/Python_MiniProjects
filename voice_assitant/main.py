import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer() 
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def initialize(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    initialize('Welcome to your Assistant. How may I help you?')
    try:
        with sr.Microphone() as source:
            print("Listening for voice")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')        
    except:
        pass
    
    return command

def run_assistant():
    command = take_command()
    # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        initialize('Playing')
        print('Playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command: 
        time = datetime.datetime.now().strftime('%I:%M %p')  #%H:%M 
        initialize('Current time is ' + time)
        
    elif 'search about' or 'who is ' in command:
        person = command.replace('search about', '')
        info = wikipedia.summary(person, 1)
        initialize(info)
        print(info)
        
    elif 'made you' in command:
        speak = 'I have been created by my creator.'
        initialize(speak)
        
    elif 'are you' or 'introduce yourself' in command:
        speak = 'Hello, I am your personal assistant. I am here to make your life easier. You can use me to play any video on Youtube, find out the time, opening other applications, calculating sum as well.'
        initialize(speak)
    
    # elif 'close yourself' or 'end' in command:
    #     exit
        
    else:
        initialize('Please say the command again.')
        
while True:        
    run_assistant()
