

class StoryBase(object):
    """ standard core story object """
    def __init__( self,
                schema=None,
                category=None,
                headline=None,
                timestamp=None,
                interactions=None,
                author=None,
                image=None ):
        self.schema = schema
        self.category = category
        self.headline = headline
        self.timestamp = timestamp
        self.interactions = interactions
        self.author = author
        self.image = image


class StorySplash(StoryBase):
    """docstring for StoryDetail."""

    def __init__( self,
                schema=None,
                category=None,
                headline=None,
                timestamp=None,
                interactions=None,
                author=None,
                image=None,
                text=None ):
        self.schema = schema
        self.category = category
        self.headline = headline
        self.timestamp = timestamp
        self.interactions = interactions
        self.author = author
        self.image = image
        self.text = text


B = StoryBase(
    schema="@base",
    category="Politics",
    headline="This Just In: Events Occur",
    timestamp="July 26, 2019",
    interactions="69",
    image="hello",
    author="Admin"
)

S = StorySplash(
    schema="@splash",
    category="Sports",
    headline="A Story You Want To Read",
    timestamp="July 24, 2019",
    interactions="420",
    image="world",
    author="Admin",
    text="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
)
