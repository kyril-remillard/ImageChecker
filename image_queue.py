from image_validator import validate_image
from image_data import labelbox_image_data


def queue_image(image_data):
  # print(labelbox_image_data[image_data["id"]]["state"])
  # labelbox_image_queue.pop
  labelbox_image_data[f'{image_data["id"]}']["state"] = "started"
  return validate_image(image_data)
  # print(labelbox_image_data[f'{image_data["id"]}']["id"])
  # print(labelbox_image_data[f'{image_data["id"]}'])
  # labelbox_image_queue.pop
  # while True:
  # validate_image(image_data)