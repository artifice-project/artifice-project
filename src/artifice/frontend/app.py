from flask import Flask, request, render_template, url_for

app = Flask(__name__)

def get_schema():
    schema = {
        "story_id" : "#",
        "headline" : "fake news causing unrest amongst low-education voters",
        "author" : "john e. doe",
        "timestamp" : "July 23, 2019",
        "caption" : "an image shows several people talking to a reporter in a small town.",
        "byline" : "a bit of text that gives a short summary of the content within the article.",
        "article" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    }
    schema["headline"] = schema["headline"].title()
    schema["author"] = schema["author"].title()
    schema["caption"] = schema["caption"].capitalize()
    schema["byline"] = schema["byline"].capitalize()
    return schema

@app.route("/")
def home():
    schemas = [get_schema() for _ in range(3)]
    return render_template("navbar.html", schemas=schemas)
