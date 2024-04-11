from flask import Flask 
app= Flask(__name__)
@app.route("/")
def home():
    return "Welcome"

from controllers import user_controller
    