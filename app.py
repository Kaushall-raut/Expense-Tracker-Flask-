from flask import Flask , render_template,request,flash,redirect,url_for

from flask_sqlalchemy import SQLAlchemy
from datetime import date ,datetime
from sqlalchemy import func

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


def date_parser(s:str):

    if not s:
        return None
    try:
        return datetime.strptime(s,"%Y-%m-%d").date()
    except ValueError:
        return None
    

@app.route("/")
def home():


    start_Str=(request.args.get("start") or "".strip())
    end_Str=(request.args.get("end") or "".strip())
    selected_category=(request.args.get("selected_category") or "".strip())

    start_date=date_parser(start_Str)
    end_date=date_parser(end_Str)
    today= date.today().isoformat()
    
    if start_date and end_date and end_date<start_date:
        flash("end date cannot be before start date","error")
        start_date=end_date=None
        start_Str=end_Str=""
    

    q=Expense.query
    if start_date :
        q=q.filter(Expense.date>=start_date)
    if end_date:
      q=q.filter(Expense.date <= end_date)
    if selected_category:
        q=q.filter(Expense.category == selected_category)

    category=['Food','Transport',"Rent",'Utilities','Health']
    data=q.order_by(Expense.date.desc(),Expense.id.desc()).all()
    total = round(sum(t.amount for t in data),2)

    cat_q=db.session.query(Expense.category,func.sum(Expense.amount))

    if start_date:
        cat_q=cat_q.filter(Expense.date >= start_date)
    if end_date:    
        cat_q=cat_q.filter(Expense.date >= end_date)
    if selected_category :
        cat_q=cat_q.filter(Expense.category == selected_category)

    cat_rows=cat_q.group_by(Expense.category).all()
    cat_labels=[c for c , _ in cat_rows]
    cat_values=[round(float(s),2) for _ , s in cat_rows]


    daily_chart=db.session.query(Expense.date,func.sum(Expense.amount))

    if start_date:
        daily_chart=daily_chart.filter(Expense.date >= start_date)
    if end_date:    
        daily_chart=daily_chart.filter(Expense.date >= end_date)
    if selected_category :
        daily_chart=daily_chart.filter(Expense.category == selected_category)

    day_rows=daily_chart.group_by(Expense.category).order_by(Expense.date).all()
    print("daily",day_rows)
    day_labels=[d.isoformat() for d , _ in day_rows]
    day_values=[round(float(s),2) for _ , s in day_rows]
    

    return render_template('index.html',data=data ,category=category ,total=total ,start_Str=start_Str , end_Str=end_Str,today=today , selected_category=selected_category, cat_labels=cat_labels , cat_values=cat_values ,day_labels=day_labels,day_values=day_values)


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


@app.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    e=Expense.query.get_or_404(id)
    db.session.delete(e)
    print(e)
    db.session.commit()
    flash("Deleted successfully","success")

    return redirect(url_for("home"))


if __name__== "__main__":
    app.run(debug=True)