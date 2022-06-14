from unicodedata import name
from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    name = 'Jan Dąbrowski'
    return render_template('index.html.jinja', name=name)


@app.route('/author')
@app.route('/templates/author')
def author():
    index_number = '222944'
    field_of_study = 'Applied Informatics'
    return render_template('author.html.jinja', index_number=index_number, field_of_study=field_of_study)

@app.route("/extract")
def extract():
    return render_template("extract.html.jinja")

@app.route("/products")
def products():
    return render_template("products.html.jinja")

@app.route("/product/<product_id>")
def product():
    return render_template("product.html.jinja")

@app.route("/opinions")
def opinions():
    return render_template("opinions.html.jinja")