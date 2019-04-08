#  django_blog_demo

#### 项目介绍
一个django blog demo，管理后台使用xadmin做替代，具有文章展示、基础搜索功能、栏目分类显示功能、文章分页功能、标签分类功能、归档功能，可扩充第三方账号登录发布评论、相似性文章推荐、相册功能、文章转发订阅等功能。

#### 软件架构
1. python 3.6.2
2. django 1.11.16
3. redis redis-5.0.3
4. amaze UI、jquery


#### 安装教程

1. pip install -r requirements.txt
2. 安装redis. https://redis.io/download
3. 直接runserver测试或者线上部署(使用collectstatic收集静态文件)

#### 使用说明

1. 默认使用sqlite作为数据库,后台管理员,用户:demoadmin 密码:Zcz9VuIm7Z
2. 线上使用nginx+gunicorn+django+redis的组合部署(数据库使用mysql或者sqlite)
3. xxxx

![](https://raw.githubusercontent.com/sepmoon/django_blog_demo/master/img.png)
