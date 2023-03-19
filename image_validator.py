from flask import Flask, request, jsonify, Response
import requests
from image_data import labelbox_image_data, labelbox_image_queue
from helper_functions import is_accessible, validate_image_attributes

def validate_image(image_data):
  image_path = labelbox_image_data[f'{image_data["id"]}']["image_path"]
  errors = {}
  
  if is_accessible(image_path) == False:
    errors["access"] = 'File is not reachable by the server'
    payload = {
      "id" : image_data["id"],
      "state" : "failed",
      "errors" : errors
    }
    return payload 
  
  errors = validate_image_attributes(image_path)
  
  if errors:
    payload = {
      "id" : image_data["id"],
      "state" : "failed",
      "errors" : errors
    }
    # requests.post(image_data["notifications"]["onFailure"], payload)
    return payload
  else:
    payload = {
      "id" : image_data["id"],
      "state" : "success",
    }
    # requests.post(image_data["notifications"]["onSuccess"], payload)
    return payload
