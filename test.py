import requests
import validators
from helper_functions import is_accessible, validate_image_attributes, validate_urls

post_url = "http://127.0.0.1:5000/assets/images"


jpeg_image_payload_failure = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/ImageChecker/",
        "path": "test_images/Random_pyramids.jpeg"
        
    },
    "notifications": {
     "onStart": "http://somevalidurl.com",
     "onSuccess": "http://somevalidurl.com",
     "onFailure": "http://somevalidurl.com"
   }
}

jpeg_image_payload_success = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/ImageChecker/",
        "path": "test_images/butterfly-blue-insect-drawing.jpeg"
        
    },
    "notifications": {
     "onStart": "http://somevalidurl.com",
     "onSuccess": "http://somevalidurl.com",
     "onFailure": "http://somevalidurl.com"
   }
}

png_image_payload_failure = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/ImageChecker/",
        "path": "test_images/png-image.png"
        
    },
    "notifications": {
     "onStart": "http://somevalidurl.com",
     "onSuccess": "http://somevalidurl.com",
     "onFailure": "http://somevalidurl.com"
   }
}


# TEST CASES

# response = requests.post(post_url, json = jpeg_image_payload_failure)
# print(response.json())

# response = requests.post(post_url, json = jpeg_image_payload_success)
# print(response.json())

# response = requests.post(post_url, json = png_image_payload_failure)
# print(response.json())



    
urls = ['www.google.ca', 'www.facebook.com']
# print(validate_urls(urls))

print(validators.url('https://wwww.google.com'))


png_image_payload_failure = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/ImageChecker/",
        "path": "test_images/png-image.png"
        
    },
    "notifications": {
     "onStart": "http://somevalidurl.com",
     "onSuccess": "http://somevalidurlm",
     "onFailure": "httsomevalidurl.com"
   }
}

# webhook_urls = [webhook_url for webhook_url in png_image_payload_failure["notifications"].items()]

# print(validators.url("httsomevalidurl.com"))

print(validate_urls(png_image_payload_failure["notifications"]))