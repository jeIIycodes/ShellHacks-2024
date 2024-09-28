# FrontendServer.py

from flask import Flask, render_template
from Extensions import oauth  # Assuming Extensions.py handles the oauth initialization
from Config import config  # Load configuration
from Blueprints.User import user_bp  # Import the user authentication blueprint

app = Flask(__name__)
app.secret_key = config["WEBAPP"]["SECRET_KEY"]

# Initialize OAuth with Flask app
oauth.init_app(app)

auth0_config = config['AUTH0']
domain = auth0_config["DOMAIN"]
client_id = auth0_config["CLIENT_ID"]
client_secret = auth0_config["CLIENT_SECRET"]

# Register the Auth0 OAuth client
oauth.register(
    'auth0',
    client_id=client_id,
    client_secret=client_secret,
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=f'https://{domain}/.well-known/openid-configuration'
)

# Register the user authentication blueprint
app.register_blueprint(user_bp)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002,debug=True)
