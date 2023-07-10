#Importing all necessary modules 
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[2].id)
print(voices[2].id)

#Defining speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hii, I am Swati, please tell me how may i help you")


def takeCommand():
    #It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

        


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en - in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query


    #Creating a function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com', to , content)
    server.close()





if __name__ == "__main__":
    wishMe()
    while True:
        #if 1:
          query = takeCommand().lower() #converting user query into lower case
          #logic for executing tasks based on query
          if 'wikipedia' in query:
              speak("Searching Wikipedia...")
              query = query.replace("Wikipedia", "")
              results = wikipedia.summary(query, sentences =2)
              speak("According to Wikipedia")
              print(results)
              speak(results)

          elif 'open youtube' in query:
              webbrowser.open("youtube.com")


          elif 'open google' in query:
              webbrowser.open("google.com")

          elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


          elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

          elif 'email to shubham' in query:
             try:
             
                  speak("what should i say?")
                  content = takeCommand()
                  to = "my email id"
                  sendEmail(to, content)
                  speak("email has been sent")

             except Exception as e:
                 print(e)
                 speak("Sorry Shubham, I am not able to send this email")

          elif 'open instagram ' in query:
              webbrowser.open("instagram.com")


              

             



            

        











          

              


         
            


    
