# coding=utf8


from . import admin
from flask import render_template, redirect, url_for, request, jsonify, session, flash
from app import getConn
from functools import wraps
import re


def admin_login_req(f):
    """
    访问控制装饰器
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'is_super' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    """
    管理员登录
    """
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        # 建立数据库连接、查询账户名是否存在
        with getConn() as cursor:
            cursor.execute(
                '''
                select * from admin where account="%s"
                ''' %account
            )
        value = cursor.fetchone()
        if not value:
            # 用户名不存在
            flash(u'用户名不存在')
        else:
            # 用户名存在
            columns = ('id', 'account', 'password', 'username', 'is_super', 'create_time')
            user = dict(zip(columns, value))
            # 检查密码是否正确
            if user['password'] == password:
                # 密码正确，将用户信息加入 session
                for key in user:
                    session[key] = user[key]
                # 重定向到主页
                return redirect(url_for('admin.index'))
            else:
                # 密码不正确
                flash(u'密码错误')
    # 如果是 GET 请求，则会直接返回 admin/login.html
    return render_template('admin/login.html')


@admin.route('/logout/')
@admin_login_req
def logout():
    """
    管理员退出
    """
    keys = ('id', 'account', 'password', 'username', 'is_super', 'create_time')
    for key in keys:
        # Flask 中的 session 基于字典类型实现，调用 session.pop() 方法时会返回调用时传入的键对应的值，如果键并不存在，那么返回第二个参数 
        session.pop(key, None)
    # 重定向到登录页面
    return redirect(url_for('admin.login'))


@admin.route('/')
@admin_login_req
def index():
    """
    后台主页
    """
    # 建立数据库连接、查询 user 表信息
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, score, fund from user
            '''
        )
        users = []
        columns = ('id', 'account', 'username', 'score', 'fund')
        for item in cursor.fetchall():
            users.append(dict(zip(columns, item)))
    # 返回 admin/index.html，并返回 users 列表信息
    return render_template('admin/index.html', users = users)


@admin.route('/user/add/', methods=['GET', 'POST'])
@admin_login_req
def user_add():
    """
    添加成员
    """
    if request.method == 'POST':
        account = request.form['account']
        # 判断 account 字段是否已经存在 
        with getConn() as cursor:
            cursor.execute(
                '''
                select * from user where account="%s"
                ''' %account
            )
            value = cursor.fetchone()
        if value:
            flash(u'账号已存在')
        username = request.form['username']
        password = request.form['password']
        score = int(request.form['score'])
        fund = int(request.form['fund'])
        edu_map = {
            1: u'学硕',
            2: u'专硕',
            3: u'博士'
        }
        education = edu_map[int(request.form['education'])]
        # 将数据插入数据库中
        with getConn() as cursor:
            cursor.execute(
                '''
                insert into user(account, username, password, education, score, fund) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
                ''' %(account, username, password, education, score, fund)
            )
        # 重定向到 user_list.html 页面
        return redirect(url_for('admin.user_list'))
    # 渲染并返回 admin/user_add.html 页面
    return render_template('admin/user_add.html')


@admin.route('/user/list/')
@admin_login_req
def user_list():
    """
    成员列表
    """
    # 建立数据库连接、查询 user 表信息
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, education, grade, telephone, qq from user
            '''
        )
        users = []
        columns = ('id', 'account', 'username', 'education', 'grade', 'telephone', 'qq')
        for item in cursor.fetchall():
            users.append(dict(zip(columns, item)))
    # 渲染并返回 admin/user_list.html 页面
    return render_template('admin/user_list.html', users=users)


@admin.route('/score/edit/<int:user_id>/', methods=['GET', 'POST'])
@admin_login_req
def score_edit(user_id=None):
    """
    修改分数
    user_id: 用户id
    """
    if request.method == 'POST':
        current_score = int(request.form['current_score'])
        option = int(request.form['option'])
        edit_score = int(request.form['edit_score'])
        reason = request.form['reason']
        if option == 2:
            # 如果是减分操作
            edit_score = -edit_score
        score = current_score + edit_score
        with getConn() as cursor:
            # 更新 user 表
            if option == 1:
                # 如果是加分操作，那么同时增加额度
                cursor.execute(
                    '''
                    update user set fund=fund + %s, score="%s" where id="%s"
                    ''' %(edit_score, user_id)
                )
                # 增加了额度，就要同步更新 fundlog 表
                edit_fund = edit_score
                cursor.execute(
                    '''
                    insert into fundlog(user_id, value, reason) values ("%s", "%s", "%s")
                    ''' %(user_id, edit_fund, reason)
                )
            else:
                # 如果是减分操作，那么只更新分数
                cursor.execute(
                    '''
                    update user set score="%s" where id="%s"
                    ''' %(score, user_id)
                )
            # 更新 scorelog 表
            cursor.execute(
                '''
                insert into scorelog(user_id, value, reason) values ("%s", "%s", "%s")
                ''' %(user_id, edit_score, reason)
            )
            # 重定向到 amdin/index.html 页面
            return redirect(url_for('admin.index'))
    # 如果发起的是 GET 请求，那么会直接执行以下代码
    with getConn() as cursor:
        # 查询 user 表信息
        cursor.execute(
            '''
            select id, account, username, score from user where id="%s"
            ''' %user_id
        )
        user = cursor.fetchone()
        columns = ('id', 'account', 'username', 'score')
        user = dict(zip(columns, user))
        # 查询 score_label 表内容
        cursor.execute(
            '''
            select * from score_label
            '''
        )
        columns = ('id', 'name')
        labels = []
        for item in cursor.fetchall():
            labels.append(dict(zip(columns, item)))
    # 渲染并返回 score_edit.html 页面
    return render_template('admin/score_edit.html', labels=labels, user=user)


@admin.route('/fund/edit/<int:user_id>/', methods=['GET', 'POST'])
@admin_login_req
def fund_edit(user_id=None):
    """
    修改额度
    user_id: 用户id
    """
    if request.method == 'POST':
        current_fund = int(request.form['current_fund'])
        option = int(request.form['option'])
        edit_fund = int(request.form['edit_fund'])
        reason = request.form['reason']
        if option == 2:  # 减少额度
            edit_fund = -edit_fund
        fund = current_fund + edit_fund
        with getConn() as cursor:
            # 更新 user 表
            cursor.execute(
                '''
                update user set fund="%s" where id="%s"
                ''' %(fund, user_id)
            )
            # 更新 fundlog 表            
            cursor.execute(
                '''
                insert into fundlog(user_id, value, reason) values ("%s", "%s", "%s")
                ''' %(user_id, edit_fund, reason)
            )
        # 重定向到 admin/index.html 页面
        return redirect(url_for('admin.index'))
    # 如果为 GET 请求，则会直接执行以下代码
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, fund from user where id="%s"
            ''' %user_id
        )
        user = cursor.fetchone()
        columns = ('id', 'account', 'username', 'fund')
        user = dict(zip(columns, user))
    # 渲染并返回 fund_edit.html 页面
    return render_template('admin/fund_edit.html', user=user)


@admin.route('/user/delete/<int:user_id>/', methods=['GET', 'POST'])
@admin_login_req
def user_delete(user_id=None):
    """
    删除用户
    user_id: 用户id
    """
    with getConn() as cursor:
        cursor.execute(
            '''
            delete from user where id="%s" 
            ''' %user_id
        )
    return redirect(url_for('admin.user_list'))


@admin.route('/pwd/', methods=['GET', 'POST'])
@admin_login_req
def pwd():
    """
    修改管理员密码
    """
    if request.method == 'POST':
        user_id = request.form['user_id']
        old_password = request.form['old_password']
        # 验证输入的旧密码是否正确
        with getConn() as cursor:
            cursor.execute(
                '''
                select password from admin where id="%s"
                ''' %user_id
            )
            password = cursor.fetchone()
            if old_password != password:
                flash("旧密码错误")
        new_password = request.form['new_password1']
        with getConn() as cursor:
            cursor.execute(
                '''
                update admin set password="%s" where id="%s"
                ''' %(new_password, user_id)
            )
            # 重定向到 admin/index.html 页面
            return redirect(url_for('admin.index'))
    # 渲染并返回 admin/pwd.html 页面
    return render_template('admin/pwd.html')
