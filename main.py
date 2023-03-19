from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource
from PIL import Image
from image_data import labelbox_image_data
from image_queue import queue_image
import requests
import uuid

app = Flask(__name__)
api = Api(app)
BASE = "/http://127.0.0.1:5000/"

# labelbox_image_data = {}
labelbox_image_queue = []

@app.route('/assets/images', methods = ['POST'])
def handle_request():
  data = request.get_json()
  image_id =  uuid.uuid4()

  try:
    image_data = {
      "image_path" : data["assetPath"]["location"] + data["assetPath"]["path"],
      "id" : image_id,
      "state": "queued",
      "notifications" : data["notifications"]
    }
    
    # Add data to a dictionary, this is assuming we want to keep all image data even after they have been validated.
    # For example, if someone was to GET /assets/images/<id> it should return a state of success for finished validations
    labelbox_image_data[f'{image_id}'] = image_data
    
    # add to the queue, which keeps track of images yet to be validated
    labelbox_image_queue.append(image_id)
    
    # queue_image will handle validation && sending further notifcations to the webook URLs
    response = queue_image(image_data)
    return jsonify(response), 202
  except FileNotFoundError:
    response = {
      "errors": {
        "file" : 'Not found'
        }
    }
    
    # Are we supposed to call the "onFailure" webhook here?
    return jsonify(response), 201

@app.route('/assets/images/<id>', methods = ['GET'])
def get_image_info(id):
  response = {
    "id" : id,
    "state" : labelbox_image_data[id]["state"]
  }
  return jsonify(response), 202
     
if __name__ == "__main__":
  app.run(debug=True)
