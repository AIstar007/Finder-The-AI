import datetime
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Fixed 'voices' to 'voice'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Finder, please tell me how can I help you")


def textCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        question = r.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")

    except Exception:
        print("Say that again please")
        speak("please say that again")
        return "none"
    return question.lower()


def sendEmail(to, content):  # First you have to enable "Less secure Apps"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        sender_email = input("Enter your Email : ")
        sender_password = input("Enter your Password : ")
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry sir, I have failed to send the email")


wish()

contacts = {
    'alice': 'alice@example.com',
    'bob': 'bob@example.com'
}

while True:
    question = textCommand()

    if 'wikipedia' in question:
        speak("Searching Wikipedia...")
        question = question.replace("wikipedia", "")
        try:
            results = wikipedia.summary(question, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        except Exception:
            speak("Sorry, I could not find any information on that topic.")

    elif 'open youtube' in question:
        webbrowser.open("https://youtube.com")

    elif 'open google' in question:
        webbrowser.open("https://google.com")

    elif 'my name' in question:
        speak("You asked about your name, but I don't know it yet!")

    elif 'time' in question:
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        speak(f"The time is {time_str}")

    elif 'date' in question:
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        speak(f"Today's date is {date_str}")

    elif 'your name' in question:
        speak("My name is Finder")

    elif 'tomorrow' in question:
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        speak(tomorrow.strftime("Tomorrow will be %B %d, %Y"))

    elif 'is this a leap year' in question:
        year = datetime.datetime.now().year
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            speak("Yes, this is a leap year.")
        else:
            speak("No, this is not a leap year.")

    elif 'open instagram' in question:
        webbrowser.open('https://instagram.com')

    elif 'email to' in question:
        try:
            words = question.split()
            name = words[words.index('to') + 1]
            if name in contacts:
                speak("What should I say sir?")
                content = textCommand()
                if content == "none":
                    speak("Email cancelled.")
                    continue
                to = contacts[name]
                sendEmail(to, content)
            else:
                speak(f"Sorry, I don't have an email address for {name}")
        except Exception:
            speak("Sorry sir, I couldn't process the email command.")

    elif 'who are you' in question:
        speak("I am Finder. An AI Featured Desktop Assistant")

    elif 'how are you' in question:
        speak("I am well sir, How are you?")

    elif 'i am well' in question:
        speak("Have a nice day sir")

    elif 'i am not well' in question:
        speak("Sorry about that sir, may you recover soon")

    elif 'exit' in question or 'quit' in question:
        speak("Exiting...")
        sys.exit()

    else:
        speak("I didn't understand that. Please say it again.")
