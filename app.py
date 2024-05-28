import flask
from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.secret_key = 'ietsiets'

connection = pymysql.connect(host="localhost", user="root", passwd="", database="dnd")
cursor = connection.cursor()


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (email, password))
        data = cursor.fetchone()
        session['id'] = data[0]

        global idd
        idd = session['id'] = data[0]

        if data:
            session['loggedin'] = True
            return flask.render_template('home.html')
    else:
        return flask.render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute('INSERT INTO user (username, password ) values (%s, %s)', (email, password))
        connection.commit()

        return flask.render_template('login.html')
    else:
        return flask.render_template('register.html')

@app.route('/home')
def home():
    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run()