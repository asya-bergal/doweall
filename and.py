from flask import Flask
from models import *
app = Flask(__name__)

@app.route('/<question>/<yesno>')
def display_and(question, yesno):
    bit = yesno.lower() in ["yes", "y", "1"]
    result, responses = compute_and(question, bit)
    answer = "Yes" if result else "No" 
    return ("%s. There have been a total of %d responses this question." % (answer, responses))
