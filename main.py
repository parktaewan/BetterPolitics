from flask import Flask, render_template, jsonify, request
import pymongo

conn = pymongo.MongoClient()
db = conn.BetterPolitics
db_pg = db.politician

app = Flask(__name__,
            static_url_path='',
            static_folder='front',
            template_folder="front")

@app.route("/")
def main_page():
    return render_template("{}.html".format("index"))

@app.route("/search")
def search():
    keyword = request.args.get("search")
    
    key = db_pg.find_one({"name" : keyword})
    if key == None:
        return render_template("search.html", name = None)
    return render_template("search.html", name = key["name"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)