from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
@app.route("/one", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        print('User Email: ' + email)
    return render_template ('one.html')

@app.route("/two", methods=['GET', 'POST'])
def two():
    if request.method == 'POST':
        password = request.form['password']
        print('User Password: ' + password)
    return render_template('two.html')


if __name__ == "__main__":
   app.run(debug=True)

