# coding: utf8
from . import home
from flask import render_template, redirect, url_for, session, request, redirect, flash
from functools import wraps
from app import getConn


@home.route('/')
def index():
    return render_template('home/index.html')


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


@home.route('/login/', methods=['GET', 'POST'])
def login():
    """
    用户登录
    """
    user_columns = ('id', 'account', 'password', 'username')
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        with getConn() as cursor:
            cursor.execute(
                '''
                select * from user where account="%s"
                ''' %account)
        value = cursor.fetchone()
        if not value:
            flash(u'用户名不存在')
        else:
            user_dict = dict(zip(user_columns, value))
            if user_dict['password'] == password:
                for key in user_dict:
                    session[key] = user_dict[key]
                return redirect(url_for('home.user'))
            else:
                flash(u'密码错误')
    return render_template('home/login.html')
 

@home.route('/logout/')
@home_login_req
def logout():
    # 重定向到 home 模块下的 login 视图
    user_columns = ('id', 'account', 'password', 'username')
    for column in user_columns:
        session.pop(column, None)
    return redirect(url_for('home.login'))

@home.route('/user/', methods=['GET', 'POST'])
@home_login_req
def user():
    if request.method == 'POST':
        pass
    account = session['account']
    columns = ('id', 'account', 'password', 'username', 'education', 'grade', 'score', 'fund', 'telephone', 'qq', 'adm_time')
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, password, username, education, grade, score, fund, telephone, qq, adm_time from user where account="%s"
            ''' %account)
        user = cursor.fetchone()
    user = dict(zip(columns, user))
    for key in user:
        if not user[key]:
            user[key] = u'待录入'
    return render_template('home/user.html', user=user)  

@home.route('/pwd/')
@home_login_req
def pwd():
   return render_template('home/pwd.html')

# 得分记录页面
@home.route('/score/')
@home_login_req
def score():
   return render_template('home/score.html')

# 额度记录页面
@home.route('/fund/')
@home_login_req
def fund():
   return render_template('home/fund.html')
