import random
import sys
import json
import requests
from requests.structures import CaseInsensitiveDict
from urllib3 import response
from bs4 import BeautifulSoup

#set url target
host_url = "http://localhost:8000/DEFAULT/Location"
#set request headers
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

def delete_locations():
    try: 
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
    except:
        print("to delete locations, please input start id and stop id as integer values")
        exit()
    for id in range(start, stop):
        print("deleting location with id = " + str(id))
        response = requests.delete(url=host_url + "/" + str(id), headers=headers)
        if (200 <= response.status_code <= 299):
            print("Successfully deleted resource with id: " + str(id))
        else:
            print("Failed to delete resource with id: " + str(id))
        print(str(id - start + 1) + "/" + str(stop - start))


#set location randomizer url
random_location_url = "https://hiveword.com/papi/random/locationNames"

#makes sure that the number of Locations to be created is set correctly
if (len(sys.argv) == 1):
    print("ERROR: Please specify the number of Location resources to create as an input parameter")
    exit()

if len(sys.argv) == 3:
    delete_locations()
    exit()

requested_locations = sys.argv[1]

try:
    requested_locations = int(requested_locations)
except:
    print("ERROR: Input parameter must be an integer")
    exit()


#keep track of success and failures
success = 0
failure = 0

for request in range(requested_locations):
    #build location
    location_dict = {}
    location_dict["resourceType"] = "Location"
    location_dict["status"] = "active"

    #extract location randomly
    random_location_json = requests.get(url=random_location_url).json()[0]

    #build address
    number = str(random.randint(0, 10000))
    city = random_location_json["name"]
    country = random_location_json["country"]

    address = {}
    address["line"] = number
    address["city"] = city
    address["country"] = country

    location_dict["name"] = number + city + country
    location_dict["address"] = address

    #build json object
    location_json = json.dumps(location_dict)

    print(location_json)

    #send location to endpoint and capture response
    response = requests.post(url=host_url, headers=headers, data=location_json)

    #prints the response to console
    print(response)
    if 200 <= response.status_code <= 299:
        success = success + 1
    else:
        print("ERROR: could not ingest location")
        #print(response.content())
        failure = failure + 1
    print("Processed location " + str(success + failure) +  " out of " + str(requested_locations))
    print(str((success + failure) * 100 /requested_locations) + "%" + " Done")

    


