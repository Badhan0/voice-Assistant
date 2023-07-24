import pyttsx3
import datetime   
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",300)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
        speak("how may I help you?")
    elif hour>=12 and hour<19:
        speak("good afternoon!")
        speak("how may I help you?")
    else:
        speak("good evening!")
        speak("how may I help you?")
    

def takecommand(): 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print (f"You said: {query}\n")
    except Exception as e:
        # print (e)
        speak("Say that again please")
        print ("say that again please..")
        return "none"
    return query
if __name__ == "__main__":
    speak(" hello sir  ")
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching.....")
            query = query.replace("wikipedia","")
            try:
                results = wikipedia.summary(query,sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple pages with that name. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, there were no matching pages found for your query.")
        elif 'stop' in query or 'exit' in query:
            speak("Exiting the program.")
            break
        if 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/') 
        if 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open('https://web.whatsapp.com/')
        if 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open('https://stackoverflow.com/')
        if 'music from youtube' in query:
            speak("playing music from youtube")
            webbrowser.open('https://www.youtube.com/watch?v=YxWlaYCA8MU&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa&index=2')
        if 'gfg' in query or 'geek for geeks' in query:
            speak("opening gfg") 
            webbrowser.open('https://www.geeksforgeeks.org/')   
        if 'the time' in query:
            Time=datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir,its{Time}")
        if 'open vs code' in query or 'visual studio code' in query:
            codepath="C:\\Users\\MD.SAFIUR RAHAMAN\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening Visual studio code")
            os.startfile(codepath)
        if 'open Chrome' in query or 'google chrome' in query:
            chromepath="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            speak("opening Google chrome")
            os.startfile(chromepath)
        
        