# Blueprints/User.py

from flask import Blueprint, session, redirect, url_for, render_template
import pandas as pd
from Extensions import oauth  # Assuming oauth is initialized in Extensions.py
from urllib.parse import urlencode, quote_plus
from Config import config

auth0_config = config['AUTH0']
domain = auth0_config["DOMAIN"]
client_id = auth0_config["CLIENT_ID"]
audience = auth0_config["AUDIENCE"]

user_bp = Blueprint("user", __name__, url_prefix="/")

# Login route
@user_bp.route('/login')
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("user.callback", _external=True),
        audience=audience
    )

# Auth0 callback route
@user_bp.route('/callback')
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect(url_for("user.profile"))

# Profile route (requires authentication)
@user_bp.route('/profile')
def profile():
    if "user" not in session:
        return redirect(url_for("user.login"))

    user_info = session["user"]["userinfo"]
    return render_template('profile.html', user=user_info)

@user_bp.route('/datapage')
def datapage():
    if "user" not in session:
        return redirect(url_for("user.login"))
    
    csv_file_path = './static/student_spending.csv'
    
    def calculate_averages(csv_file_path):
        try:
        # Read the CSV file using pandas
            df = pd.read_csv(csv_file_path)

        # Select only numerical columns and exclude 'ID'
            numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            if 'ID' in numerical_cols:
                numerical_cols.remove('ID')

        # Calculate the average for each numerical column
            averages = df[numerical_cols].mean().round(2).to_dict()
            print("Averages:", averages.keys())
            return averages
        
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return {}
        
    averages = calculate_averages(csv_file_path)
    
    
    average_keys = list(averages.keys()) if averages else []
    average_values = list(averages.values()) if averages else []
    print("keys:",average_keys)
    print("values:",average_values)
    user_info = session["user"]["userinfo"]
    
    return render_template('datapage.html', averages=averages, average_keys=average_keys, average_values=average_values)

# Logout route
@user_bp.route('/logout')
def logout():
    session.clear()
    params = {
        "returnTo": url_for("home", _external=True),
        "client_id": client_id
    }
    return redirect(f"https://{domain}/v2/logout?" + urlencode(params, quote_via=quote_plus))



@user_bp.route('/scholarships')
def scholarships():
    return "pp"


@user_bp.route('/resources')
def resources():
    return "pp"