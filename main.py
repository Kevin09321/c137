from flask import Flask, jsonify
from flask.wrappers import Request
from data import data
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data": data, 
        "message": "succes"
            }),200
@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data": planet_data, 
        "message": "succes"
            }),200
if __name__ == "__main__":
    app.run()
