import speech_recognition as sr
import pyttsx3

#Global VAriable
engine = pyttsx3.init()

def speech_to_text():
    # recognizer ng speech
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    # Capture audio from the microphone
    with sr.Microphone() as source:
        engine.say("You can Talk Now: ")
        engine.runAndWait()
        audio = recognizer.listen(source, timeout=5)
  

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        return text.strip()
    
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    
    
    except sr.RequestError as e:
        print(f"Sorry, there was an error connecting to Google's API: {e}")

def main():

    stop_listening = False
    
    while not stop_listening:
        recognized_text = speech_to_text()
        
        magic_word = "sabihin mo"

        if recognized_text:
            print("You said:", recognized_text)
                #engine.say(recognized_text)
                #engine.runAndWait()

            if recognized_text.lower().startswith(magic_word):
                response = recognized_text[len(magic_word):].strip()
                engine.say(response)
                engine.runAndWait()

            if recognized_text.lower() == "magic word":
                engine.say("Ang magic word ay Gah-Go!")
                engine.runAndWait()

            if recognized_text.lower() == "1 + 1":
                engine.say("Ang sagot ay equals 2")
                engine.runAndWait()
            
            if recognized_text.lower() == "stop":
                engine.say("HEE HEE, goodbye master")
                engine.runAndWait()
                stop_listening = True


if __name__ == "__main__":
    main()