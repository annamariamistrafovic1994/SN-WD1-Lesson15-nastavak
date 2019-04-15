from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_year = datetime.datetime.now().year
    
    cities = ["Boston", "Vienna", "Paris", "Berlin"]
    
    return render_template("index.html", current_year=current_year, cities=cities)


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

if __name__=='__main__':
    app.run()



