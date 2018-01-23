## NGINX
Nginx是高度自由化的Web服务器，它的功能是由许多模块来支持。如果使用了某个模块，这个模块使用了一些类似zlib或OpenSSL等的第三方库，那么就必须先安装这些软件。

## 辅助命令

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

## 安装依赖包

``` shell
// PCRE库支持正则表达式。如果我们在配置文件nginx.conf中使用了正则表达式，那么在编译Nginx时就必须把PCRE库编译进Nginx，因为Nginx的HTTP模块需要靠它来解析正则表达式。另外，pcre-devel是使用PCRE做二次开发时所需要的开发库，包括头文件等，这也是编译Nginx所必须使用的。
apt install libpcre3 libpcre3-dev
// zlib库用于对HTTP包的内容做gzip格式的压缩，如果我们在nginx.conf中配置了gzip on，并指定对于某些类型（content-type）的HTTP响应使用gzip来进行压缩以减少网络传输量，则在编译时就必须把zlib编译进Nginx。zlib-devel是二次开发所需要的库。
apt install zlib1g-dev
// 如果服务器不只是要支持HTTP，还需要在更安全的SSL协议上传输HTTP，那么需要拥有OpenSSL。另外，如果我们想使用MD5、SHA1等散列函数，那么也需要安装它。
apt install openssl libssl-dev
```

## 安装 nginx
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
