from flask import Flask

app = Flask(__name__)

MAP_BASE = 'https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers={}'
STREET_VIEW_BASE = 'https://maps.googleapis.com/maps/api/streetview?size=700x300&location={}'

@app.route('/')
def homepage():
    return 'Hello world!'

@app.route('/foo/<thing>')
def hello_thing(thing):
    txt = 'Hello, ' + thing
    txt += '''
<img src="{}">
<img src="{}">
    '''.format(MAP_BASE.format(thing), STREET_VIEW_BASE.format(thing))
    return txt


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
