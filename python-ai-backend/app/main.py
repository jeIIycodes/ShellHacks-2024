import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return { 'status' : 'ok' }

#Need to add /prompt to extension to ge it running correctly (note: add the applicable weblinks file)
@app.route("/prompt", methods=['POST','GET'])
def prompt():

    url = 'http://127.0.0.1:5000/api/params'
    # Make the GET request
    responseJ = requests.get(url)
    # Check if the request was successful
    if responseJ.status_code == 200:
        # Parse the JSON response
        json_data = responseJ.json()
        print(json_data)
    else:
        print(f"Error: {responseJ.status_code} - {responseJ.text}")

    genai.configure(api_key=os.getenv('API_KEY'))

    # call the gemini-1.5-flash
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("Generating content...")
    response = model.generate_content(["Give me a sample essay using these parameters.", json_data])

    return { 'status' : 'ok', 'response' : response.text }
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

