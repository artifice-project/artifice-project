from marshmallow import Schema, fields, pprint

class StorySocial(Schema):
    comments = fields.Int()
    views = fields.Int()
    likes = fields.Int()
    shares = fields.Int()


class StoryMeta(Schema):
    publish_date = fields.DateTime()
    current_time = fields.DateTime()
    elapsed_time = fields.Str()


class StoryPhoto(Schema):
    image = fields.Str()
    caption = fields.Str()


class StoryContent(Schema):
    topic = fields.Str()
    headline = fields.Str()
    author = fields.Str()


class StorySite(Schema):
    url = fields.Str()


class StoryCore(Schema):
    meta = fields.Nested(StoryMeta())
    social = fields.Nested(StorySocial())
    photo = fields.Nested(StoryPhoto())
    content = fields.Nested(StoryContent())
    link = fields.Nested(StorySite())
