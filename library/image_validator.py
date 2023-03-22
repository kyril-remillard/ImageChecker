'''ImageValidator validates all the image attributes and returns an errors object.'''

from library.library_functions import (
    validate_image_file, validate_image_dimensions,
    validate_file_size, validate_image_file_type
)

class ImageValidator:
    '''ImageValidator validates all the image attributes and returns an errors object.'''
    def __init__(self, file_path):
        self.image_path = file_path
        self.errors = {}

    def validate_image(self):
        '''validates all the image attributes and returns an errors object.'''
        self.errors.update(validate_image_file(self.image_path))
        if self.errors:
            return self.errors

        self.errors.update(validate_image_dimensions(self.image_path))
        self.errors.update(validate_file_size(self.image_path))
        self.errors.update(validate_image_file_type(self.image_path))

        return self.errors

    def notify(self):
        '''notifies the webhook urls of validation state changes'''
