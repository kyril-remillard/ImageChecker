import validators

def file_is_accessible(file_path):
  try:
    open(file_path, "r")
    return True
  except FileNotFoundError:
    return False
  
def validate_file_access(file_path):
  errors = {}
  
  if not file_is_accessible(file_path):
    errors["file access"] = 'File is not accessible'
  
  return errors

def valid_url(url):
  if not validators.url(url):
    return False
  return True

def validate_urls(notifications):
  errors = {}
  
  for notification, url in notifications.items():
    if not valid_url(url):
      errors[f'{notification}'] = f'{url} is not a valid url'

  return errors

# class ApiRequestValidator:
#   def __init__(self, image_data):
#     self.image_path = image_data["assetPath"]["location"] + image_data["assetPath"]["path"]
#     self.notifications = image_data["notifications"]
#     self.errors = {}
  
#   def validate_post_request(self):
#     self.errors.update(validate_file_access(self.image_path))
#     self.errors.update(validate_urls(self.notifications))
    
