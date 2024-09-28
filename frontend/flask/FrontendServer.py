from flask import Flask, redirect, session, url_for, render_template
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode, quote_plus
import os

# Load configuration from the config file
from config import config

app = Flask(__name__)
app.secret_key = config["WEBAPP"]["SECRET_KEY"]

# Initialize Authlib OAuth client for Auth0
oauth = OAuth(app)

auth0_config = config['AUTH0']
domain = auth0_config["DOMAIN"]
client_id = auth0_config["CLIENT_ID"]
client_secret = auth0_config["CLIENT_SECRET"]
audience = auth0_config["AUDIENCE"]

oauth.register(
    "auth0",
    client_id=client_id,
    client_secret=client_secret,
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f'https://{domain}/.well-known/openid-configuration'
)


# Home route (optional)
@app.route('/')
def home():
    return render_template('home.html')


# Login route
@app.route('/login')
def login():
    return oauth.auth0.authorize_redirect(redirect_uri=url_for("callback", _external=True), audience=audience)


# Auth0 callback route
@app.route('/callback')
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect(url_for("profile"))


# Profile route (requires authentication)
@app.route('/profile')
def profile():
    if "user" not in session:
        return redirect(url_for("login"))

    user_info = session["user"]["userinfo"]
    return render_template('profile.html', user=user_info)


# Logout route
@app.route('/logout')
def logout():
    session.clear()
    params = {
        "returnTo": url_for("home", _external=True),
        "client_id": client_id
    }
    return redirect(f"https://{domain}/v2/logout?" + urlencode(params, quote_via=quote_plus))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
