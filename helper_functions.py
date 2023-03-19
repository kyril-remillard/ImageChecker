import os
from PIL import Image
import constants

def is_accessible(image_path):
  return os.access(image_path, os.R_OK)

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
        errors["image"] = []
        errors["image"].append(f'Image width exceeds maximum ({width}/{constants.MAX_WIDTH})')
    
    if height > constants.MAX_HEIGHT:
      if "image" in errors:
        errors["image"].append(f'Image height exceeds maximum ({height}/{constants.MAX_HEIGHT})')
      else:
        errors["image"] = []
        errors["image"].append(f'Image height exceeds maximum ({height}/{constants.MAX_HEIGHT})')
    
    if image.format != 'JPEG':
      errors["format"] = ['Image format is not JPEG']
    
    if file_size_in_megabytes >= constants.MAX_FILE_SIZE_IN_MB:
      errors["file_size"] = ['File size must be less than 10MB']

  except:
    errors["file_type"] = 'File must be a valid image file'
  
  return errors