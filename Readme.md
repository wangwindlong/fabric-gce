Skip to content
This repository
Search
Pull requests
Issues
Gist
 @wangwindlong
 Unwatch 1
  Star 0
  Fork 0 wangwindlong/fabric-gce
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
No description or website provided. — Edit
 5 commits
 1 branch
 0 releases
 1 contributor
 JavaScript 54.1%	 Python 22.3%	 CSS 14.7%	 HTML 8.9%
JavaScript	Python	CSS	HTML
Clone or download  Create new file Upload files Find file Branch: master New pull request
Latest commit e210aff  3 days ago  wangwindlong test deploy
app	test deploy	3 days ago
tests	init	3 days ago
.gitignore	init	3 days ago
Readme.md	test deploy	3 days ago
config.py	init	3 days ago
fabfile.py	test deploy	3 days ago
manage.py	init	3 days ago
requirements.txt	add requirements module	3 days ago
run.py	init	3 days ago
 Readme.md
Todo
a todo web app based on flask and mongodb

﻿ Flask + google compute engine 部署

1.安装supervisor virtualenv 等工具 sudo pip install virtualenv sudo apt-get install supervisor #应用程序进程的控制 多应用进程管理 应用中断后快速恢复 sudo apt-get install mongodb-server nginx

2.激活virtualenv 和 flask virtualenv venv source venv/bin/activate pip install flask deactivate #退出virtualenv

3.编写app.py并运行 1)app.py from flask import Flask

app = Flask(name)

@app.route('/') def index(): return "Hello World too"

if name == "main": app.run(port=8081)

2) python app.py

3) curl 127.0.0.1:8081

4.supervisor使用 1）添加配置文件 /etc/supervisor/conf.d/app.conf [program:app] command = python /home/wang20064412/app.py 2）重启supervisor：sudo service supervisor restart 3）sudo supervisorctl 打开控制台 status 查看状态 stop app 停止app应用 start app 启动app应用 reload 重启supervisor

5.部署flask 1)安装nginx和mongodb 查看nginx状态 sudo service nginx status 查看mongo状态 mongo

2）上传应用程序和安装应用所需的安装包 source venv/bin/activate pip install -r requirements.txt deactivate

使用filezilla链接gce： Edit→Setting→SFTP Click on Add Key File button, and point it to the PPK file generated（gce-ssh-keygen.hub）. Once this is done, you can connect to your instance using FileZilla SFTP. Specify your instance's public IP address in the host field (stfp://instanceipaddress). You would not need to specify any password.

3）配置nginx cd /etc/nginx & ls sites-available 可用的配置文件 sites-enabled 生效的配置文件（创建available的软链接） sudo vim sites-available/todo_app server { listen 80; location /static { alias /home/wang20064412/Todo/app/static; } location / { proxy_pass http://127.0.0.1:9000; } } cd sites-enabled/ sudo ln -s ../sites-available/todo_app . sudo service nginx reload #重启nginx如果启动失败：vi /var/log/nginx/error.log

4）配置supervisor cd ../supervisor/ sudo vim conf.d/todo.conf #添加todo的supervisor配置文件：

[program:todo] command = /home/wang20064412/Todo/venv/bin/gunicorn -b 127.0.0.1:9000 run:app directory = /home/wang20064412/Todo

sudo supervisorctl reload #重新加载supervisor

6.nginx配置文件 https://cloud.google.com/compute/docs/tutorials/setting-up-lemp#install_nginx_and_php_on_your_instance

修改nginx配置文件: sudo vi /etc/nginx/sites-available/default LEMP 启动后默认关联打开（default）： sudo vi /var/www/html/index.html

教程上是：/usr/share/nginx/www/phpinfo.php

7.链接ssh ssh wang20064412@104.155.196.109
Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help