import sys
sys.path.append("..")
from library.image_validator import ImageValidator

IMAGE_LOCATION = '/Users/kyrildoubson-remillard/Desktop/image_checker/test_images/'

def test_image_validation_for_image_with_no_errors():
    '''
    as title says
    '''
    file_path = IMAGE_LOCATION + "butterfly-blue-insect-drawing.jpeg"
    image_validator = ImageValidator(file_path)

    assert not image_validator.validate_image()


def test_image_validation_for_image_with_dimension_errors():
    '''
    as title says
    '''
    file_path = IMAGE_LOCATION + "Random_pyramids.jpeg"
    image_validator = ImageValidator(file_path)
    width = 2048
    height = 1536

    assert image_validator.validate_image() == {
        "image": [
            f"Image width exceeds maximum ({width}/1000)",
            f"Image height exceeds maximum ({height}/1000)",
        ]
    }


def test_image_validation_for_image_with_image_file_type_error():
    '''
    as title says
    '''
    file_path = IMAGE_LOCATION + "png-image.png"
    image_validator = ImageValidator(file_path)

    assert image_validator.validate_image() == {"format": ["Image format is not JPEG"]}


def test_image_validation_for_non_image_file():
    '''
    as title says
    '''
    file_path = "/Users/kyrildoubson-remillard/Desktop/image_checker/api/routes.py"
    image_validator = ImageValidator(file_path)

    assert image_validator.validate_image() == {
        "file_type": "File must be a valid image file"
    }


def test_image_validation_for_file_exceeding_file_size_and_dimensions():
    '''
    as title says
    '''
    file_path = IMAGE_LOCATION + "SampleJPGImage_15mbmb.jpg"
    image_validator = ImageValidator(file_path)
    width = 10212
    height = 6806

    assert image_validator.validate_image() == {
        "file_size": ["File size must be less than 10MB"],
        "image": [
            f"Image width exceeds maximum ({width}/1000)",
            f"Image height exceeds maximum ({height}/1000)",
        ],
    }
