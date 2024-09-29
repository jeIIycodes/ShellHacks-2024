import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from flask import Flask
from flask import request
import requests
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return { 'status' : 'ok' }

@app.route('/api/params', methods=['GET'])
def get_data():
    years_in_college = request.args.get('years_in_college', default=0)
    field_of_study = request.args.get('field_of_study', default=None)
    gender_self_describe = request.args.get('gender_self_describe', default=None)
    florida_resident = request.args.get('florida_resident', default="No")
    first_gen_college_student = request.args.get('first_gen_college_student', default="No")
    race_self_describe = request.args.get('race_self_describe', default=None)
    mean_yearly_income = request.args.get('mean_yearly_income', default=0)
    expected_yearly_scholarships = request.args.get('expected_yearly_scholarships', default=0)
    housing = request.args.get('housing')
    
    data = {
        'years_in_college': years_in_college,
        'field_of_study': field_of_study,
        'gender_self_describe': gender_self_describe,
        'florida_resident': florida_resident,
        'first_gen_college_student': first_gen_college_student,
        'race_self_describe': race_self_describe,
        'mean_yearly_income': mean_yearly_income,
        'expected_yearly_scholarships': expected_yearly_scholarships,
        'housing': housing
    }

    #return jsonify(data), 200

    #Test return
    return jsonify({
        "years_in_college": 4,
        "field_of_study": "Computer Science",
        "gender_self_describe": "male",
        "florida_resident": True,
        "first_gen_college_student": False,
        "race_self_describe": "white",
        "mean_yearly_income": 60000,
        "expected_yearly_scholarships": 10000,
        "housing": "on-campus"
    })

#Need to add /prompt to extension to ge it running correctly (note: add the applicable weblinks file)
@app.route("/prompt", methods=['POST'])
def prompt():
    dotenv_path = os.path.join(os.path.dirname(__file__), 'python-ai-backend/app/.env')
    load_dotenv(dotenv_path) 
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key)
    try:
        # Parse the incoming JSON data
        params_response = requests.get('http://localhost:5000/api/params')

        if params_response.status_code != 200:
            return jsonify({"error": "Failed to retrieve parameters"}), params_response.status_code
        
        print(params_response)
        # Parse the JSON data
        #data = params_response.json()
        #print(data)

        prompt = json.dumps(params_response, indent=2)

        # call the gemini-1.5-flash
        model = genai.GenerativeModel("gemini-1.5-flash")
        print("Generating content...")
        response = model.generate_content(["Give me a sample essay using these parameters.", prompt])
        print(response.text)
        # Check if the response is successful
        if response.status_code == 200:
            # Return the text response directly to the user
            return response.text, 200
        else:
            return response.text, response.status_code

    except Exception as e:
        return str(e), 400
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

