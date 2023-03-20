import os
from PIL import Image
import constants
import validators
import requests

def is_accessible(image_path):
  return os.access(image_path, os.R_OK)


# NOTIFICATION FUNCTIONS

def send_start_notification(image_data):
  on_start_webhook_url = image_data["notifications"]["onStart"]
  on_start_payload = {
    "id" : image_data["id"],
    "state" : "started",
  }
  requests.post(on_start_webhook_url, on_start_payload)

def send_failure_notification(image_data, errors):
  payload = {
      "id" : image_data["id"],
      "state" : "failed",
      "errors" : errors
    }
  webhook_url = image_data["notifications"]["onFailure"]
  requests.post(webhook_url, payload)

def send_success_notification(image_data):
  on_start_webhook_url = image_data["notifications"]["onSuccess"]
  on_start_payload = {
    "id" : image_data["id"],
    "state" : "success",
  }
  requests.post(on_start_webhook_url, on_start_payload)


# VALIDATION FUNCTIONS
  # returns error objects if validation fails

def validate_image_attributes(image_path):
  errors = {}
  
  try:
    image = Image.open(image_path)
    width, height = image.size
    file_size_in_megabytes = os.stat(image_path).st_size / (1024 * 1024)
    
    if width > constants.MAX_WIDTH:
      if "image" in errors:
        errors["image"].append(f'Image width exceeds maximum ({width}/{constants.MAX_WIDTH})')
      else:
        errors["image"] = [(f'Image width exceeds maximum ({width}/{constants.MAX_WIDTH})')]

    if height > constants.MAX_HEIGHT:
      if "image" in errors:
        errors["image"].append(f'Image height exceeds maximum ({height}/{constants.MAX_HEIGHT})')
      else:
        errors["image"] = [(f'Image height exceeds maximum ({height}/{constants.MAX_HEIGHT})')]
    
    if image.format != 'JPEG':
      errors["format"] = ['Image format is not JPEG']
    
    if file_size_in_megabytes >= constants.MAX_FILE_SIZE_IN_MB:
      errors["file_size"] = ['File size must be less than 10MB']

  except:
    errors["file_type"] = 'File must be a valid image file'
  
  return errors

def validate_urls(urls):
  errors = {}
  
  for notification, url in urls.items():
    if not validators.url(url):
      errors[f'{notification}'] = f'{url} is not a valid url'

  return errors