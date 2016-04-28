from datetime import datetime

from flask import Flask, render_template

from datafoo import get_data

recalls_data = get_data()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html', recalls=recalls_data)

@app.route('/hello')
def hello_world():
    return render_template('helloworld.html', the_date=datetime.now(), numbers=range(1,8))

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
