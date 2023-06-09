from flask import Flask
from flask_cors import CORS
from scraper import get_products

app = Flask(__name__)
CORS(app)

@app.route("/search/<category>/<name>")
def searchProduct(category, name):
    return get_products(name, category)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)