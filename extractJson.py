import json
import requests
import os

batchTot = 91

token = os.environ.get('RCaccessToken')

response = requests.get('https://www.recurse.com/api/v1/profiles?' + 'access_token=' + token)

# get the info for every batch via the api
for i in range(1, batchTot + 1):
    batch = requests.get('https://www.recurse.com/api/v1/batches/' + str(i) + '/people?' + 'access_token=' + token)
    batchJson = batch.json()
    #write each batches info to it's own json file
    with open('jsonFiles' + '\\' + 'batch' + str(i) + '.json', 'w') as json_file:
        json.dump(batchJson, json_file)

