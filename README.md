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
```
# 创建数据库
mysql -uroot -p123456
CREATE DATABASE score;

# 切换到 score 根目录下，执行以下命令
python manage.py deploy
```

## 项目启动
```
# 切换到 score 根目录下，执行以下命令
python manage.py run
```

## 数据库
### ER 图
![ER图](er.jpg)
