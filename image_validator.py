from flask import Flask, request, jsonify, Response
from PIL import Image

def validate_image(image_path, notifications):
  errors = []
  try:
    image = Image.open(image_path)
    
    width, height = image.size
    if width > 1000:
      errors.append('Width cannot be over 1000 pixels')
    
    if height > 1000:
      errors.append('Height cannot be over 1000 pixels')
    
    if image.format != 'JPEG':
      errors.append('Image format must be JPEG')
  except:
    errors.append('File must be a valid image file')
  
  if errors:
    response = {
      "errors" : errors,
      "next_step" : f'Send it to the following webhook endpoint: {notifications["onFailure"]}'
    }
    return jsonify(response), 202
  else:
    return jsonify('The image was successfully validated. Send to --> "onSuccess": "http://somevalidurl.com"'), 202