import pyttsx3
import speech_recognition as sr
import pywhatkit
import time
import datetime
import wikipedia
from wikipedia import *
import datetime
import webbrowser
import requests
from wolfram import App
import wolframalpha
import subprocess
import pyjokes
import os
from requests import get
import random
import cv2
import pywhatkit as kit
from datetime import date
from gtts import gTTS
import subprocess
#all external file impliement here..

#engine is start for speak.. 
engine = pyttsx3.init()

# #voice control setting here....
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 180)
engine.say("initializing engine")
# #  0 for male voice & 1 for female voice



def meena():
    
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 180)
    engine.say('I am Meena. thank you for selecting me....')
    engine.say("Now i Am ready for your work")
    engine.runAndWait()
    
def jarvis():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say('I am Jarvis. thank you for selecting me....')
    engine.say("Now i Am ready for your work")
    engine.runAndWait()

#listener for listening ..
def take_command():
    listener = sr.Recognizer()
    try:
     with sr.Microphone() as source:
        print('listening.....!')
        listener.pause_threshold=5
        voice = listener.listen(source,timeout=50,phrase_time_limit=5)
        print('Recongnizing...')
     
        command = listener.recognize_google(voice,language='en-IN')
        print("user said :", command)

    except: 
        pass    
    return command

# #def fun() for actual speaking function
def talk(x):
    engine.say(x)   
    engine.runAndWait()

#wish function
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        talk('good morning')
    elif hour>=12 and hour<=18:
        talk('good afternoon')
    else: 
        talk('Good evening..')

#user name
def username():
    talk("What should i call you sir")
    uname = take_command()
    talk("Welcome Mister")
    talk(uname)
    print("#####################")
    print("Welcome Mr.", uname)
    print("#####################")
     
    talk("How can i Help you, Sir")

def Meena():
   
    assname =("Meena 1 point o")
    talk("mee meena")
    print(assname)
    talk(assname)


# wish()

# talk("I am your Assistant")
# meena()
# username()
talk('what can i do for you sir..')


def movies():
    print("I have some movies in my database, here is a list")
    talk( "I have some movies in my database, here is a list")
    
    add="E:\Movies\Hollywood\movie category" 
    listsong=os.listdir(add)
    print(listsong)
    talk(listsong) 
    talk("which one do you like to play sir..")
    def moviename():
        command =take_command()
        print(command)
        
        if 'Marvel' in command:
                add1="E:\Movies\Hollywood\movie category\Marvel's all movie" 
                listmovie=os.listdir(add1)
                print("Avenger's End game playing...")
                talk("Avenger's End Game playing...")
                os.startfile(os.path.join(add1,listmovie[1]))
                time.sleep(15)   

        elif 'Harry Potter' in command:
                add1="E:\Movies\Hollywood\movie category\HARRY POTTER all movies" 
                listmovie=os.listdir(add1)
                print("HArry potter playing....")
                talk("Harry potter playing....")
                os.startfile(os.path.join(add1,listmovie[7]))
                time.sleep(15)
                
        elif "suggest" in command:
            talk(" According to me,  you have to watch Marvel movie. I recommanding you to watch Avenger's End Game . it is best movie in Marvel Comic. now goto marvel section and enjoy movie sir..")
            

        elif 'exit' in command:
            talk("we are exiting from movie list.., what can i do for you sir..")
            run=Run_meena()
                

    while True:
        moviename()     
    

def mob():
    while True:
     talk ("please tell me that person name")
     num = take_command()
     if 'Ragini' in num:
        talk(" searching on my Database number of")
        talk(num)
        WPNum="+917218971418"
        return WPNum
                         
     elif 'Ashwini' in num:
        talk(" searching on my Database number of")
        talk(num)
        WPNum="+917057145157"
        return WPNum
        
     elif 'Patil sir' in num:
            talk(" searching on my Database number of")
            talk(num)
            WPNum="+919823355660"
            return WPNum

     elif 'Dairya' in num:
            talk(" searching on my Database number of")
            talk(num)
            WPNum="+917057575876"
            return WPNum 

     elif 'Vikas' in num:
            talk(" searching on my Database number of")
            talk(num)
            WPNum="+919767338373"
            return WPNum  

     elif 'Utkarsha' in num or 'mam' in num :
            talk(" searching on my Database number of")
            talk(num)
            WPNum="+919039031821"
            return WPNum 

     elif 'information' in num :
            talk(" searching on my Database this Group ")
            talk(num)
            WPNum="La307llRVGQ0yLf3UnT3fD"
            return WPNum 
            
     else:
         talk("this number is not found in my database")

