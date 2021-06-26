from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('templates/index.html')

@app.route("/about")
def about():
    return render_template('templates/about.html')

@app.route("/more")
def more():
    return render_template('more.html')






app.run(debug=True)
