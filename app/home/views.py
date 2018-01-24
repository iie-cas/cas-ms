#coding=utf-8


from . import home
from flask import render_template, redirect, url_for, session, request, flash, jsonify
from functools import wraps
from app import getConn


def home_login_req(f):
    """
    访问控制装饰器
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'account' not in session:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@home.route('/')
def index():
    # 渲染并返回 home/index.html 页面
    return render_template('home/index.html')


@home.route('/login/', methods=['GET', 'POST'])
def login():
    """
    用户登录
    """
    if request.method == 'POST':
        account = request.form.get('account')
        password = request.form.get('password')
        db = getConn()
        cursor = db.cursor()
        sql = '''select id, account, password, username from user where account="%s"''' %account
        try:
            value = None
            cursor.execute(sql)
            value = cursor.fetchone()
        except:
            print('[Error][login]: unable to fetch data')
        if not value:  # 判断用户是否存在
            return jsonify({'message': u'用户名不存在'})
        else:
            columns = ('id', 'account', 'password', 'username')
            user = dict(zip(columns, value))
            if user['password'] == password:  # 判断密码是否正确
                for key in user:
                    session[key] = user[key]
                return jsonify({'message': ''})
            else:
                return jsonify({'message': u'密码错误'})
        db.close()
    else:
        return render_template('home/login.html')
 

@home.route('/logout/')
@home_login_req
def logout():
    """
    用户退出
    """
    columns = ('id', 'account', 'password', 'username')
    for column in columns:
        session.pop(column, None)
    # 重定向到登录页面
    return redirect(url_for('home.login'))

@home.route('/user/', methods=['GET', 'POST'])
@home_login_req
def user():
    if request.method == 'POST':
        user_id = request.form.get("id")
        tel = request.form.get("tel")
        qq = request.form.get("qq")
        status = True
        db = getConn()
        cursor = db.cursor()
        sql = '''update user set telephone="%s", qq="%s" where id="%s"''' %(tel, qq, user_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            status = False
        db.close()
        return jsonify({"status": status})
    else:
        account = session['account']
        db = getConn()
        cursor = db.cursor()
        sql = '''select id, account, password, username, education, grade, score, fund, telephone, qq from user
                 where account="%s"''' %account
        try:
            user = None
            cursor.execute(sql)
            user = cursor.fetchone()
        except:
            pass
        columns = ('id', 'account', 'password', 'username', 'education', 'grade', 'score', 'fund', 'telephone', 'qq')
        user = dict(zip(columns, user))
        for key in user:
            if user[key] is None:
                user[key] = u"待录入"
        return render_template('home/user.html', user=user)  


@home.route('/pwd/')
@home_login_req
def pwd():
    """
    修改密码
    """
    return render_template('home/pwd.html')


@home.route('/score/')
@home_login_req
def score():
    """
    得分记录页面
    """
    return render_template('home/score.html')


@home.route('/fund/')
@home_login_req
def fund():
    """
    额度记录页面
    """
    return render_template('home/fund.html')
