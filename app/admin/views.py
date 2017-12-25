# coding: utf8
from . import admin
from flask import render_template, redirect, url_for, request, jsonify, session, flash
from app import getConn
from functools import wraps


def admin_login_req(f):
    """
    访问控制装饰器
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'account' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    """
    管理员登录
    """
    admin_columns = ('id', 'account', 'password', 'username', 'is_super', 'create_time')
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        with getConn() as cursor:
            cursor.execute(
                '''
                select * from admin where account="%s"
                ''' %account)
        value = cursor.fetchone()
        if not value:
            flash(u'用户名不存在')
        else:
            user_dict = dict(zip(admin_columns, value))
            if user_dict['password'] == password:
                for key in user_dict:
                    session[key] = user_dict[key]
                return redirect(url_for('admin.index'))
            else:
                flash(u'密码错误')
    return render_template('admin/login.html')


@admin.route('/logout/')
@admin_login_req
def logout():
    """
    管理员退出
    """
    admin_columns = ('id', 'account', 'password', 'username', 'is_super', 'create_time')
    for column in admin_columns:
        session.pop(column, None)
    return redirect(url_for('admin.login'))


@admin.route('/')
@admin_login_req
def index():
    """
    后台主页
    """
    user_columns = ('id', 'account', 'username', 'score', 'fund')
    users = []
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, score, fund from user
            ''')
        for item in cursor.fetchall():
            users.append(dict(zip(user_columns, item)))
    return render_template('admin/index.html', users = users)


@admin.route('/user/add/', methods=['GET', 'POST'])
@admin_login_req
def user_add():
    """
    添加成员
    """
    if request.method == 'POST':
        account = request.form['account']
        username = request.form['username']
        password = request.form['password']
        score = request.form['score']
        fund = request.form['fund']
        education = int(request.form['education'])
        grade = u'待录入'
        telephone = u'待录入'
        qq = u'待录入'
        adm_time = u'待录入'
        if account == '':
            flash(u'账号不能为空')
        elif username == '':
            flash(u'姓名不能为空')
        else:
            with getConn() as cursor:
                cursor.execute(
                    '''
                    select * from user where account="%s"
                    ''' %account)
                value = cursor.fetchone()
            if value:
                flash(u'账号已存在')
            else:
                if education == 1:
                    education = u'学硕'
                elif education == 2:
                    education = u'专硕'
                elif education == 3:
                    education = u'博士'
                with getConn() as cursor:
                    cursor.execute(
                        '''
                        insert into user(account, username, password, education, grade, score, fund, telephone, qq, adm_time) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
                        ''' %(account, username, password, education, grade, score, fund, telephone, qq, adm_time))
                return redirect(url_for('admin.user_list'))
    return render_template('admin/user_add.html')


@admin.route('/user/list/')
@admin_login_req
def user_list():
    """
    成员列表
    """
    user_columns = ('id', 'account', 'username', 'education', 'grade', 'telephone', 'qq', 'adm_time')
    users = []
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, education, grade, telephone, qq, adm_time from user
            ''')
        for item in cursor.fetchall():
            users.append(dict(zip(user_columns, item)))
    for user in users:
        for key in user:
            if not user[key]:
                user[key] = u'待录入'
    return render_template('admin/user_list.html', users=users)


@admin.route('/score/edit/<int:user_id>/', methods=['GET', 'POST'])
@admin_login_req
def score_edit(user_id=None):
    """
    修改得分
    user_id: 用户id
    """
    error_msg = None
    if request.method == 'POST':
        current_score = int(request.form['current_score'])
        option = int(request.form['option'])
        try:
            edit_score = int(request.form['edit_score'])
        except:
            error_msg = u'请输入整数'
            flash(error_msg)
        if not error_msg:
            reason = request.form['reason']
            if reason == '':
                reason = u'无详细说明'
            if option == 2:  # 减分
                edit_score = -edit_score
            score = current_score + edit_score
            with getConn() as cursor:
                # 更新得分
                cursor.execute(
                    '''
                    update user set score="%s" where id="%s"
                    ''' %(score, user_id))
                # 分数更新记录
                cursor.execute(
                    '''
                    insert into scorelog(user_id, value, reason) values ("%s", "%s", "%s")
                    ''' %(user_id, edit_score, reason))
                if option == 1:  # 加分则同时增加额度
                    # 更新额度
                    cursor.execute(
                        '''
                        update user set fund=fund + %s where id="%s"
                        ''' %(edit_score, user_id))
                    # 额度更新记录
                    edit_fund = edit_score
                    cursor.execute(
                    '''
                    insert into fundlog(user_id, value, reason) values ("%s", "%s", "%s")
                    ''' %(user_id, edit_fund, reason))
            return redirect(url_for('admin.index'))
    keys = ('id', 'account', 'username', 'score')
    score_label = ('id', 'name')
    labels = []
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, score from user where id="%s"
            ''' %user_id)
        user = cursor.fetchone()
        cursor.execute(
            '''
            select * from score_label
            ''')
    user = dict(zip(keys, user))
    for item in cursor.fetchall():
        labels.append(dict(zip(score_label, item)))
    return render_template('admin/score_edit.html', labels=labels, user=user)


@admin.route('/fund/edit/<int:user_id>/', methods=['GET', 'POST'])
@admin_login_req
def fund_edit(user_id=None):
    """
    修改额度
    user_id: 用户id
    """
    error_msg = None
    if request.method == 'POST':
        current_fund = int(request.form['current_fund'])
        option = int(request.form['option'])
        try:
            edit_fund = int(request.form['edit_fund'])
        except:
            error_msg = u'请输入整数'
            flash(error_msg)
        if not error_msg:
            reason = request.form['reason']
            if reason == '':
                reason = u'无详细说明'
            if option == 2:  # 减少额度
                edit_fund = -edit_fund
            fund = current_fund + edit_fund
            with getConn() as cursor:
                cursor.execute(
                    '''
                    update user set fund="%s" where id="%s"
                    ''' %(fund, user_id))
                cursor.execute(
                    '''
                    insert into fundlog(user_id, value, reason) values ("%s", "%s", "%s")
                    ''' %(user_id, edit_fund, reason))
            return redirect(url_for('admin.index'))
    keys = ('id', 'account', 'username', 'fund')
    with getConn() as cursor:
        cursor.execute(
            '''
            select id, account, username, fund from user where id="%s"
            ''' %user_id)
        user = cursor.fetchone()
    user = dict(zip(keys, user))
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
            ''' %user_id)
    return redirect(url_for('admin.user_list'))


@admin.route('/pwd/', methods=['GET', 'POST'])
@admin_login_req
def pwd():
    """
    管理员修改密码
    """
    if request.method == 'POST':
        error_msg = None
        user_id = request.form['user_id']
        old_password = request.form['old_password']
        new_password1 = request.form['new_password1']
        new_password2 = request.form['new_password2']
        keys = ('id', 'account', 'password', 'username')
        with getConn() as cursor:
            cursor.execute(
                '''
                select id, account, password username from admin where id="%s"
                ''' %user_id)
            user = cursor.fetchone()
        user = dict(zip(keys, user))
        print(user['password'])
        if old_password != user['password']:
            error_message=u"旧密码错误"
            flash(error_message)
        elif new_password1 == u"":
            error_message=u"新密码不能为空"
            flash(error_message)
        elif new_password1 != new_password2:
            error_message=u"两次输入密码不一致"
            flash(error_message)
        else:
            with getConn() as cursor:
                cursor.execute(
                    '''
                    update admin set password="%s" where id="%s"
                    ''' %(new_password1, user_id))
            return redirect(url_for('admin.index'))
    return render_template('admin/pwd.html')
