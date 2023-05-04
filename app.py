
from flask import Flask, render_template, request
from flaskext.markdown import Markdown

from ai.summariser import youtube_video_summariser

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

if __name__ == "__main__":
    app.run(debug=True)