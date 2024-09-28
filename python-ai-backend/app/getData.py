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
def get_items():
    years_in_college = request.args.get('years_in_college')
    field_of_study = request.args.get('field_of_study')
    gender_self_describe = request.args.get('gender_self_describe')
    florida_resident = request.args.get('florida_resident')
    first_gen_college_student = request.args.get('first_gen_college_student')
    race_self_describe = request.args.get('race_self_describe')
    mean_yearly_income = request.args.get('mean_yearly_income')
    expected_yearly_scholarships = request.args.get('expected_yearly_scholarships')
    housing = request.args.get('housing')
    
     # Create a dictionary of the parameters
    params = {
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

    return jsonify(params)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')