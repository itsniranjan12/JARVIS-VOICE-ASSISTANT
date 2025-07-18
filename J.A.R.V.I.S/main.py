import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI






recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="")
    response = client.responses.create(model="gpt-4.1",input=command) 
    speak(response.output_text)   

def processCommand(c):
    if (c.lower() == "open youtube"):
        webbrowser.open("https://www.youtube.com/")
    elif (c.lower() == "open google"):
        webbrowser.open("https://www.google.com/")
    elif (c.lower() == "open linkedin"):
        webbrowser.open("https://www.linkedin.com/feed/")
    elif (c.lower() == "open facebook"):
        webbrowser.open("https://www.facebook.com/")
    elif (c.lower() == "open instagram"):
        webbrowser.open("https://www.instagram.com/")
    elif (c.startswith("play")):
        song = c.lower().split(" ")[1]
        for key in musicLibrary.music.keys():
            if song in key:
                link = musicLibrary.music[key]
                webbrowser.open(link)
                break
    elif ("news" in c.lower()):
        r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2025-06-17&sortBy=publishedAt&apiKey=9e1a8b1d42754d81b758e37a0253d9bb')
        data = r.json()
        if "articles" in data:
            for article in data["articles"]:
                speak(article["title"])
    else:
        #let OpenAPI handle the rest.
        aiProcess(c)


                

    
    

        


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognising...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                word = r.recognize_google(audio)
                if (word.lower() == "jarvis"):
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
            print(f"Error {e}")                

