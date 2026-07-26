#i have to create 4 function
from datetime import datetime
import sqlite3

#build a class called Expenstracker 
class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.table = self.cursor.execute("create table if not exists data(id integer primary key,amount integer,category text,note text,date text) ")


    def add(self, amount, category, note):
        date =  datetime.today().strftime( "%Y-%m-%d")
        self.cursor.execute("insert into data(amount,category,note,date) values (?,?,?,?)",(amount,category,note,date))
        self.conn.commit()
    def list(self):
        self.cursor.execute("select * from data")
        data = self.cursor.fetchall() #{(id,category,note,date),(id,catergory....)}
        info = []
        if data:
            for tuple_ in data:
                if tuple_:
                    dic =  {"id":tuple_[0],
                            "amount":tuple_[1],
                            "category":tuple_[2],
                            "note":tuple_[3],
                            "date":tuple_[4]}
                    info.append(dic)
           
         
            return info
                    #print(f"[{tuple_[0]:<3}]: {tuple_[1]:<5.1f}DH | {tuple_[2]:<12} | {tuple_[3]:<12} | {tuple_[4]}")
        else:
             return "you have no expenses yet ( ✜︵✜ )"
    def summary(self):
        info = []
        self.cursor.execute("select sum(amount) from data")
        amount_data = self.cursor.fetchall()#[(toatale,)]
        totale = amount_data[0][0]
        if totale == None:
            print("you have no expenses yet to summary( ✜︵✜ )")
            return
        self.cursor.execute("select category,sum(amount) from data group by category")#same need a hangling here
        data = self.cursor.fetchall()#[(cat,amount),(cat,amount),...]
        print("Totale spent:",totale)
        for element in data:
            print(element[0],element[1],"DH")
            info.append((element[0],element[1]))
        return info
    def delete(self,id):
        #if id does not exist do not stay silent
        rows_number = self.count_rows()
        if rows_number == 0:
            print("you have no expenses yet ! there is nothing to delete ( ✜︵✜ )")
            return
        self.cursor.execute("delete from data where id  = ? ",(id,))
        self.conn.commit()
        if rows_number == self.count_rows():
            print(f"the id [{id}] not found ! there is no expense with the id: [{id}]")
    def modify_category(self,id,new_category=None,new_note=None):
        #handle the case where the giving id is not found
        
        if new_category:
            self.cursor.execute("update data  set category = ? where id = ? ",(new_category,id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                print( f"the id: [{id}] is not found !")
        if new_note:
            self.cursor.execute("update  data set note = ? where id = ?",(new_note,id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                print(f"the id: [{id}] is not found !")
        if not new_category and not new_note:
            print("you have no expenses yet to modify")
       
    def delete_all(self):
        #for now this stay silent in succes and fealure cus it doesnt matter 
        self.cursor.execute("delete from data")
        self.conn.commit()
    def count_rows(self):
        self.cursor.execute("select count(*) from data")
        count = self.cursor.fetchall()#[(count,)]
        return count[0][0]
    


        
        
       
     