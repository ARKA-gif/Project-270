# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC68033d0260e4c2f3ac073784ef67248b'
        auth_token = '27ee99a383d92894c3875228a7fab09c'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VA7fa0d40c162843de97a9e39eb453c8c5') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



        verification = client.verify \
            .services('VA7fa0d40c162843de97a9e39eb453c8c5') \
            .verifications \
            .create(to=mobile_number, channel='sms')










if __name__ == "__main__":
    app.run()

