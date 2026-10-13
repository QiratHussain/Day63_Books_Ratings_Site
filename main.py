from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/add", methods= ['POST','GET'])
def add():
    if request.method=='POST':
        new_book= {'Title':request.form['title'], 'Author':request.form['author'], 'Rating':request.form['rating']}
        all_books.append(new_book)
        return  render_template("index.html", books_list= all_books)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

