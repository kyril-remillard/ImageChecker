import sys
sys.path.append('..')

from library.library_functions import *

def test_valid_width():
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/Random_pyramids.jpeg'
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  
  assert valid_width(success_file_path) == True  
  assert valid_width(failure_file_path) == False  
  
def test_validate_width():
  valid_width_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  invalid_width_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/Random_pyramids.jpeg'
  invalid_width = width(invalid_width_file)
  
  assert validate_width(valid_width_file) == {}
  assert validate_width(invalid_width_file) == {
    "image" :  [f'Image width exceeds maximum ({invalid_width}/1000)']
  }

def test_validate_height():
  valid_height_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  invalid_height_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/Random_pyramids.jpeg'
  invalid_height = height(invalid_height_file)
  
  assert validate_height(valid_height_file) == {}
  assert validate_height(invalid_height_file) == {
    "image" :  [f'Image height exceeds maximum ({invalid_height}/1000)']
  }

def test_valid_height():
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/Random_pyramids.jpeg'
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  
  assert valid_height(success_file_path) == True  
  assert valid_height(failure_file_path) == False 

def test_valid_file_size():
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/SampleJPGImage_15mbmb.jpg'
  
  assert valid_file_size(success_file_path) == True 
  assert valid_file_size(failure_file_path) == False 

def test_valid_image_file_type():
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/png-image.png'
  
  assert valid_image_file_type(success_file_path) == True 
  assert valid_image_file_type(failure_file_path) == False 

def test_valid_image_file():
  image_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  non_image_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/library/library_functions.py'  
  
  assert valid_image_file(image_file) == True
  assert valid_image_file(non_image_file) == False
  
def test_validate_file_size():
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/SampleJPGImage_15mbmb.jpg'
  
  assert validate_file_size(success_file_path) == {} 
  assert validate_file_size(failure_file_path) == {
    "file_size" :  ['File size must be less than 10MB']
  }
  
def test_validate_image_file_type():
  success_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  failure_file_path = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/png-image.png'
  
  assert validate_image_file_type(success_file_path) == {}
  assert validate_image_file_type(failure_file_path) == {
    "format" : ['Image format is not JPEG']
  }
  
def test_validate_image_file():
  image_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/test_images/butterfly-blue-insect-drawing.jpeg'
  non_image_file = '/Users/kyrildoubson-remillard/Desktop/ImageChecker/library/library_functions.py'  
  
  assert validate_image_file(image_file) == {}
  assert validate_image_file(non_image_file) == {
    "file_type" : 'File must be a valid image file'
  }