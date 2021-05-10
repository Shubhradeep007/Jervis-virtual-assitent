import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import json
import requests
import tracestack
import pyjokes




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning sir! A greate day waiting for you")

    elif hour>=12 and hour<=18:
        speak("Good afternoon Sir! hope your day was going good") 
        
    else: 
        speak("Good Evening Sir! so i hope your day was good")   
        
    speak("I am JaRVIS, How may I help you!")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listninig...")
        # r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again....") 
        return "None"   
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            speak("Anything More")    
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")
            speak("Anything More")    
            

            

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
            speak("Anything More")    
        

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stackoverflow")
            speak("Anything More")        
        
        elif 'play music' in query:
            music_dir = 'D:\\Music\\audio'
            songs = os.listdir(music_dir)
            speak("Playing music")       
            os.startfile(os.path.join(music_dir, songs[0]))
                    

                
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
            speak("Anything more sir")

        elif 'thank you' in query:
            speak("Your welcome, I am happy to help you")

        elif 'who are you' in query:
            speak("hi i am jarvis. I Am your virtual assistent") 

        elif 'who created you' in query:
            speak("i am created by Shubhradeep bose. thank you for creating me")

                   

        elif 'open chrome' in query:
            cpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            speak("anything more")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif 'joke' in query or 'one more' in query:
            speak(pyjokes.get_joke())        

        elif 'do not try' in query:
            speak("Yaaa i know it quite wired but have lots of more")     
        
        elif 'exit' in query or 'shutdown' in query or 'shut down' in query:
            speak("Thanks for giving me your time, I hope you like my service")
            exit()       

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to IZZON. further It's a secret")    

        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "use your own app key from openwheather website"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "your city"
            complete_url = base_url + "q=" + city_name + "&appid=" + api_key
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                k = current_temperature - 273.15
                T = round(k)
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature = " +str(T)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
                if str(weather_description) == "clear sky" and str(T)>="30":
                    speak("Temperature =" +str(T)+ "degree celsius outdoor is too sunny you should stay at home otherwise you get a suns stroke")
                elif str(weather_description) == "few clouds" and str(T)>="30":
                    speak("Temperature =" +str(T)+"degree celsius outdoor is sunny but it have some clouds" )
                else:
                    speak("Temperature =" +str(T)+"degree celsius") 
                #you can chose diffrent weather digree and type to speak differently        

             
            else:
                speak(" City Not Found ")    

        



