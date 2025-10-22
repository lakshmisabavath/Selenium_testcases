from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('form.html')  # your username/password form

@app.route('/result', methods=['POST'])
def result():
    username = request.form['username']
    password = request.form['pwd']
    return render_template('result.html', username=username, password=password)

if __name__ == '__main__':
    app.run(debug=True)
