import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json 
import openai
from bs4 import BeautifulSoup
openai.api_key ="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"


 
engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am Jarvis boss.  please tell me how may i can help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said: {query} \n")


    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()




if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music = 'D:\\music\\Best Nepali'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[10]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.exe"
            os.startfile(codePath)

        elif 'close'  in query:
            speak("Quiting jarvis, have a goodday    bye bye")
            exit()

        elif 'Artificial intelligence' in query:
             gpt3_response = get_gpt3_response(query)
             speak(gpt3_response)  # Speak the GPT-3 generated response

        
        elif 'temperature' in query:
            search = "temperature in Itahari"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"curent {search} is {temp}")

         
           