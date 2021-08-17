import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import ssl
import requests
import json
MASTER="ABHAY"
engine=pyttsx3.init("sapi5")
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

#speak function will pronous the string which is passes to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function wish you as per current time
def wishme():

    hour=int(datetime.datetime.now().hour)
    #print(hour)
    if(hour >=0 and hour <=12):
        speak("GOOD MORNING"+MASTER)
    elif(hour >=12 and hour <=18):
        speak("GOOD AFTERNOON" + MASTER)
    else:
        speak("GOOD EVENING" + MASTER)
    speak("hii,this is jarvish,Please tell me how may I help you")

#this function is take command from the microphone
def takecommand():
    # this is from speech recognization
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        query=r.recognize_google(audio,language='en-in')
        print("you said " + query)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        query=None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        query=None
    return query
def sendEmail(to,content):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "abhayrathod246@gmail.com"
    password = ''

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email,to,content)

    except Exception as e:
        print(e)
    finally:
        server.quit()
def sendSMS(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):

    req_params = {
            'apikey': apiKey,
            'secret': secretKey,
            'usetype': useType,
            'phone': phoneNo,
            'message': textMessage,
            'senderid': senderId
        }
    return requests.post(reqUrl, req_params)


    # print response if you want







#main program
speak("initializing .....")
wishme()

#query = takecommand().lower()
# Logic for executing tasks based on query
if 1:
    query = takecommand().lower()

    if 'wikipedia' in query:

        speak("Serching Wikipedia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("Accourding to wikipedia")
        speak(result )
        print(result)
    elif 'open youtube' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("youtube.com")
    elif 'open google' in query:
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("google.com")
    elif 'open stackoverflow' in query:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("stackoverflow.com")
    elif 'play music' in query:

    #os model import
        music_dir='E:\\new song'
        song=os.listdir(music_dir)
        rn=random.choice(song)
        print(song)
        os.startfile(os.path.join(music_dir,rn))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak("the sir time is"+strTime)
        print(strTime)
    elif 'open code' in query:
        codepath="C:\\Users\\Abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'open sublime' in query:
        codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(codepath)
    elif 'open notepad' in query:
        codepath="%windir%\\system32\\notepad.exe"
        os.startfile(codepath)
    elif 'email to manali' in query:
        try:

            speak('what should i say??')
            content=takecommand()
            to="manalirathod71 @ gmail.com"
            sendEmail(to,content)
            speak('yout email has been sent')
        except Exception as e:
            print(e)
            speak("Sorry my master.I am not able to send this email")
    elif 'email to deep' in query:
        try:

            speak('what should i say??')
            content = takecommand()
            to = "idipupatel @ gmail.com"
            sendEmail(to, content)
            speak('yout email has been sent')

        except Exception as e:
            print(e)
            speak("Sorry my master.I am not able to send this email")
    elif 'email to banshita' in query:
        try:

            speak('what should i say??')
            content = takecommand()
            to = "banshitagangwar2000@gmail.com"
            sendEmail(to, content)
            speak('yout email has been sent')

        except Exception as e:
            print(e)
            speak("Sorry my master.I am not able to send this email")
    elif 'email to dhaval' in query:
        try:

            speak('what should i say??')
            content = takecommand()
            to = "banshitagangwar2000@gmail.com"
            sendEmail(to, content)
            speak('yout email has been sent')

        except Exception as e:
            print(e)
            speak("Sorry my master.I am not able to send this email")
    elif 'who is banshita' in query:
        speak("she is your classmate sir,you also called her majnubhai")
    elif 'who is dhaval' in query:
        speak("he is one of the bestfriend,,,you both complete your diploma in same college")
    elif 'who is tom' in query:

        speak("he is your friend,classmate and brother")
        print("he is your friend,classmate and brother")
        speak("one of the mature person you know")
        print("one of the mature person you know")
        speak("now he is in canada!!!")
        print("now he is in canada!!!")
    elif 'text to manali' in query:
        print("HELLO")
        api='76U13ANJ2A89OHU1KI5QHI9T01W8TELC'
        privatekey='W19310MX4PU8GLMD'
        yourno='8488824650'
        email='abhayrathod438@gmail.com'
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        speak("what should i say??")
        msg=takecommand()
        response = sendSMS(URL, api, privatekey, 'stage',yourno ,email, msg)
        print('done')

