from flask import Flask, render_template, request, url_for, redirect, session
import pymysql

app = Flask(__name__) # __name__代表目前執行的模組
app.config['SECRET_KEY'] = b'\x8f\xef\xa5\xba#8.9\xa5A]\xdd\xc4\x1b\x8d\x0c'
conn = pymysql.connect(host='localhost',user='root',password='',db='website',charset='utf8')
cur = conn.cursor()

@app.route("/") # 函式的裝飾(Decorater):以函式為基礎，提供附加的功能
def index():
    session.clear()
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def signup():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = request.form['username'] 

    if request.method == 'POST':
        # 阻擋空白欄位
        if name == "" or username == "" or password == "": 
            return redirect(url_for('error', message='請填寫所有欄位'))
        # 搜尋資料庫，阻擋已存在帳號
        sql = "SELECT * FROM member WHERE username = %s"
        params = username
        cur.execute(sql, params)
        data = cur.fetchone()        
        if not data == None:
            session.pop('username', None)
            return redirect(url_for('error', message='帳號已經被註冊'))
        sql_insert = "INSERT INTO member(name,username,password)VALUES(%s, %s, %s)" 
        params_insert = (name, username, password)
        cur.execute(sql_insert, params_insert)
        conn.commit() 
        # 存入資料庫後清除session回到首頁重新登入
        session.pop('username', None)
        return render_template("index.html")


@app.route("/signin", methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = request.form['username'] 

    if request.method == 'POST':
        # 阻擋空白帳密
        if username == "" and password == "":
            # 清除錯誤session避免直接更改URL
            session.pop('username', None)
            return redirect(url_for('error', message='請輸入帳號、密碼'))
        # 搜尋資料庫，判斷帳號是否存在
        sql = "SELECT name,username,password FROM member WHERE username = %s"
        params = username
        cur.execute(sql, params)
        data = cur.fetchone()
        if data == None:
            # 清除錯誤session避免直接更改URL
            session.pop('username', None)
            return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))
        # 判斷對應密碼是否正確
        mypwd=data[2] # 輸入的帳號對應的密碼位置 SELECT X,X,password....
        # print(mypwd)
        if (mypwd != password):
            # 清除錯誤session避免直接更改URL
            session.pop('username', None)
            return redirect(url_for('error', message='密碼輸入錯誤'))
        else:
            return redirect(url_for("member"))                       
    else: 
        return render_template("index.html")


@app.route("/member") 
def member():   
    if "username" in session:
        print(f'Signed in as {session["username"]}')
        username = session["username"]
        sql = "SELECT name,username FROM member WHERE username = %s"
        params = username
        cur.execute(sql, params)
        data = cur.fetchone()
        myname = data[0]

        # 顯示message所有聊天內容
        sql = "SELECT name, content FROM message INNER JOIN member ON member.id=message.member_id ORDER BY message.time DESC"
        cur.execute(sql)
        data = cur.fetchall() 
        return render_template("member.html",name=myname,data=data)
    else:
        return render_template("index.html")



@app.route("/message", methods=['POST'])
def message():
    # 每按一次"送出"存進一筆資料
    # 根據登入時在Session 紀錄的使⽤者編號，將留⾔內容紀錄到 message 資料表。
    content = request.form.get('content')
    if request.method == 'POST':
        if "username" in session:
            sql = "SELECT id, name,username FROM member WHERE username = %s"
            params = session['username']
            cur.execute(sql,params)
            data = cur.fetchone() 
            myid = data[0]
            sql_insert = "INSERT INTO message(member_id,content)VALUES('%s', '"+ content + "')" 
            params_insert = (myid)
            cur.execute(sql_insert, params_insert)
            conn.commit()
        return redirect(url_for("member")) 

@app.route("/signout", methods=['GET'])
def signout():
    print(f'Signed out as {session["username"]}')
    session.clear() # 刪除所有
    return render_template("index.html")

@app.route("/signagain", methods=['GET'])
def signagain():
    session.clear()
    return render_template("index.html")


@app.route("/error") 
def error():
    session.clear()
    return render_template('error.html')


if __name__=="__main__": # 如果以主程式執行
    app.run(port=3000) # 立刻啟動伺服器

