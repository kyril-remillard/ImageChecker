from image_validator import validate_image
from image_data import labelbox_image_data

labelbox_image_queue = []

def queue_image(image_data):
  labelbox_image_data[f'{image_data["id"]}']["state"] = "started"
  validate_image(image_data)