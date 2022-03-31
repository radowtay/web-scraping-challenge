from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


#create flask app instance
app=Flask(__name__)
#connection variable
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# #variables
#create route
# @app.route("/")
# def echo():
#     return render_template("index.html",
#     # news_title=news_title,
#     # news_blurb=news_blurb,
#     # featured_image_url=featured_image_url,
#     # mars_html_table=mars_html_table,
#     hemispheres=hemispheres

#     )

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_stuff=mongo.db.mars_stuff.find_one()


    # Return template and data
    return render_template("index.html", mars_stuff=mars_stuff)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_stuff=mongo.db.mars_stuff
    data = scrape_mars.scrape()
    mars_stuff.update_one(
            {"$set": data},
            upsert=True
        )
    return redirect("/")






if __name__ =="__main__":
    app.run(debug=True)