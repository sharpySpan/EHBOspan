from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/cursus')
def cursus():
    return render_template("cursus.html")

if __name__ == '__main__':
    app.run()
