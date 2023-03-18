from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource
from PIL import Image
from queue_image import queue_image

app = Flask(__name__)
api = Api(app)
BASE = "/http://127.0.0.1:5000/"

@app.route('/', methods = ['POST'])
def handle_request():
  data = request.get_json()
  try:
    image_path = data["assetPath"]["location"] + data["assetPath"]["path"]
    # queue_image(image_path)
    
    response = {
      "message" : "File successfully received.",
      "next_step" : f'send it to the following webhook endpoint: {data["notifications"]["onStart"]}'
    }
    return jsonify(response), 202
 
  except FileNotFoundError:
    response = {
      "message" : "File not found.",
      "next_step" : f'send it to the following webhook endpoint: {data["notifications"]["onFailure"]}'
    }
    
    return jsonify(response), 201

    
if __name__ == "__main__":
  app.run(debug=True)
