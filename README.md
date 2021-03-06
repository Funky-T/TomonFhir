# TomonFhir
<h2>A collection of scripts and applications related to Fhir data and implementations</h2>

<h3>Restom:</h3>
Restom is a simple Python REST server that accepts FHIR JSON PUT and POST requests for the currently supported resource types:

- Patient

- Location

I set up this simple listener server to test and debug FHIR Rest Server Subscription implementation, and therefore the only information stored as of now is a map (ID: Number of POST/PUT request submitted for that ID) as well as total count of request received. May extend this implementation as requirements arise.

**TO USE:** simply execute the script: i.e run `python Restom.py` in terminal

**DEPENDENCIES:**

- `pip install Flask`

<br></br>
<h3>Tomocurl:</h3>
Tomocurl is a tool I have created in order to install packages (folders) containing FHIR JSON resources. I initially coded this tool up in order to install the resources generated by the Synthea FHIR data generator, as the synthea program generates hundreds of JSON files and I did not want to manually POST each resource to my test server's endpoint.

<br></br>
**TO USE:** run the following command in terminal: `python tomocurl.py {target_package_directory}`. You may have to modify the target endpoint in the code by modifying the value of the `host_url` variable. 

**DEPENDENCIES:**

- `pip install requests`

<br></br>
<h3>Tomolocation:</h3>
Tomolocation is a FHIR JSON Location resource generator and intaller that conforms to the minimal required fields as per the R4 implementation specifications (https://hl7.org/fhir/location.html) with some extra added fields to replicate more accurate production level data. Tomolocation will generate the location resources and POST them to your specified FHIR host server for ingestion.

The currently implemented fields are as follow:

- resourceType
- status
- name
- address (with following sub fields)
  * city
  * line
  * Country
  
 Example of generated output:
 
 ```
 {
   "resourceType":"Location",
   "status":"active",
   "name":"3933Les Artigues-de-LussacFrance",
   "address":{
      "city":"Les Artigues-de-Lussac",
      "line":"3933",
      "country":"France"
   }
}

```

The city and country values are pulled from a random location generator endpoint, therefore this program REQUIRES internet access in order to function.
<br></br>
**TO USE:** run the following command in terminal: `python tomolocation.py {number_of_locations_to_generate}`. You may have to modify the target endpoint in the code by modifying the value of the `host_url` variable.

**DEPENDENCIES:**

- `pip install requests`
- `pip install beautifulsoup4`
