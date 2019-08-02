import os
from datetime import datetime
from flask import Flask, render_template, url_for, jsonify, request

from artifice.website.schemas import StoryCore
from artifice.util import right_now, decorate_time


loc = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


_published = datetime(2019, 7, 30, 2, 39, 10, 744482)
_current = right_now()
social = dict(
    comments=2,
    views=4,
    likes=18,
    shares=9,
)
meta = dict(
    publish_date=_published,
    current_time=_current,
    elapsed_time=decorate_time(_published,_current),
)
photo = dict(
    # image="https://www.newleafls.com/uploads/2019/05/hero-landscape.jpg",
    image="https://steamuserimages-a.akamaihd.net/ugc/2433509963997568736/4BF2B74EC1D22EA9DDAD1485342249025A5D97BB/",
    caption="Photo of a landscape.",
)
content = dict(
    topic="Technology",
    headline="This Is The Headline You\'ll Write",
    author="Admin",
)
link = dict(
    url="#",
    story_id=1,
)
story = dict(
    content=content,
    meta=meta,
    photo=photo,
    social=social,
    link=link,
)

story_core = StoryCore()

@app.route("/")
def index():
    global story
    schema = story_core.dump(story)
    carousel_posts = [schema.data] * 3
    popular_posts = [schema.data] * 4
    timeline_posts = [schema.data] * 11
    stories = dict(
        carousel_posts=carousel_posts,
        popular_posts=popular_posts,
        timeline_posts=timeline_posts,
    )
    return render_template("index.html", stories=stories)


@app.route("/raw")
def raw():
    global story
    schema = story_core.dump(story)
    carousel_posts = [schema.data] * 1
    popular_posts = [schema.data] * 2
    timeline_posts = [schema.data] * 3
    stories = dict(
        carousel_posts=carousel_posts,
        popular_posts=popular_posts,
        timeline_posts=timeline_posts,
    )
    return jsonify(**stories)


@app.route("/info")
def info():
    data = dict(
        loc=loc,
        routes=["/","/raw","/info"],
    )
    return jsonify(**data)


@app.route("/echo", methods=["GET","POST"])
def echo():
    # data = request.get_json() if not not request.data else None
    params = dict(
        method=request.method,
        headers=[{k:v} for k, v in request.headers.items()],
        args=[{k:v} for k, v in request.args.items()],
        form=[{k:v} for k, v in request.form.items()],
        data=(request.get_json() if not not request.data else None),
    )
    return jsonify(**params)


if __name__ == '__main__':
    app.run(
        debug=True
    )
