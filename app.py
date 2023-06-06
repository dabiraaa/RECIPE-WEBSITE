from flask import Flask, render_template
app = Flask(__name__)
#this defines the entry point
@app.route("/")
def home():
    return render_template("kitchen.jpg")
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/jollof")
def jollof():
    return render_template("jollof.html")
@app.route("/stew")
def stew():
    return render_template("stew.html")
@app.route("/egusi")
def egusi():
    return render_template("egusi.html")
@app.route("/efo")
def efo():
    return render_template("efo.html")
@app.route("/puffpuff")
def puffpuff():
    return render_template("puffpuff.html")
#runs the web server and app
if __name__ == '__main__':
    app.run(debug=True)





