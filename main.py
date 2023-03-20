from flask import Flask, request, jsonify
from flask_restful import Api
from image_data import labelbox_image_data
# from image_queue import queue_image
from helper_functions import validate_urls
import uuid


app = Flask(__name__)
api = Api(app)

@app.route('/assets/images', methods = ['POST'])
def handle_request():
  try:
    data = request.get_json()
    image_path = data["assetPath"]["location"] + data["assetPath"]["path"]
    
    # STEP 1: Check whether the file is reachable by the server, this will exit the try block on FileNotFoundError
    open(image_path, "r")

    # STEP 2: Validate the notification URLs:
    notification_url_errors = validate_urls(data["notifications"])
    if notification_url_errors:
      response = {
        "errors" : notification_url_errors
      }
      return jsonify(response), 400
  
    image_id =  uuid.uuid4()
    image_data = {
      "image_path" : data["assetPath"]["location"] + data["assetPath"]["path"],
      "id" : image_id,
      "state": "queued",
      "notifications" : data["notifications"]
    }

    # STEP 3: Add image data to database
    labelbox_image_data[f'{image_id}'] = image_data
    
    # Step 4: Queue image for validation
      # to do: implement queue
      # queue_image(image_data)
    
    response = {
      "id": image_id,
      "state": "queued"
    }
    return jsonify(response), 202
  except FileNotFoundError:
    response = {
      "errors": "file not found"
    }
    return jsonify(response), 404

@app.route('/assets/images/<id>', methods = ['GET'])
def get_image_info(id):
  if id in labelbox_image_data:
    response = {
      "id" : id,
      "state" : labelbox_image_data[id]["state"]
    }
    return jsonify(response), 200
  else:
    response = {
      "errors" : f'the provided image id is invalid [{id}]'
    }
    return jsonify(response), 404
     
if __name__ == "__main__":
  app.run(debug=True)
