from fabric.api import *

env.user = 'wang20064412'
env.hosts = ['104.155.196.109']

def hello():
    print "hello world"

# http://docs.jinkan.org/docs/flask/patterns/fabric.html
def deploy_bak():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/project.tar.gz')
    run('mkdir /tmp/project')
    with cd('/tmp/project'):
        run('tar xzf /tmp/project.tar.gz')
        run('/var/www/project/env/bin/python setup.py install')
    run('rm -rf /tmp/project /tmp/yourapplication.tar.gz')
    run('touch /var/www/project.wsgi')

def deploy():
    with cd('/home/wang20064412/workspace/python/fabric-gce'):
        run('git pull origin master')
        sudo('supervisorctl restart todo')
        sudo('supervisorctl status')