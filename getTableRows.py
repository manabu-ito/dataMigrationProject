#coding: utf-8

# Imports the Google Cloud client library
# 使い方↓(20140801から20141231までのbigqueryのデーターを取得)
# プロジェクト名 & データーセット名を環境によって修正する必要がある
# python getTableRows.py 20140801 20141231

from google.cloud import bigquery
import sys, csv

argvs = sys.argv
from_date = argvs[1]
to_date = argvs[2]

# Instantiates a client
bigquery_client = bigquery.Client("htl-datastore-prod")

# The name for the new dataset
dataset_name = 'dss_twittersampling'

# Prepares the new dataset
dataset = bigquery_client.dataset(dataset_name)

tmpDict = {}
for table in dataset.list_tables():
    tmpMonth = table.name[0:4]
    if tmpMonth == "LOAD":
        continue
    else:
        month = table.name[8:16]
        tmp = int(month)
        if tmp > int(to_date) :
            break
        elif tmp < int(from_date):
            continue
        else:
            t = dataset.table(table.name)
            t.reload()
            tmpDict[tmp] = t.num_rows

sortDict = sorted(tmpDict.items())

with open("number.csv", "a") as f:
    #w = csv.DictWriter(f,sortDict)
    w = csv.writer(f)
    #w.writeheader()
    w.writerows(sortDict)
sys.exit()
