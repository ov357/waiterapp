from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "under contstruction"

if __name__ == '__main__':
    app.run(port=8001, debug = True)
