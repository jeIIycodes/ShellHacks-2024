# Blueprints/User.py

from flask import Blueprint, session, redirect, url_for, render_template
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
    return oauth.auth0.authorize_redirect(redirect_uri=url_for("user.callback", _external=True), audience=audience)


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


# Logout route
@user_bp.route('/logout')
def logout():
    session.clear()
    params = {
        "returnTo": url_for("home", _external=True),
        "client_id": client_id
    }
    return redirect(f"https://{domain}/v2/logout?" + urlencode(params, quote_via=quote_plus))


