#example
# python write-excel_fixed_em_25w.py 201701

import MySQLdb
import sys, os, time
import csv

argvs = sys.argv

def getTables(hostName, month):
    connect = MySQLdb.connect(host=hostName, port=3306, db="dss", user="dss", passwd="", charset="utf8")
    cursor  = connect.cursor()
    dictTmp = {}

    sql = "show tables like 'document" + month + "%'"
    cursor.execute(sql)

    res = cursor.fetchall()

    for row in res:
        tableName = row[0].encode('utf-8')
        sql = "select count(*) from " + tableName
        cursor.execute(sql)
        num = cursor.fetchone()
        dictTmp[tableName] = int(num[0])
        #listtmp.append(int(num[0]))

    cursor.close()
    connect.close()


    return sorted(dictTmp.items())

dss31 = getTables("dss26w", argvs[1])
#dss32 = getTables("DSS32w", argvs[1])

with open('fixed_em_26w_2017.csv', 'a') as f:
    w = csv.writer(f)
    w.writerows(dss31)
    #w.writerows(dss32)

