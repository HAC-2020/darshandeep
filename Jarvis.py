import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour>12:
       speak("Good Evening! Darshan")

       speak("I am Jarvis Sir. Please tell me how may I Help You")

   elif hour>=12 and hour<18:
       speak("Good Afternoon! Darshan")

       speak("I am Jarvis Sir. Please tell me how may I Help You")

   else:
      speak("Good Morning! Darshan")


      speak("I am Jarvis Sir. Please tell me how may I Help You")   

def takeCommand():
    #It take microphone input from the user and return string Output
     
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir...") 
        r.pause_threshold = 1  
        audio = r.listen(soure)

    try:
        print("Recognizing Sir...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 


    except Exception as e:
       # print(e)


        print("Say it again Please Sir....") 
        return "None"          

if __name__ == "__main__":
    wishMe()
