from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/mars_db'
mongo = PyMongo(app)
print(mongo.db)


@app.route("/")
def index():
    mars_data = mongo.db.mars_db.find_one()
    return render_template('index.html', db_data = mars_data)

@app.route("/scrape")
def scrape():
    #mars_data = mongo.db.mars_db.find_one()
    data = scrape_mars.scrape_all()
    mongo.db.mars_db.update({},data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)