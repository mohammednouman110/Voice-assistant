import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# ---------- SPEAK FUNCTION ----------
def speak(text):
    engine.say(text)
    engine.runAndWait()


# ---------- COMMAND HANDLER ----------
def process_Command(c):
    c = c.lower()   # Convert to lowercase to avoid case-sensitivity issues
    
    if "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "show time" in c:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")
    
    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    
    else:
        speak("I am not sure how to do that yet.")

# ---------- MAIN LOOP ----------
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_Command(command)

        # ---------- EXCEPTIONS ----------
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")

        except sr.UnknownValueError:
            print("Sorry, I didn’t understand that.")
            speak("Sorry, I didn’t catch that. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, I didn't catch that. Please try again.")
