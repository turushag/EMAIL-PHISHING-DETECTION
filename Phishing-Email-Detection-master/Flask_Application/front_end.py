from flask import Flask, render_template
import sqlite3 as sql
app = Flask(__name__)
app.secret_key="randomstring"
con = sql.connect("D:/Projects/Phishing-email-detection/Flask_Application/email_db.db")
con.row_factory = sql.Row
cur = con.cursor()
cur.execute("select * from EMAIL")
# cur.execute("DELETE FROM EMAIL WHERE SL_NO=22")
con.commit()

rows = cur.fetchall(); 
@app.route('/')
def inbox():
    return render_template("inbox.html",rows = rows)

@app.route('/read_email/<int:id>') 
def read_email(id):
    con = sql.connect("D:/Projects/Phishing-email-detection/Flask_Application/email_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from EMAIL where SL_NO = ?",(id,))
    rows = cur.fetchone()
    print("id=",rows[0])
    # print("sender=",rows[1])
    # print("subject=",rows[2])
    # print("date=",rows[3])
    # print("mail-content=",rows[4])
    # print("phishing=",rows[5])

    return render_template("read_email.html",rows = rows)
	
if __name__ == '__main__':
   app.run(debug=True)
   
