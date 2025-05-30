import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import os
import wikipedia
import pywhatkit 
import user_config






engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice

engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)

engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    content = " "
    while content == " ":
        
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content=r.recognize_google(audio,language='en-in')
           
            print("you said............." + content)
        except Exception as e:
            print("Please try again")
        #speak("hellow sandipan")
    return content 



def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome,how can i help you")
        elif"play music" in request:
            speak("playing music")
            song=random.randint(1,3)
            if song ==1:
                webbrowser.open("https://www.youtube.com/watch?v=K4DyBUG242c&list=RDQMTgh66LaGkb4&start_radio=1&ab_channel=NoCopyrightSounds")
            elif song==2:
                webbrowser.open("https://www.youtube.com/watch?v=5u6QMA56q5Q&ab_channel=MountassirSabir")
            elif song==3:
                webbrowser.open("https://www.youtube.com/watch?v=QgHtzmr1kQk&ab_channel=Monolink-Topic")
        elif "say time" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("Current time is" + str(now_time))
        elif "say date" in request:
            now_time=datetime.datetime.now().strftime("%d:%m")
            speak("Current date is" + str(now_time))
        elif "new task" in request:
            task=request.replace("new task","")
            task=task.strip()
            if task !="":
                speak("Adding task :" + task)
                with open("todo.txt","a") as file:
                    file.write(task+"\n")
        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("Work we have to do today is :" + file.read())

        elif "clear task" in request:
            open("todo.txt", "w").close()
            speak("All tasks have been cleared.")
        
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks =file.read()
            notification.notify(
                title="today's task",
                message=tasks
            )
        #open any apps that can open from web browser(add any item)
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        #open laptop devise
        elif "open" in request:
            quary=request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(quary)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "take screenshot" in request or "screenshot" in request:
            speak("Taking screenshot")
            screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
            pyautogui.screenshot(screenshot_path)
            speak("Screenshot taken and saved as screenshot.png")
        #take from wikipedia
        elif "wikipedia" in request:
            request=request.replace("jarvis","")
            request=request.replace("search wikipedia","")
            
            result= wikipedia.summary(request, sentences=2)
            
            speak(result)
        #take from google
        elif "search google" in request:
            request=request.replace("jarvis","")
            request=request.replace("search google","")
            webbrowser.open("https://www.google.com/search?q="+request)
        #for send message   
        elif "send whatsapp" in request:
            pywhatkit.sendwhatmsg("+919339020435", "Hi,how are you brother", 1, 22,30)
            
       
        elif "exit" in request or "quit" in request:
            speak("Goodbye!")
            break


        elif "send email" in request:
            pywhatkit.send_mail("sandipan116@gmail.com", user_config.gmail_password, "hello", "hello,how are you","sandipan9212@gmail.com" )
            speak("send email")
        
        # elif "send email" in request:
            
        #     pywhatkit.send_mail("sandipanjana9212@gmail.com",user_config.gmail_password,"hello","how are you","sandipanjana116@gmail.com")
        #     s=smtplib.SMTP('smtp.gmail.com',587)
        #     s.starttls()
        #     s.login("sandipanjana116@gmail.com",user_config.gmail_password)
        #     message="""this is sandipan jana.how are you"""
        #     s.sendmail("sandipanjana116@gmail.com","sandipanjana9212@gmail.com",message)
        #     s.quit()

main_process() 

