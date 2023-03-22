'''
Class returns an errors object that contains all validation errors found during 
an api request. It is instantiated with the image_data and will test the following:
  - Is the file accessible?
  - are the webhook notification urls valid?
'''
from api_functions import validate_file_access, validate_urls


class ApiRequestValidator:
    def __init__(self, image_data):
        self.image_path = (
            image_data["assetPath"]["location"] + image_data["assetPath"]["path"]
        )
        self.notifications = image_data["notifications"]
        self.errors = {}

    def validate_post_request(self):
        ''' 
        runs the validations and updates the errors object 
        '''
        self.errors.update(validate_file_access(self.image_path))
        self.errors.update(validate_urls(self.notifications))
        return self.errors
