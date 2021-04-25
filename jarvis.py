import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import pywhatkit
import random
from requests import get
import wikipedia
import webbrowser
# import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pytube
from pytube import YouTube
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI import Ui_Jarvis
###################################################################################################################



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


#################################################################################################################


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#####################################################################################################################

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am Jarvis. Any work for me ")

######################################################################################################################  
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajputvivo245@gmail.com', 'rajputana')
    server.sendmail('rajputvivo245@gmail.com', to, content)
    server.close()
 
###################################################################################################################### 
 

#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")





            
#######################################################################################################################



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()
        
    
########################################################################################################################
    def run(self):
             speak("Please say wakup to continue")
             
             while True:
                 self.query = self.takecommand()
                 if "activate" in self.query or "are you there" in self.query or "hello jarvis" in self.query or "om" in self.query:
                     self.TaskExecution()
                 else:
                     speak("who are You")

    #To convert voice into text
    def  takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 1
                audio = r.listen(source,timeout=5,phrase_time_limit=8)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")
                

        except Exception as e:
                speak("Say that again please...")
                return "none"
        query = query.lower()
        return query



############################################################################################################################
    


    
            
            
                
                
###############################################################################################################################
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()
            if "open notepad" in self.query:
                npath ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                os.startfile(npath)

        
            elif 'hi' in self.query or 'hello' in self.query:
                speak('Hello sir, how may I help you?')
            
            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()


            elif "play music" in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))



            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open instagram" in self.query:
                webbrowser.open("https://www.instagram.com/")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                
                webbrowser.open("www.google.com")

            elif "send Whatsapp message" in self.query:
                pywhatkit.sendwhatmsg("+916264383047", "this is testing protocol",21,36)
                speak("message has been sent")

            elif "song on youtube" in self.query:
                pywhatkit.playonyt("bella ciao instrumental")
                
            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = takeCommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')
             
            elif "email to avinash" in self.query:
                try:
                    speak("what should i say?")
                    content = takecommand()
                    to = "EMAIL OF THE OTHER PERSON"
                    sendEmail(to,content)
                    speak("Email has been sent to avinash")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to avi")
                    
                  

            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()
                


    #to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill {npath}")

    #to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22: 
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
    #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                       

            elif "tell me news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()

            #downlod you tube videos
            elif "download video" in self.query:
                speak("wait a minute")
                YouTube('').stream.first().download()


            
            
            
            speak("sir, do you have any other work")

#########################################################################################################################################

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Jarvis()
        self.ui.setupUi(self)
        print ("activate")
        
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/cf6951100506795c4fbb8dfccc28e460.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

########################################################################################################################
app = QApplication(sys.argv)
Jarvis = Main()
Jarvis.show()
exit(app.exec_())


        
