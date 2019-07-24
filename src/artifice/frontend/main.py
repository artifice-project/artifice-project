from flask import Flask, request, render_template, url_for

app = Flask(__name__)

schema = {
    "headline" : "fake news causing unrest amongst low-education voters",
    "author" : "john e. doe",
    "timestamp" : "July 23, 2019",
    "caption" : "an image shows several people talking to a reporter in a small town.",
    "article" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
}

@app.route("/")
def home():
    global schema
    schema["headline"] = schema["headline"].title()
    schema["author"] = schema["author"].title()
    schema["caption"] = schema["caption"].capitalize()
    return render_template("index.html", schema=schema)

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=11000,
        debug=True
    )
