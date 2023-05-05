
from flask import Flask, render_template, request, Response
from flaskext.markdown import Markdown

from ai.summariser import youtube_video_summariser
from streaming import chain

app = Flask(__name__)
Markdown(app)

@app.get('/')
def home():
    return render_template('home.html')

@app.post("/summarize")
def summarize():
    url = request.form.get('url')
    summary = youtube_video_summariser(url)

    return render_template('video.html', summary=summary)

@app.route('/summarize/stream', methods=['POST'])
def strem():
    url = request.form.get('url')
    article = request.form.get('is_article')
    return Response(chain(url, article), mimetype='text/plain')

if __name__ == "__main__":
    app.run(threaded=True, debug=True)