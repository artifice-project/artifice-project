from datetime import datetime
from marshmallow import Schema, fields, pprint
from flask import Flask, render_template, url_for, jsonify


app = Flask(__name__)


class StorySocial(Schema):
    comments = fields.Int()
    views = fields.Int()
    likes = fields.Int()
    shares = fields.Int()


class StoryMeta(Schema):
    publish_date = fields.DateTime()
    elapsed_time = fields.DateTime()


class StoryPhoto(Schema):
    image = fields.Str()
    caption = fields.Str()


class StoryContent(Schema):
    topic = fields.Str()
    headline = fields.Str()
    author = fields.Str()


class StoryCore(Schema):
    meta = fields.Nested(StoryMeta())
    social = fields.Nested(StorySocial())
    photo = fields.Nested(StoryPhoto())
    content = fields.Nested(StoryContent())


social = dict(
    comments=2,
    views=4,
    likes=18,
    shares=9,
)

meta = dict(
    publish_date=datetime.now(),
    elapsed_time=datetime.now(),
)

photo = dict(
    image = "https://www.newleafls.com/uploads/2019/05/hero-landscape.jpg",
    caption = "Photo of a landscape.",
)

content = dict(
    topic="Technology",
    headline = "This Is The Headline You\'ll Write",
    author="Admin",
)

story = dict(
    content=content,
    meta=meta,
    photo=photo,
    social=social,
)

# schema = StoryCore()
# result = schema.dump(story)
# pprint(result.data, indent=2)

@app.route("/")
def index():
    global story
    schema = StoryCore().dump(story)
    carousel_posts = [schema.data] * 3
    popular_posts = [schema.data] * 4
    timeline_posts = [schema.data] * 10
    stories = dict(
        carousel_posts=carousel_posts,
        popular_posts=popular_posts,
        timeline_posts=timeline_posts
    )
    return render_template("index.html", stories=stories)
    # return jsonify(stories)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
