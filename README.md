## 依赖包

### requirements.txt
```
PyMySQL==0.7.11
Flask==0.12.2
Flask_Script==2.0.6
```

### 安装依赖包 
``` shell
pip install -r requirements.txt
```

## 数据库

### 创建数据库
``` sql
CREATE DATABASE score;
```

### 数据库初始化
```
source init.sql
```

### 数据库迁移
``` sql
mysql dump -uroot -p123456 > score.sql
source score.sql
```

### ER 图
![ER图](er.jpg)

## 待完善
- 分页功能
- 搜索功能
- 统计功能：排序，分时间段数据统计
- 添加普通管理员
- 普通管理员权限管理
- 主页前端处理
- 前台后端逻辑处理、前台前端页面完善

## 服务器

### 安装 NGINX 服务器