from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__) # __name__代表目前執行的模組
app.config['SECRET_KEY'] = b'\x8f\xef\xa5\xba#8.9\xa5A]\xdd\xc4\x1b\x8d\x0c'

@app.route("/") # 函式的裝飾(Decorater):以函式為基礎，提供附加的功能
def index():
    session.clear()
    return render_template('index.html')

@app.route("/signin", methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = request.form['username'] 

    if request.method == 'POST':            
            if username == "" and password == "":
                session.pop('username', None)
                return redirect(url_for('error', message='請輸入帳號、密碼'))
            if username != 'test' or password != 'test':
                session.pop('username', None)
                return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))            
            return redirect(url_for("member"))
            # return render_template("member.html")                        
    else: 
        return render_template("index.html")


@app.route("/member") 
def member():
    if "username" in session:
        print(f'Signed in as {session["username"]}')
        username = session["username"]
        return render_template("member.html",username=username)
    else:
        return render_template("index.html")
    

@app.route("/signout", methods=['GET'])
def signout():
    print(f'Signed out as {session["username"]}')

    # remove the username from the session if it's there
    # session.pop('username', None) # 刪除某一個key
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

