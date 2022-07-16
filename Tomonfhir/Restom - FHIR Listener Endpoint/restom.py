from flask import Flask, json
from flask import request
import re

num_of_locations = 0
num_of_locations_by_id = {}

num_of_patients = 0
num_of_patients_by_id = {}

api = Flask(__name__)

@api.route('/Location', methods=['GET'])
def get_num_of_locations():
  response = {}
  response["total"] = num_of_locations
  response["resources"] = num_of_locations_by_id
  return json.dumps(response)

@api.route('/Patient', methods=['GET'])
def get_num_of_patients():
  response = {}
  response["total"] = num_of_patients
  response["resources"] = num_of_patients_by_id
  return json.dumps(response)

@api.route('/Location', methods=['DELETE'])
def delete_num_of_locations():
  global num_of_locations, num_of_locations_by_id
  num_of_locations_by_id = {}
  num_of_locations = 0
  return json.dumps("deleted all locations")

@api.route('/Patient', methods=['DELETE'])
def delete_num_of_patients():
  global num_of_patients, num_of_patients_by_id
  num_of_patients_by_id = {}
  num_of_patients = 0
  return json.dumps("deleted all patients")


@api.route('/Location', methods=['POST'])
def add_location():
  global num_of_locations, num_of_locations_by_id
  resource_id = request.get_json()["id"]
  try:
    num_of_locations_by_id[resource_id] = num_of_locations_by_id[resource_id] + 1
  except:
    num_of_locations_by_id[resource_id] = 1
  if num_of_locations_by_id[resource_id] == 1:
    num_of_locations = num_of_locations + 1
  
  return json.dumps("Location received")

@api.route('/Location/<name>', methods=['PUT'])
def add_or_update_location(name):
  global num_of_locations, num_of_locations_by_id
  resource_id = request.get_json()["id"]
  try:
    num_of_locations_by_id[resource_id] = num_of_locations_by_id[resource_id] + 1
  except:
    num_of_locations_by_id[resource_id] = 1
  if num_of_locations_by_id[resource_id] == 1:
    num_of_locations = num_of_locations + 1
  
  return json.dumps("Location received")

@api.route('/Patient/<name>', methods=['PUT'])
def add_or_update_patient(name):
  global num_of_patients, num_of_patients_by_id
  resource_id = request.get_json()["id"]
  try:
    num_of_patients_by_id[resource_id] = num_of_patients_by_id[resource_id] + 1
  except:
    num_of_patients_by_id[resource_id] = 1
  if num_of_patients_by_id[resource_id] == 1:
    num_of_patients = num_of_patients + 1
  
  return json.dumps("Patient received")

@api.route('/Patient/<name>', methods=['DELETE'])
def delete_patient(name):
  global num_of_patients, num_of_patients_by_id

  if name in num_of_patients_by_id:
    num_of_patients_by_id.pop(name)
    num_of_patients = num_of_patients - 1
    return json.dumps("deleted all patient " + name)
  
  return json.dumps("could not delete patient " + name + " since patient does not exist")

if __name__ == '__main__':
    api.run() 