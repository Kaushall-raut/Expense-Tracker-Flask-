from flask import Flask , render_template

from flask_sqlalchemy import SQLAlchemy
from datetime import date

app=Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expense.db"

db = SQLAlchemy(app)

class Expense (db.Model):
  id=  db.Column(db.Integer,primary_key=True)
  description=  db.Column(db.String(200),nullable=False)
  amount=  db.Column(db.Float,nullable=False)
  category=  db.Column(db.Integer,Primary_key=True)
  date=  db.Column(db.Date,nullable=False,default=date.today())



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('index.html')



if __name__== "__main__":
    app.run(debug=True)