from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print("Email:", email)
        print("Password:", password)

        message = "Login Successful"

    return render_template('login.html', message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

        message = "Registration Successful"

    return render_template('register.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)