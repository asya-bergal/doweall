from flask import Flask
from models import *
app = Flask(__name__)

@app.route('/<question>/<yesno>')
def display_and(question, yesno):
    bit = 0
    if yesno in ["yes", "y"]:
        bit = 1
    result, responses = compute_and(question, bit)
    answer = "No"
    if result == 1:
        answer = "Yes"
    return ("%s. There have been a total of %d responses this question." % (answer, responses))
