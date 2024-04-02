import flask
from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.secret_key = 'ietsiets'

connection = pymysql.connect(host="localhost", user="root", passwd="", database="flipquiz")
cursor = connection.cursor()


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        data = cursor.fetchone()
        session['id'] = data[0]

        global idd
        idd = session['id'] = data[0]

        if data:
            session['loggedin'] = True
            return redirect(url_for('quiz_Home'))
    else:
        return flask.render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        school_name = request.form['school_name']
        subject = request.form['subject']

        cursor.execute('INSERT INTO users (email, password, name, schoolname, subject ) values (%s, %s, %s, %s, %s)', (email, password, name, school_name, subject))
        connection.commit()

        return flask.render_template('home.html')
    else:
        return flask.render_template('register.html')


if __name__ == '__main__':
    app.run()