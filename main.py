# python main.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def times():
    return render_template("times.html")

if __name__ == "__main__":
    app.run(debug=True)