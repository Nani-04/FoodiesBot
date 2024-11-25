from flask import Flask, request, jsonify

# Define the Flask app
app = Flask(__name__)

# Welcome route
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Chatbot API! Use the /chat endpoint for chatbot interaction."

# Chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the request
        user_message = request.json.get('message', '').lower()

        # Response logic
        if "menu" in user_message:
            response = {"text": "Here is our menu: https://example.com/menu.jpg"}
        elif any(dish in user_message for dish in ["dosa", "samosa", "idly"]):
            response = {
                "text": "Would you like me to order this for you, or should I read out the ingredients?",
                "options": ["Order", "Read Ingredients"]
            }
        else:
            response = {"text": "I'm sorry, I didn't understand that. Could you try again?"}

    except AttributeError:
        # Handle cases where the request JSON is invalid
        response = {"text": "Invalid request. Please send a JSON object with a 'message' key."}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
