from flask import Flask , render_template,request,flash,redirect,url_for

from flask_sqlalchemy import SQLAlchemy
from datetime import date ,datetime

app=Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expense.db"
app.config["SECRET_KEY"] = "my-secret-key"

db = SQLAlchemy(app)

class Expense (db.Model):
  id=  db.Column(db.Integer,primary_key=True)
  description=  db.Column(db.String(200),nullable=False)
  amount=  db.Column(db.Float,nullable=False)
  category=  db.Column(db.Integer)
  date=  db.Column(db.Date,nullable=False,default=date.today)



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    data=Expense.query.order_by(Expense.date.desc(),Expense.id.desc()).all()
    return render_template('index.html',data=data)


@app.route("/add",methods=['POST'])
def add():

    desc=request.form.get('desc')
    amount=request.form.get('amount')
    category=request.form.get('category')
    date_today=request.form.get('date')

    if not desc or not amount or not category or not date :
        flash("no fields can be empty","error")
    

    try :
        if int(amount)<0:
            raise ValueError
    
    except ValueError :
        flash("value cannot be less than zero","error")
        
    try :
        d=datetime.strptime(date_today,"%Y-%m-%d").date() if date_today else date.today()
    except ValueError:
        d=date.today()
    
    ex=Expense(description=desc,amount=amount,category=category,date=d)
    db.session.add(ex)
    db.session.commit()
    flash("Form submitted successfully")
    

    return redirect(url_for("home"))


if __name__== "__main__":
    app.run(debug=True)