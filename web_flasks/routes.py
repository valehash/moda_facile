from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hompage():
    """loads the homepage"""
    
    return "Homepage space"
    #return render_template("home.html")

@app.route("/cart", strict_slashes=False)
def cart_page():
    return "cartpage space"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)

