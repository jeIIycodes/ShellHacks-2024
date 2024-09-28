import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    return { 'status' : 'ok' }

#Need to add /prompt to extension to ge it running correctly (note: add the applicable weblinks file)
@app.route("/prompt", methods=['POST','GET'])
def prompt():
    genai.configure(api_key=os.getenv('API_KEY'))

    messages = [ 
        # System prompt used to set context for the conversation
        # { "role": "system", "content": "You are an experienced software engineer." }
    ]

    #prompt_text = request.get_data()
    #prompt_text = prompt_text.decode('utf-8')

    # append user prompt from request
    messages.append({ "role": "user", "content": "hello how are you?" })

    # call the gemini-1.5-flash
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("Generating content...")
    chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
    response = chat.send_message("I have 2 dogs in my house.")
    print(response.text)
    response = chat.send_message("How many paws are in my house?")
    print(response.text)

    return { 'status' : 'ok', 'response' : response.text }
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

