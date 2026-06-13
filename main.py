# 

import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl
import openai_request as gpt




engine = pyttsx3.init()
voices = engine.getProperty('voices')    
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 150)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = ""
    while content == "":

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10)

            content = r.recognize_google(audio, language='en-in')
            print("You Said............" + content)
            return content

        except sr.WaitTimeoutError:
            
            print("Say something")
            speak("Say something")

            try:
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=20)

                content = r.recognize_google(audio, language='en-in')
                print("You Said............" + content)
                return content

            except sr.WaitTimeoutError:
                print("Second timeout")
                speak("No input detected. Session terminated.")
                return "terminate"

        except Exception:
            print("Please try again...")
            continue

    
def main_process():

    speak("Hi, I am Hannah. How can I help you today?")

    while True:
        request = command().lower()

        if request == "terminate":
            break
        
        elif "ok stop" in request:
            speak("Bye Bye")
            break

        elif "hello" in request:
            speak("Hi, How can i help you.")

        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=6KKs0QGGe-0&t=242s")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=6KKs0QGGe-0&t=242s")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=6KKs0QGGe-0&t=242s")
        
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_time))

        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task : " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt", "r") as file:
                speak("Work we have to do today is : " + file.read())            

        elif "show work" in request:
            with open("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            )

        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in request:
            webbrowser.open("www.instagram.com")  

        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

            im1 = pyautogui.screenshot()
            im1.save('my_screenshot.png')
            im2 = pyautogui.screenshot('my_screenshot2.png')

        elif "wikipedia" in request:
            request = request.replace("Hannah", "")
            request = request.replace("search wikipedia", "")
            result = wikipedia.summary(request, sentences = 2)
            speak(result)        

        elif "search google" in request:
            request = request.replace("Hannah", "")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q="+request)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+91xxxx2", "Hi, How are you?", 2, 37, 20, True, 2)



        elif "send email" in request:

            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()

                s.login(
                    "medhavee.gemini@gmail.com",
                    user_config.gmail_pass
)

                message = (
                    "Subject: Greeting\n\n"
                    "Hi, Hope you are doing well!\n"
                    "This is a test email sent by Hannah.\n"
                    "Thanks"
                )

                s.sendmail(
                    "medhavee.gemini@gmail.com",
                    "medscodes@gmail.com",
                    message
                )

                s.quit()
                print("Email sent")

            except Exception as e:
                print("Email failed:", e)
      

        # elif "ask gpt" in request:
        #     request = request.replace("Hannah", "")
        #     request = request.replace("ask gpt", "")
        #     print("Request to GPT: " + request)
        #     response = gpt.ask_gpt(request)
        #     print("GPT Response: " + response)
        #     speak(response)

        # else ask ai in request:
        #     request = request.replace("Hannah", "")
        #     request = request.replace("ask ai", "")
        #     print("Request to GPT: " + request)
        #     response = gpt.ask_gpt(request)
        #     print("GPT Response: " + response)
        #     speak(response)



main_process()
