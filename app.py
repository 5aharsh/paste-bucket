from flask import Flask, request, jsonify, render_template, url_for, send_from_directory
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
	return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
	user = request.form["username"]
	file = request.files["code"]
	os.makedirs(os.path.join(app.instance_path, user), exist_ok=True)
	file.save(os.path.join(app.instance_path, user, secure_filename(file.filename)))
	return jsonify({"status": "success", "user": user})

@app.route("/fetch/<username>/<file>")
def fetch(username, file):
	return send_from_directory(os.path.join(app.instance_path, username), file)

@app.route("/view")
def show():
	return render_template("fetch.html")

@app.route("/upload")
def upload():
	return render_template("upload.html")

if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)
