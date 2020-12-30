from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)
app.config["Mongo_URI"] = 'mongodb://localhost:27017/mars_db'
mongo = pymongo(app)

@app.route("/")
def index():
    mars_data = db.collection.find_one()
    return render_template('index.html', list = mars_data)

@app.route("/scrape")
def scrape():
    scrape.scrape_all()
    scrape.insert_into_mongo()
    return redirect("/")