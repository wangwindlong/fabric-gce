from fabric.api import *

# 远程服务器登陆使用的用户名
env.user = 'wang20064412'
# 需要进行操作的服务器地址
env.hosts = ['104.155.196.109/']

def hello():
    print "hello world"

#http://docs.jinkan.org/docs/flask/patterns/fabric.html
def deploy_bak():
    # 之处发布产品的名称和版本
    dist = local('python setup.py --fullname', capture=True).strip()
    # 将代码归档上传到服务器当中的临时文件夹内
    put('dist/%s.tar.gz' % dist, '/tmp/project.tar.gz')
    # 创建一个文件夹，进入这个文件夹，然后将我们的归档解压到那里
    run('mkdir /tmp/project')
    with cd('/tmp/project'):
        run('tar xzf /tmp/project.tar.gz')
        # 使用我们虚拟环境下的 Python 解释器安装我们的包
        run('/var/www/project/env/bin/python setup.py install')
    # 现在我们的代码已经部署成功了，可以删除这个文件夹了
    run('rm -rf /tmp/project /tmp/yourapplication.tar.gz')
    # 最终生成 .wsgi 文件，以便于 mod_wsgi 重新加载应用程序
    run('touch /var/www/project.wsgi')

def deploy():
    with cd('/home/wang20064412/workspace/python/fabric-gce'):
        run('git pull')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')
