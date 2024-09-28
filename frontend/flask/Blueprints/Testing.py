import pandas as pd
from flask import Blueprint, jsonify, render_template

test_bp=Blueprint("testingStuff", __name__, url_prefix="/testing")


def calculate_averages(csv_file_path):
    """
    Reads the CSV file and calculates the average of each numerical column.
    Excludes the 'ID' column from the calculations.

    Args:
        csv_file_path (str): Path to the CSV file.

    Returns:
        dict: A dictionary with column names as keys and their average as values.
    """
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(csv_file_path)

        # Select only numerical columns and exclude 'ID'
        numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        if 'ID' in numerical_cols:
            numerical_cols.remove('ID')

        # Calculate the average for each numerical column
        averages = df[numerical_cols].mean().round(2).to_dict()

        return averages
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return {}


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