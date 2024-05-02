from flask import Flask, render_template, request

app = Flask(__name__)

criminals = []

@app.route('/')
def index():
    return render_template('index.html', criminals=criminals)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    image_url = request.form['image_url']
    information = request.form['information']
    criminals.append({'name': name, 'image_url': image_url, 'information': information})
    return render_template('index.html', criminals=criminals)

if __name__ == '__main__':
    app.run(debug=True)

