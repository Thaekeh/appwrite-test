import json
import os

import requests

# parsing payload
payload = json.loads(os.environ['APPWRITE_FUNCTION_EVENT_DATA'])
documentId = payload['$id']


def updateDocument(documentId):
    print("ID: " + documentId)
