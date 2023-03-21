from library.library_functions import *

class ImageValidator:
  def __init__(self, file_path):
    self.image_path = file_path
    self.errors = {}
  
  def validate_image(self):
    self.errors.update(validate_image_file(self.image_path))
    if self.errors:
      return self.errors
    
    self.errors.update(validate_image_dimensions(self.image_path))
    self.errors.update(validate_file_size(self.image_path))
    self.errors.update(validate_image_file_type(self.image_path))
    
    return self.errors