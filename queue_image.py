from image_validator import validate_image

def queue_image(image_path):
  while True:
    validate_image(image_path)