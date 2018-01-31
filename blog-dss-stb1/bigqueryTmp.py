#coding: utf-8

import MySQLdb
import subprocess
from jinja2 import Environment, FileSystemLoader
import sys, os, time

env = Environment(loader= FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('bigqueryTmp_old.yml')
message = {}
flag = False
false_list = []
argvs = sys.argv

def getTables(month):
    connect = MySQLdb.connect(host="blog-dss-stb1", port=3306, db="dss", user="dss", passwd="", charset="utf8")
    cursor  = connect.cursor()
    listtmp = []

    sql = sql = "show tables like '%document" + month + "%'"
    cursor.execute(sql)

    res = cursor.fetchall()

    for row in res:
        listtmp.append(row[0].encode('utf-8'))

    cursor.close()
    connect.close()

    return listtmp

res = getTables(argvs[1])
message['projectid'] = argvs[2]
message['datasetname'] = argvs[3]
for i in res:
    message['mysqltable'] = i
    message['bigquerytable'] = i
    tmp = tpl.render({'info': message})
    tmpfile = open('embulk_bigquery_' + i + '.yml', 'w')
    tmpfile.write(tmp.encode('utf-8'))
    tmpfile.close()

for i in res:
    filepath = 'embulk_bigquery_' + i + '.yml'
    res = os.path.isfile(filepath)
    #os.chdir('/home/vagrant/embulk_sample/')
    command = '/home/buzz-setup/.embulk/bin/embulk run /home/buzz-setup/bin.wu/blog-dss-stb1/' + filepath
    print(command)
    if res:
        tmp = subprocess.call(command, shell=True)
        if tmp != 0:
            print "process is failure"
            flag = True
            false_list.append(i)
            continue
            #command failure
        else:
            print "processing is successful!"
            os.remove('/home/buzz-setup/bin.wu/blog-dss-stb1/' + filepath)
            time.sleep(1)

    else:
        print "file is not exists"
        sys.exit()

if flag:
    print(false_list)

sys.exit()
