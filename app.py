from flask import Flask,render_template,request,redirect
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
@app.route("/list",methods=["POST","GET"])
def list():
    obj  = ExpenseTracker()
    data = obj.list()#[{id=val,amount=val,cat=val,date=val},{...},{...}]
    return render_template("list.html",data = data)
@app.route("/modify",methods=["POST","GET"])
def modify():
    obj  = ExpenseTracker()
    if request.method == "POST":
        target_id = request.form.get("target_id")
        request_type = request.form.get("request-type")
        if request_type == "save-request":
            id = target_id
            category =  request.form.get("catego")
            note = request.form.get("note")
            obj.modify_category(id,category,note)
            return redirect("/list",code=302)
        else:
            print("the request type is:",request_type)
             # js return value as str always
            data = obj.list()#[{id=val,amount=val,cat=val,date=val},{...},{...}]
            print("the target id is ;",target_id)
            return render_template("modify.html",target_id=target_id,data=data)
@app.route("/delete/<int:id>")
def delete(id):
    obj = ExpenseTracker()
    obj.delete(id)
    return "ok"
@app.route("/delete-all",methods=["POST"])
def delete_all():
    obj = ExpenseTracker()
    obj.delete_all()
    return render_template("home.html")
@app.route("/summary")
def summary():
    obj = ExpenseTracker()
    data = obj.summary()
    return render_template("summary.html",data=data)#[(cat,amount),(cat,amount),...]

app.run()