import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia as wiki
import webbrowser
import pywhatkit as pk
import sys
import time
import pyjokes
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',200)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    query = query.lower()
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good Morning Boss, its {tt}")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon Boss, its {tt}")
    else:
        speak(f"Good Evening Boss, its {tt}")
    speak(" Team hash it out. please tell me how can i help you")

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=033d8fd208684cbe8fd429998e76788e'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__":
    wish()
    while True:
   # if 1:


        query = takecommand().lower()

        # logic building
        if "open command prompt" in query:
            os.system("start cmd")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "who is" in query:
            query = query.replace("who is ", "")
            result = wiki.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wiki.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "play" in query:
            query = query.replace("play", "")
            speak("playing " + query)
            pk.playonyt(query)
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)



        # to close application
        elif "close command prompt" in query:
            speak("okay sir closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        # to change window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()


        # To find my location
        elif "where i am" in query or "where we are" in query or "what is my location" in query:
            speak("wait sir, let me find")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print (geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak(" sorry sir, Due to network issue i am not able to find our location.")
                pass

        # To take screen shot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold screen for few seconds , i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("it is done sir, the screenshot is saved in main folder. now i am ready for next command")

        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you something..")


        elif "how are you" in query:
            speak("i am fine sir, what about you.")

        elif "fine" in query or "good" in query or "also good" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure sir.")

        elif "you can sleep" in query or "sleep now" in query:
            speak("ok sir i am going to sleep .")

        elif "no thanks" in query or "no" in query:
            speak("thanks for using me sir, have a great day.")
            sys.exit()

        speak("sir, do yo have any other work")