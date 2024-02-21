from flask import Flask, render_template ,request,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    
    con = sql.connect('users.db')
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    return render_template('index.html',users=users)  
       
@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        Nname=request.form['nname']
        Nemail=request.form['nemail']
        con = sql.connect('users.db')
        con.row_factory=sql.Row
        cur = con.cursor()
        cur.execute('INSERT INTO users (NAME,EMAIL) values (?,?) ',(Nname,Nemail))
        con.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route("/update/<string:id>",methods=['POST','GET'])
def update(id):
    if request.method=='POST':
        Newname=request.form['newname']
        Newemail=request.form['newemail']
        con = sql.connect('users.db')
        con.row_factory=sql.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET NAME =?,EMAIL =? WHERE ID =?",(Newname,Newemail,id,))
        con.commit()
        return redirect(url_for('index'))
    
    #SPECIFY THE ROW THAT YOU WANNA UPDATE
    con = sql.connect('users.db')
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE ID = ? ',(id))
    users = cur.fetchone()
    return render_template('update.html' , users=users)

@app.route('/delete/<string:id>',methods=['POST','GET'])
def delete(id):
    con = sql.connect('users.db')
    con.row_factory=sql.Row
    cur = con.cursor()
    cur.execute('DELETE FROM users WHERE ID=?',(id))
    con.commit()
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True)
