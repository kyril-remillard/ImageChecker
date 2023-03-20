from image_validator import validate_image
from image_data import labelbox_image_data
from helper_functions import set_validation_state


labelbox_image_queue = []

def queue_image(image_data):
  validate_image(image_data)