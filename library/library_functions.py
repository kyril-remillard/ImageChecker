from PIL import Image
import os
MAX_WIDTH = 1000
MAX_HEIGHT = 1000
MAX_FILE_SIZE_IN_MB = 10

def width(file_path):
  return Image.open(file_path).size[0]

def height(file_path):
  return Image.open(file_path).size[1]

# Adjective 'valid' returns booleans

def valid_width(file_path):
  if width(file_path) > MAX_WIDTH:
    return False

  return True

def valid_height(file_path):  
  if height(file_path) > MAX_HEIGHT:
    return False

  return True

def valid_file_size(file_path):
  file_size_in_megabytes = os.stat(file_path).st_size / (1024 * 1024)

  if file_size_in_megabytes >= MAX_FILE_SIZE_IN_MB:
    return False

  return True

def valid_image_file_type(file_path):
  image = Image.open(file_path)
  
  if image.format != 'JPEG':
    return False

  return True

def valid_image_file(file_path):
  try:
    Image.open(file_path)
    return True
  except:
    return False

# Verb 'validate' returns errors object

def validate_width(file_path):
  errors = {}
  
  if not valid_width(file_path):
    errors["image"] = [(f'Image width exceeds maximum ({width(file_path)}/{MAX_WIDTH})')]
  
  return errors

def validate_height(file_path):
  errors = {}
  
  if not valid_height(file_path):
    errors["image"] = [(f'Image height exceeds maximum ({height(file_path)}/{MAX_HEIGHT})')]
  
  return errors

def validate_file_size(file_path):
  errors = {}
  
  if not valid_file_size(file_path):
    errors["file_size"] = ['File size must be less than 10MB']
  
  return errors

def validate_image_file_type(file_path):
  errors = {}
  
  if not valid_image_file_type(file_path):
    errors["format"] = ['Image format is not JPEG']
  
  return errors

def validate_image_file(file_path):
  errors = {}
  
  if not valid_image_file(file_path):
    errors["file_type"] = 'File must be a valid image file'
  
  return errors

def validate_image_dimensions(file_path):
  errors = {}
  
  if not valid_width(file_path):
    errors["image"] = [(f'Image width exceeds maximum ({width(file_path)}/{MAX_WIDTH})')]
    
  if not valid_height(file_path):
    if errors["image"]:
      errors["image"].append(f'Image height exceeds maximum ({height(file_path)}/{MAX_HEIGHT})')
    else:
      errors["image"] = [(f'Image height exceeds maximum ({height(file_path)}/{MAX_HEIGHT})')]
  
  return errors