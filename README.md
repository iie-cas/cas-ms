## 解决项目依赖问题
### 通过 requirements.txt 文件安装依赖包 
```
pip install -r requirements.txt
```

### 生成 requirements.txt 文件的方法
#### 方法一，该项目使用的是该方法
```
pip install pipreqs
pipreqs ./
```
#### 方法二
```
pip freeze > ./requirements.txt
```

## 项目部署

### 创建数据库
```
# 打开 mysql 客户端
mysql -uroot -p123456
create database score;

# 切换到 score 根目录下，执行以下命令
python manage.py deploy
```

### 插入测试数据
```
# 打开 mysql 客户端
mysql -uroot -p123456
# 执行 init.sql 中的 sql 语句
```

## 项目启动
```
# 切换到 score 根目录下，执行以下命令
python manage.py run
```

## 项目中用到的正则规则
1. 初始化分数（额度）可以为 0分 或者非 0 开头的 1~9 位数
2. 每次修改分数（额度）可以为非 0 开头的 1~4 位数，不能为 0 分
3. 账号只包含字母和数字，长度在 3-20 之间
4. 密码只包含字母和数字，长度在 6-20 之间
5. 姓名只能包含汉字，长度在 2-4 之间
6. 手机号码长度为 11 位，第一位必须为 1，第二位可为 3、4、5、7、8

## 项目用到的基础知识
1. HTML, CSS, JavaScript
2. jQuery
3. Bootstrap
4. Flask
5. MySQL
6. JSON
7. AJAX
8. Nginx

## 小项目介绍
这个小项目用到了大量的 Web 开发的基本技术，适合入门学习。

## Nginx
Nginx 是高度自由化的Web服务器，它的功能是由许多模块来支持。如果使用了某个模块，这个模块使用了一些类似 zlib 或 OpenSSL 等的第三方库，那么就必须先安装这些软件。

### 辅助命令
``` shell
cat /proc/cpuinfo
free -m
df -h
gcc --version
g++ --version
cat /etc/issue
uname -a
uname -r
```

### 安装依赖包
``` shell
# PCRE 库支持正则表达式。如果我们在配置文件 nginx.conf 中使用了正则表达式，那么在编译 Nginx 时就必须把 PCRE 库编译进 Nginx，因为 Nginx 的 HTTP 模块需要靠它来解析正则表达式。另外，pcre-devel 是使用 PCRE 做二次开发时所需要的开发库，包括头文件等，这也是编译 Nginx 所必须使用的。
apt install libpcre3 libpcre3-dev
# zlib 库用于对 HTTP 包的内容做 gzip 格式的压缩，如果我们在 nginx.conf 中配置了 gzip on，并指定对于某些类型（content-type）的 HTTP 响应使用 gzip 来进行压缩以减少网络传输量，则在编译时就必须把 zlib 编译进 Nginx。zlib-devel 是二次开发所需要的库。
apt install zlib1g-dev
# 如果服务器不只是要支持 HTTP，还需要在更安全的 SSL 协议上传输 HTTP，那么需要拥有 OpenSSL。另外，如果我们想使用 MD5、SHA1 等散列函数，那么也需要安装它。
apt install openssl libssl-dev
```

### 安装 Nginx
``` shell
cd /usr/local/src
wget http://nginx.org/download/nginx-1.12.2.tar.gz
tar -zxvf nginx-1.12.2.tar.gz
useradd nginx
cd nginx-1.12.2/
./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-http_ssl_module
make && make install
ln -s /usr/local/nginx/sbin/nginx /usr/sbin
nginx
netstat -anptu | grep nginx
```

## 后续工作
1. 密码密文处理
2. 服务器端合法性验证
3. 分页功能
4. 404 错误页
5. 加分的时候提供可选项同时增加额度

## SQL 语句
``` sql
alter table user drop column adm_time;
update user set grade="二年级" where grade="研二";
```

## 参考
[jQuery](https://www.jquery123.com/)

[Bootstrap](https://v2.bootcss.com/index.html)

[Flask](http://docs.jinkan.org/docs/flask/)

[菜鸟教程](http://www.runoob.com/)

[python 操作 MySQL](http://www.runoob.com/python/python-mysql.html)

[最全正则表达式总结：验证QQ号、手机号、Email、中文、邮编、身份证、IP地址等](http://www.lovebxm.com/2017/05/31/RegExp/)
