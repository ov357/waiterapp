from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "under construction"
	
if __name__ == '__main__':
	app_run(port = 5000, debug = True)
	
