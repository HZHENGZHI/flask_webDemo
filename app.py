from flask import Flask, Response
from flask import *
import pymysql
import json
DBhost='127.0.0.1'
DBuser='root'
DBpass='123456'
DBname='python'

app = Flask(__name__)
def select(time):
    db = pymysql.connect('localhost', 'root', '123456','python')
    cursor = db.cursor()
    sql = "SELECT * FROM stu_score where (term_time)=('%s')" % (time)
    cursor.execute(sql)
    result = cursor.fetchall()
    key = ('id', 'subject', 'score', 'gap', 'pass_or_no', 'term_time')
    dict1 = [dict(zip(key, value)) for value in result]
    return dict1
def login(id,pw):
    db = pymysql.connect('localhost', 'root', '123456', 'python')
    cursor = db.cursor()
    sql = "SELECT * FROM user where (id,pw)=('%s','%s')" % (id,pw)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
@app.route('/')
def hello_world():
    # return Response(json.dumps(dict1),mimetype='application/json')
    return render_template("index_three.html")

@app.route('/center',methods=['POST','GET'])#等同于127.0.0.1/center
def center():
    id=request.form.get("id")
    print(id)
    pwd=request.form.get("pwd")
    print(pwd)
    dict1=login(id,pwd)
    if(dict1):
        s="登陆成功"
        return render_template("index_two.html",data=s)
    else:
        s="登陆失败"
        return render_template("index.html",data=s)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lodin',methods=['POST','GET'])
def lodin():
    years=request.form.get("years")
    print(years)
    dict=select(years)
    print(dict)
    if(dict):
        return render_template("index_two.html",data=dict,value1=years)
if __name__ == '__main__':
    app.run(debug=1,port=5000,host='0.0.0.0')
