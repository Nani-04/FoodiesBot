import time
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

voices = tts_engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "en_us+f" in voice.id:
        tts_engine.setProperty('voice', voice.id)
        break
tts_engine.setProperty('rate', 160)


def speak(text, delay=0):
    tts_engine.say(text)
    tts_engine.runAndWait()
    time.sleep(delay)


def listen(timeout=5):
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Sorry, the service is unavailable.")
            return ""
        except sr.WaitTimeoutError:
            return None


def detect_intent(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey", "how are you"]):
        return "greeting"
    elif "menu" in user_input:
        return "show_menu"
    elif any(word in user_input for word in ["not sure", "suggest", "recommend", "help order"]):
        return "suggest_food"
    elif any(word in user_input for word in ["order", "yes, i want", "confirm"]):
        return "confirm_order"
    elif any(word in user_input for word in ["table number", "my table is"]):
        return "table_number"
    elif "appetizer" in user_input:
        return "appetizer_menu"
    elif "email" in user_input:
        return "provide_email"
    elif any(word in user_input for word in ["feedback", "rate", "review"]):
        return "feedback"
    elif any(word in user_input for word in ["delivery", "location", "deliver"]):
        return "delivery_info"
    elif any(word in user_input for word in ["stop", "exit", "goodbye"]):
        return "farewell"
    elif any(word in user_input for word in ["specials", "vegan", "wednesday"]):
        return "specials"
    elif any(word in user_input for word in ["dosa", "samosa", "idly", "curries"]):
        return "specific_food"
    elif any(word in user_input for word in ["about", "history", "restaurant"]):
        return "about_us"
    else:
        return "unknown"


def handle_response(intent):
    if intent == "greeting":
        speak("I am fine, thank you for asking. Welcome to our restaurant!", delay=1)
        speak("How can I assist you today?", delay=1)
    elif intent == "show_menu":
        speak("Here is our menu: https://example.com/menu.jpg")
        speak("Please take your time and let me know if you have any questions.")
    elif intent == "suggest_food":
        speak("Oh, I recommend our vegan special or butter dosa. Would you like more details?")
    elif intent == "confirm_order":
        speak("Great! I'll place the order for you.")
        speak("Your delicious meal will be ready shortly.")
    elif intent == "table_number":
        speak("Got it! Please relax at your table while we prepare your order.")
    elif intent == "appetizer_menu":
        speak("Here is the appetizer menu: https://example.com/appetizers.jpg")
        speak("What would you like to have?")
    elif intent == "provide_email":
        speak("Please provide your email, and I’ll send you the receipt.")
    elif intent == "feedback":
        speak("We’d love to hear your feedback. Please share your thoughts!")
    elif intent == "delivery_info":
        speak("We deliver to Cedar Park and South Austin. Let us know where you'd like your food!")
    elif intent == "farewell":
        speak("Goodbye! Have a great day!")
    elif intent == "specials":
        speak("Today is Vegan Wednesday! Buy one, get one free on vegan specials.")
    elif intent == "specific_food":
        speak("That’s a popular choice! Would you like me to order it for you?")
    elif intent == "about_us":
        speak("We are proud to serve authentic South Indian food with love and tradition.")
    else:
        speak("I'm sorry, I didn't quite understand that. Could you please rephrase?")


def main():
    print("Chatbot is running. Say something...")
    speak("Hello! Welcome to FoodiesBot. How can I help you today?")
    while True:
        user_input = listen()

        if not user_input:
            continue

        intent = detect_intent(user_input)

        if intent == "farewell":
            handle_response(intent)
            break

        handle_response(intent)


if __name__ == "__main__":
    main()
