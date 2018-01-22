#coding=utf-8


from . import home
from flask import render_template, redirect, url_for, session, request, redirect, flash
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
        account = request.form['account']
        password = request.form['password']
        with getConn() as cursor:
            cursor.execute(
                '''
                select * from user where account="%s"
                ''' %account
            )
        value = cursor.fetchone()
        if not value:
            # 判断用户名是否存在
            flash(u'用户名不存在')
        else:
            columns = ('id', 'account', 'password', 'username')
            user = dict(zip(columns, value))
            if user['password'] == password:
                # 判断密码是否正确
                for key in user:
                    session[key] = user[key]
                return redirect(url_for('home.user'))
            else:
                flash(u'密码错误')
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
        # 如果用户修改了个人信息，会发送 POST 请求 
        pass
    # 如果是 GET 请求，则会直接执行以下代码
    account = session['account']
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, password, username, education, grade, score, fund, telephone, qq from user where account="%s"
            ''' %account
        )
        user = cursor.fetchone()
        columns = ('id', 'account', 'password', 'username', 'education', 'grade', 'score', 'fund', 'telephone', 'qq')
        user = dict(zip(columns, user))
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
