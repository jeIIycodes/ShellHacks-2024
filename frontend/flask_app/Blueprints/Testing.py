import pandas as pd
from flask import Blueprint, jsonify, render_template

test_bp=Blueprint("testingStuff", __name__, url_prefix="/testing")

@test_bp.route('/averages')
def show_averages():
    """
    Route to display the averages of each column.
    """
    # Path to the CSV file
    csv_path = 'static/student_spending.csv'

    # Calculate averages
    averages = calculate_averages(csv_path)

    return render_template('averages.html', averages=averages)


@test_bp.route('/TestRoute')
def helloWorld():
    return jsonify({"Hello": "World"})

@test_bp.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return f"{num1 * num2}"