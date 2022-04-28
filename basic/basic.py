from flask import Flask,url_for,redirect
from daily import *

app = Flask(__name__)

@app.route("/")
def intro():
    #home.html
    return get_all_to_do()

@app.route("/day/<name>")
def day(name):
    return get_the_to_do(name)

if __name__ == "__main__":
    app.run(debug=True)