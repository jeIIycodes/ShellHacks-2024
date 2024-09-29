import os
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

#Plan: Using the methods in this file to receive the GET request and then jsonify them into a single json file to be presented to main.py
# and Gemini located in there to be written into example essay
#Specific information needed from assessment
# years_in_college
# field_of_study
# gender_self_describe
# florida_resident
# first_gen_college_student
# race_self_describe
# mean_yearly_income
# expected_yearly_scholarships
# housing
@app.route('/api/params', methods=['GET'])
def get_data():
    years_in_college = request.args.get('years_in_college', default=0)
    field_of_study = request.args.get('field_of_study', default=None)
    gender_self_describe = request.args.get('gender_self_describe', default=None)
    florida_resident = request.args.get('florida_resident', default=No)
    first_gen_college_student = request.args.get('first_gen_college_student', default=No)
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