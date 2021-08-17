import speech_recognition as s
voice=s.Recognizer()
with s.Microphone() as source:
    print("Speak Now")
    audio=voice.listen(source)
    try:
        txt=voice.recognize_google(audio)
        print("you said",txt)
    except:
        print("you said not proper")
