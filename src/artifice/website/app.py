from datetime import datetime
from flask import Flask, render_template, url_for, jsonify

import artifice.util
from schemas import StoryCore

app = Flask(__name__)


social = dict(
    comments=2,
    views=4,
    likes=18,
    shares=9,
)
_published = datetime(2019, 7, 30, 2, 39, 10, 744482)
_current = artifice.util.right_now()
meta = dict(
    publish_date=_published,
    current_time=_current,
    elapsed_time=artifice.util.decorate_time(_published,_current),
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
)
story = dict(
    content=content,
    meta=meta,
    photo=photo,
    social=social,
    link=link,
)


@app.route("/")
def index():
    global story
    schema = StoryCore().dump(story)
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
    schema = StoryCore().dump(story)
    carousel_posts = [schema.data] * 1
    popular_posts = [schema.data] * 2
    timeline_posts = [schema.data] * 3
    stories = dict(
        carousel_posts=carousel_posts,
        popular_posts=popular_posts,
        timeline_posts=timeline_posts,
    )
    return jsonify(stories)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
