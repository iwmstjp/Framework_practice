from testapp import app
from flask import render_template

@app.route('/')
def index():
    my_dict={
        "message":"Flask",
        "fruits":["apple", "orange", "banana"]
    }
    return render_template("testapp/index.html", data=my_dict)