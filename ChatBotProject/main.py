import time
import speech_recognition as sr
import pyttsx3
from PIL import Image, ImageTk
import tkinter as tk

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


def show_menu_image():
    root = tk.Tk()
    root.title("Menu")
    image = Image.open("menu.jpg")  # Replace with the actual path to your menu image
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(root, image=img)
    panel.pack()
    root.mainloop()


def detect_intent(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey", "how are you"]):
        return "greeting"
    elif "menu" in user_input:
        return "show_menu"
    elif any(dish in user_input for dish in ["dosa", "samosa", "idly", "paneer tikka"]):
        return "dish_name"
    elif any(word in user_input for word in ["not sure", "suggest", "recommend", "help order"]):
        return "suggest_food"
    elif any(word in user_input for word in ["one plate", "yes, i want"]):
        return "confirm_order"
    elif any(word in user_input for word in ["table number", "my table is"]):
        return "table_number"
    elif "appetizer" in user_input:
        return "appetizer_menu"
    elif "email" in user_input:
        return "provide_email"
    elif any(word in user_input for word in ["ok", "wow", "great", "thank you"]):
        return "apply_discount"
    elif any(word in user_input for word in ["stop", "exit", "goodbye"]):
        return "farewell"
    elif any(word in user_input for word in ["vegan wednesday", "vegan specials", "buy one get one"]):
        return "vegan_wednesday"
    elif any(word in user_input for word in ["dosa", "samosa", "idly", "idiyappam", "curries", "rice"]):
        return "specific_food"
    elif any(word in user_input for word in ["cedar park", "south austin", "delivery", "deliver"]):
        return "delivery_info"
    elif "nala's" in user_input:
        return "about_nalas"
    return "unknown"


def handle_response(intent, user_input=None):
    if intent == "greeting":
        speak("I am fine, I hope you are doing great.", delay=1.5)
        speak("Thank you for visiting my restaurant. Please let me know which delicious food you are looking to order.",
              delay=2)
    elif intent == "show_menu":
        speak("Here is our menu.", delay=1)
        show_menu_image()
    elif intent == "dish_name":
        speak("Would you like me to order this for you?", delay=1)
        speak("Or would you like me to read out the ingredients?")
    elif intent == "suggest_food":
        speak("Oh! Yes, this vegan meal is a top choice of our foodies. I would love to eat that if I were human.",
              delay=1.5)
    elif intent == "confirm_order":
        speak("Great! I will place an order for you.", delay=1)
        speak(
            "Your hot, mouth-watering food will be coming to your table, made by our experienced chef and beautiful waiter.")
        speak("The total of the order is $32. Should I go ahead and place the order?")
    elif intent == "table_number":
        speak("Thank you! Please be seated while your food is being prepared.", delay=1)
        speak("Would you like to have any appetizers?")
    elif intent == "appetizer_menu":
        speak("Here is the appetizer menu.")
    elif intent == "provide_email":
        speak("Thank you, I’ll send the receipt to your email shortly.")
    elif intent == "apply_discount":
        speak("Fantastic! I’ll apply a discount. Your total is now $28.", delay=1.5)
        speak("I’ve placed your order, and an email confirmation has been sent to you.")
    elif intent == "vegan_wednesday":
        speak(
            "Every Wednesday, we have Vegan Wednesday specials. Buy one get one free on vegan dishes. You can enjoy a variety of vegan meals at a great deal.")
    elif intent == "specific_food":
        speak(
            "Yes, we have a variety of South Indian dishes including dosa, samosa, idly, idiyappam, curries, rice, and more vegan choices.")
    elif intent == "delivery_info":
        speak("Yes, we offer delivery to Cedar Park and South Austin. Let us know where you need your food delivered!")
    elif intent == "about_nalas":
        speak(
            "Nala's is a taste of South India, bringing authentic South Indian flavors to your table with love and tradition.")
    elif intent == "farewell":
        speak("Goodbye! Have a great day!")
    else:
        speak("I'm sorry, I didn't understand that. Could you please clarify?")


def main():
    print("Chatbot is running. Say something...")
    speak("Hello! How can I help you today?")
    while True:
        user_input = listen()

        if not user_input:
            continue

        intent = detect_intent(user_input)

        if intent == "farewell":
            handle_response(intent)
            break

        handle_response(intent, user_input)


if __name__ == "__main__":
    main()
