from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import os
import sys
import json

#set url target
localhost_url = "http://localhost:8000"

#set request headers
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

#makes sure that the package directory is specified
if (len(sys.argv) == 1):
    print("ERROR: Please specify the package directory as an input parameter")
    exit()

#accesses package directory
package_directory = os.fsencode(sys.argv[1])

#list out all files 
list_of_files = os.listdir(package_directory)
total_number_of_files = len(list_of_files)

#keeps track of number of resources ingested
success = 0
failure = 0

#iterate over the files  
for file in list_of_files:
    filename = os.fsdecode(file)
     
    #checks that the file is a json bundle
    if filename.endswith(".json"):
        #opens JSON file as a JSON dict
        print("now opening file: " + filename)
        f = open(filename)
        fhir_bundle = json.dumps(json.load(f))
        #sends the request to target url and capture the response
        response = requests.post(url=localhost_url, headers=headers, data=fhir_bundle)
        #prints the response to console
        print(response)
        if (response.status_code == 200):
            success = success + 1
        else:
            print("ERROR: could not ingest %s", filename)
            print(response.content())
            failure = failure + 1
        print("Processed file " + str(success + failure) +  " out of " + str(total_number_of_files))
        print(str((success + failure)/total_number_of_files) + "%" + " Done")

print("Tomocurl completed reading package: " + sys.argv[1])
print("Successfully ingested " + str(success) + " json files")
print("Failed to ingest " + str(failure) + " json files")

        