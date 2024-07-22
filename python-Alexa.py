import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Function to speak the text."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    # Function to listen and recognize commands from the microphone.
    try:
        with sr.Microphone() as source:
            print('Say Something................')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def process_command(command):
    # Function to process recognized command and execute corresponding actions.
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
        print(time)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '').strip()
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'date' in command:
        talk('Sorry buddy, I have a boyfriend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing music {song}')
        pywhatkit.playonyt(song)
        print(f'Playing: {song}')
    else:
        talk('Please say the command again')

def run_alexa():
    # Main function to run the Alexa-like assistant.
    while True:
        command = take_command()
        if command:
            process_command(command)

if __name__ == "__main__":
    run_alexa()