def msg():
 while True:
    talk (" now tell me the what is meassge..?")
    msgg=take_command()
    talk(" i am repeating your meassge..! ")
    talk(msgg)
    talk("tell me its correct or not")
    mes1=take_command()

    if 'yes' in mes1:
        talk("saved data")
        return msgg
    else:
        talk("repeating again")
       
def WPMSg():
 WPNum=mob()
 msgg=msg()
 talk("wait it is progress..")
 kit.sendwhatmsg_instantly(WPNum,msgg)
 talk("task complete")
 wait()
 wait()

def WPMSg2():
 WPNum=mob()
 msgg=msg()
 talk("wait it is progress..")
 hour1 = datetime.datetime.now().strftime('%H') 
 min1 = datetime.datetime.now().strftime('%M')
 print(min1)
 print(hour1)
 kit.sendwhatmsg_to_group(WPNum,msgg,hour1,min1)

 talk("task complete")

def wait():
    time.sleep(10)

def notepad(text):
    date=datetime.datetime.now()
    file_name= str(date).replace(":", "-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(text)

    subprocess.Popen(["C:\\Windows\\system32\\notepad.exe",file_name])

def Playmusic():
    print("I have some music in my database, here is a list")
    talk( "I have some music in my database, here is a list")
    
    add="G:\Music\MEENA PLaylist" 
    listsong=os.listdir(add)
    print(listsong)
    talk(listsong) 
    talk("which one do you like to play sir..")
    def Musiccate():
        command = take_command()
        print(command)
        
        if 'Marathi' in command:
                add1="E:\Movies\Hollywood\movie category\Marvel's all movie" 
                listmovie=os.listdir(add1)
                os.startfile(os.path.join(add1,listmovie[1]))
                time.sleep(15)
                
                

        elif 'Hindi' in command:
                add1="E:\Movies\Hollywood\movie category\HARRY POTTER all movies" 
                listmovie=os.listdir(add1)
                print("HArry potter playing....")
                talk("Harry potter playing....")
                os.startfile(os.path.join(add1,listmovie[7]))
                time.sleep(15)
                
        elif "English" in command:
                talk("English Playlist Playing....")
                add1="G:\Music\MEENA PLaylist\English Songs" 
                listsong=os.listdir(add1)
                os.startfile(os.path.join(add1,listsong[0]))
                time.sleep(8)
                talk("you can say Next and previous for song")

                i=0
                while True:
                    nxt =take_command()
            
                    if "stop" in nxt or "Stop" in nxt:
                        talk('okey sir, i am closing music')
                        os.system('taskkill /f /im AIMP.exe')
                        Run_meena()
                        
                    if "next" in nxt or "Next" in nxt:
                        i=i+1
                        add1="G:\Music\MEENA PLaylist\English Songs" 
                        listsong=os.listdir(add1)
                        os.startfile(os.path.join(add1,listsong[i]))
                        time.sleep(8)
                        
                  
                    if "previous" in nxt or "previous" in nxt:
                        
                        i=i-1
                        add1="G:\Music\MEENA PLaylist\English Songs" 
                        listsong=os.listdir(add1)
                        os.startfile(os.path.join(add1,listsong[i]))
                        time.sleep(8)
                        
                




                         

    while True:
        Musiccate()     
    
  
def Run_meena():
    #work / task declaring
    if __name__ == '__main__':
        while True:
        
            command = take_command()
            

            # time related tasks
            if 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p') 
             # indian time converter
                print(time)
                talk('current time is '+ time)


            elif 'date' in command:
                today=date.today()
                print(today)
                talk(today)
            
            #open apps task
            elif 'play YouTube' in command:
                talk("which song do you want to play on Youtube")
                song=take_command()
                # song=command.replace('play','')
                talk(' wait , its playing....'+ song)
                print('playing..' +song)
                kit.playonyt(song,use_api=True)
                wait()
                

            elif 'search' in command or 'find' in command:
                
                command = command.replace("search", "")
                command = command.replace("play", "")         
                webbrowser.open_new_tab(command )
                wait()
                
                
            elif 'open Google' in command:
            
                webbrowser.open_new_tab("https://www.google.com")
                talk("Google chrome is open now")
                wait()
                

                
            elif 'news' in command:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                talk('Here are some headlines from the Times of India,Happy reading')
                time.sleep(15)
                

            elif 'Wikipedia' in command or 'who is' in command or 'what is' in command:
                talk('Searching Wikipedia...')
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences = 2)
                talk("According to Wikipedia")
                print(results)
                talk(results)
                

            elif 'open stackoverflow' in command:
                talk("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")  
                wait()

            elif 'open camera' in command:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break

                cap.release()
                cv2.destroyAllWindows()

            elif 'open Notepad' in command:
                print("What would you like me to write down..?")
                talk("What would you like me to write down..?")
                note=take_command()
                print("I Am writing .....")
                talk("I Am writing .....")
                talk(note)
                print(note)
                notepad(note)
                talk("task complete...Result showing on your screen sir.....")
                
                
            
                
            #close apps task

            elif 'close Chrome' in command or 'close Google' in command:
                talk('okey sir, i am closing google')
                os.system('taskkill /f /im chrome.exe')

            elif 'close YouTube' in command or 'close YouTube' in command:
                talk('okey sir, i am closing Youtube')
                os.system('taskkill /f /im chrome.exe')

            elif 'close camera' in command:
                talk('okey sir, i am closing camera')
                

            elif 'close notepad' in command:
                talk('okey sir, i am closing Notepad')
                os.system('taskkill /f /im notepad.exe')

            elif 'close movie' in command:
                talk('okey sir, i am closing movie')
                os.system('taskkill /f /im VLC.exe')

            elif 'close music' in command:
                    talk('okey sir, i am closing music')
                    os.system('taskkill /f /im AIMP.exe')
                
                
                
    
            # Multimedia task
            
            elif "play music" in command:
               Playmusic()
            

            elif "play movie" in command:
                movies()
                
            #ask task
        

            elif 'ask mode' in command:
                talk('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=take_command()
                app_id="KQGPPX-2YJK83K5VR"
                client = wolframalpha.Client('KQGPPX-2YJK83K5VR')
                res = client.command(question)
                answer = next(res.results).text
                talk(answer)
                print(answer)

            elif "show me" in command:
                command = command.replace("where is", "")
                location = command
                talk("User asked to Locate")
                talk(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")
                wait()


            elif 'joke' in command:
                joke=(pyjokes.get_joke())
                print(joke)
                talk(joke)

            elif 'IP address' in command:
                ip=get('https://api.ipify.org').text
                print("your IP Address is" , ip)
                talk("your IP Address is")
                talk(ip)
                
            elif 'send message' in command or 'send a message on Whatsapp' in command:
                talk("this message is sending on personal number")
                WPMSg()
                
            elif 'send message on group' in command :
                talk("this message is sending on group")
                WPMSg2()
                    
            #Personal Task

            elif 'who I am' in command:
                talk('If you talk then definitely your human.')

            elif 'who are you' in command or "who you are" in command:
                print("I am Meena, version 1 point O your persoanl assistant. I am programmed to minor tasks like opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!")
                talk("I am  Meena,......Meena version 1 point O your persoanl assistant,....... I am programmed to minor tasks like          opening youtube   ,google chrome.....,gmail and stackoverflow.... ,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!")

            elif 'how are you' in command:
                talk("I am fine, Thank you")
                talk("How are you, Sir")
        
            elif 'fine' in command or "good" in command:
                talk("It's good to know that your fine")

            elif "thank you" in command:
                talk("Welcome Sir. now tell next task please")
                
        
            elif "change my name" in command:
                username()
        
            # elif "change name" in command:
               
        
            elif "what are you" in command or "what you are" in command:
                talk("We are voice Assistant. we perfrom task which you tells us.")
                print("We are voice Assistant. we perfrom task which you tells us.")
                
            
            elif 'exit' in command:
                talk("Thanks for giving me your time")
                exit()
            
            elif 'call Jarvis' in command:
                jarvis()
                
            elif 'wait' in command or "Wait" in command:
                time.sleep(20)
                talk("i Am waiting please tell me task")
                

            elif 'call Meena' in  command or "call Mina" in command:
                meena()
            else:
                talk('please say again. i didnt recognize what you said..!')

Run_meena()