@echo off
set "project_name=ChatBotProject"

:: Create project folder
mkdir %project_name%
cd %project_name%

:: Create subdirectories
mkdir config
mkdir data
mkdir modules

:: Create main.py file with initial template code
echo import speech_recognition as sr > main.py
echo import pyttsx3 >> main.py
echo. >> main.py
echo # Initialize the recognizer and text-to-speech engine >> main.py
echo recognizer = sr.Recognizer() >> main.py
echo tts_engine = pyttsx3.init() >> main.py
echo. >> main.py
echo def speak(text): >> main.py
echo     """Converts text to speech.""" >> main.py
echo     tts_engine.say(text) >> main.py
echo     tts_engine.runAndWait() >> main.py
echo. >> main.py
echo def listen(): >> main.py
echo     """Captures voice input and converts it to text.""" >> main.py
echo     with sr.Microphone() as source: >> main.py
echo         print("Listening...") >> main.py
echo         audio = recognizer.listen(source) >> main.py
echo         try: >> main.py
echo             text = recognizer.recognize_google(audio) >> main.py
echo             print(f"You said: {text}") >> main.py
echo             return text >> main.py
echo         except sr.UnknownValueError: >> main.py
echo             print("Sorry, I could not understand the audio.") >> main.py
echo             return "" >> main.py
echo         except sr.RequestError: >> main.py
echo             print("Sorry, the service is unavailable.") >> main.py
echo             return "" >> main.py
echo. >> main.py
echo def main(): >> main.py
echo     """Main function to run the chatbot.""" >> main.py
echo     print("Chatbot is running. Say something...") >> main.py
echo     speak("Hello! How can I help you today?") >> main.py
echo     while True: >> main.py
echo         user_input = listen() >> main.py
echo         if user_input.lower() == "exit": >> main.py
echo             speak("Goodbye!") >> main.py
echo             break >> main.py
echo         # Here, add chatbot response generation logic >> main.py
echo         response = f"You said: {user_input}"  ^&:: Placeholder response >> main.py
echo         print(f"Bot: {response}") >> main.py
echo         speak(response) >> main.py
echo. >> main.py
echo if __name__ == "__main__": >> main.py
echo     main() >> main.py

:: Create README.md file
echo # ChatBot Project > README.md
echo. >> README.md
echo This is a chatbot project template. >> README.md

echo Project structure for '%project_name%' has been created successfully.
