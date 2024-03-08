from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        return render_template('login.html', name=name, password=password)
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)