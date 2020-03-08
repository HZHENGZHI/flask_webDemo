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
    dict1=select("2018")
    return Response(json.dumps(dict1),mimetype='application/json')
@app.route('/center',methods=['POST','GET'])#等同于127.0.0.1/center
def center():
    id=request.form.get("id")
    print(id)
    pwd=request.form.get("pwd")
    print(pwd)
    dict1=login(id,pwd)
    s=0;
    dict2=select(id)
    if(dict2):
        return Response(json.dumps(dict2), mimetype='application/json')
    else:
        s="登陆失败"
        return render_template("index.html",data=s)


if __name__ == '__main__':
    app.run(debug=True)
