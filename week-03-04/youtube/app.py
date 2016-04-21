from flask import Flask, render_template, Markup
import requests

def is_url_ok(url):
    return 200 == requests.head(url).status_code

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Hello world"

@app.route('/videos/<vid>')
def videos(vid):
    youtube_url = 'https://www.youtube.com/watch?v=' + vid
    if is_url_ok(youtube_url):
        hed = """<a href="{url}">YouTube video: {id}</a>""".format(url=youtube_url, id=vid)
    else:
        # when the youtube video id is not found
        hed = """Youtube video {id} <strong>does not exist</strong>""".format(id=vid)
        vid = 'dQw4w9WgXcQ'
    return render_template('video.html', headline=Markup(hed), youtube_id=vid)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
