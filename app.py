from flask import Flask,render_template,request
from tracker import ExpenseTracker
app = Flask(__name__)
@app.route("/home",methods=["POST","GET"]) # it need post!
def home():
    return  render_template("home.html")
@app.route("/add",methods=["POST","GET"])
def add():
    obj  = ExpenseTracker()
    if request.method == "POST":
        amount = request.form.get("amount")
        catego = request.form.get("cat")
        note= request.form.get("note")
        obj.add(amount,catego,note)
    return render_template("add.html")
    
@app.route("/list")
def list():
    obj  = ExpenseTracker()
    data = obj.list()#[{id=val,amount=val,cat=val,date=val},{...},{...}]
    return render_template("list.html",data = data)
@app.route("/modify",methods=["GET","POST"])
def modify():
    obj  = ExpenseTracker()
    if request.method == "POST":
        id =request.form.get("id")
        category=request.form.get("category")
        note=request.form.get("note")
        obj.modify_category(id,category,note)
    return render_template("modify.html")
@app.route("/delete/<int:e_id>",methods=["POST","GET"])
def delete(e_id):
    if request.method == "GET":
        obj = ExpenseTracker()
        obj.delete(e_id)
    return render_template("home1.html") 
    
@app.route("/delete-all",methods=["POST"])
def delete_all():
    obj = ExpenseTracker()
    obj.delete_all()
    return render_template("home1.html")

@app.route("/summary")
def summary():
    obj = ExpenseTracker()
    data = obj.summary()
    return render_template("summary.html",data=data)
app.run()