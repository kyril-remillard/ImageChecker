import sys
from library.library_functions import (
  valid_width, valid_height, valid_file_size, valid_image_file,
  validate_image_file, validate_height, validate_width, validate_file_size,
  validate_image_file_type, width, height, valid_image_file_type
)
sys.path.append('..')

IMAGE_LOCATION = '/Users/kyrildoubson-remillard/Desktop/image_checker/test_images/'
def test_valid_width():
    '''
    Returns a boolean if width is valid
    '''
    failure_file_path = IMAGE_LOCATION + 'Random_pyramids.jpeg'
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'

    assert valid_width(success_file_path) is True
    assert valid_width(failure_file_path) is False

def test_validate_width():
    '''
    Returns an errors object with width validation
    '''
    valid_width_file = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    invalid_width_file = IMAGE_LOCATION + 'Random_pyramids.jpeg'
    invalid_width = width(invalid_width_file)

    assert not validate_width(valid_width_file)
    assert validate_width(invalid_width_file) == {
      "image" :  [f'Image width exceeds maximum ({invalid_width}/1000)']
    }

def test_validate_height():
    '''
    Returns an errors object with height validation
    '''
    valid_height_file = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    invalid_height_file = IMAGE_LOCATION + 'Random_pyramids.jpeg'
    invalid_height = height(invalid_height_file)

    assert not validate_height(valid_height_file)
    assert validate_height(invalid_height_file) == {
      "image" :  [f'Image height exceeds maximum ({invalid_height}/1000)']
    }

def test_valid_height():
    '''
    Returns a boolean if height is valid
    '''
    failure_file_path = IMAGE_LOCATION + 'Random_pyramids.jpeg'
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'

    assert valid_height(success_file_path) is True
    assert valid_height(failure_file_path) is False

def test_valid_file_size():
    '''
    Returns a boolean if file is valid size
    '''
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    failure_file_path = IMAGE_LOCATION + 'SampleJPGImage_15mbmb.jpg'

    assert valid_file_size(success_file_path) is True
    assert valid_file_size(failure_file_path) is False

def test_valid_image_file_type():
    '''
    Returns a boolean if file is correct image file type
    '''
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    failure_file_path = IMAGE_LOCATION + 'png-image.png'

    assert valid_image_file_type(success_file_path) is True
    assert valid_image_file_type(failure_file_path) is False

def test_valid_image_file():
    '''
    Returns a boolean if file is an image
    '''
    image_file = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    non_image_file = IMAGE_LOCATION + 'non_image_file.txt'

    assert valid_image_file(image_file) is True
    assert valid_image_file(non_image_file) is False

def test_validate_file_size():
    '''
    Returns an errors object with file size validation
    '''
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    failure_file_path = IMAGE_LOCATION + 'SampleJPGImage_15mbmb.jpg'

    assert not validate_file_size(success_file_path)
    assert validate_file_size(failure_file_path) == {
      "file_size" :  ['File size must be less than 10MB']
    }

def test_validate_image_file_type():
    '''
    Returns an errors object with image file type validation
    '''
    success_file_path = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    failure_file_path = IMAGE_LOCATION + 'png-image.png'

    assert not validate_image_file_type(success_file_path)
    assert validate_image_file_type(failure_file_path) == {
      "format" : ['Image format is not JPEG']
    }

def test_validate_image_file():
    '''
    Returns an errors object with isImage? validation
    '''
    image_file = IMAGE_LOCATION + 'butterfly-blue-insect-drawing.jpeg'
    non_image_file = IMAGE_LOCATION + 'non_image_file.txt'

    assert not validate_image_file(image_file)
    assert validate_image_file(non_image_file) == {
      "file_type" : 'File must be a valid image file'
    }
