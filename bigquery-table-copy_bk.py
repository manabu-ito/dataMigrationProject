# Imports the Google Cloud client library
# example:
# python bigquery-table-copy.py htl-datastore-prod htl_backup dss_rtparent 20060331 20070430
# python bigquery-table-copy.py htl-datastore-prod htl_backup dss_twittersampling 20060331 20070430


import uuid, time, sys
from google.cloud import bigquery
import google.cloud.bigquery.job

argvs = sys.argv
source_project = argvs[1]
destination_project = argvs[2]
dataset_name = argvs[3]
from_date = argvs[4]
to_date = argvs[5]

# Instantiates a client

bigquery_client_destination = bigquery.Client(destination_project)
bigquery_client_source = bigquery.Client(source_project)

dataset_destination = bigquery_client_destination.dataset(dataset_name)
dataset_source = bigquery_client_source.dataset(dataset_name)


def copyTable(projectFrom, projectTo, datasetFrom, datasetTo, tableName):
	
	table_source = datasetFrom.table(tableName)
	table_destination = datasetTo.table(tableName)

	job_id = str(uuid.uuid4())
	job = projectFrom.copy_table(job_id, table_destination, table_source)

	job.create_disposition = (google.cloud.bigquery.job.CreateDisposition.CREATE_IF_NEEDED)

	job.begin()  # Start the job.
	print('Waiting for job to finish...')
	job.result()

	print('Table {} copied to {}.'.format(tableName, tableName))

for table in dataset_source.list_tables():
        tmpMonth = table.name[0:4]
        if tmpMonth == "LOAD":
            continue
        else:
            month = table.name[8:16]
            tmp = int(month)
            if tmp > int(to_date):
                break
            elif tmp < int(from_date):
                continue
            else:
	        print("==================Table Copy Start==================")
	        copyTable(bigquery_client_source, bigquery_client_destination, dataset_source, dataset_destination, table.name)
	        print("==================Table Copy End==================")
