import requests

BASE = "http://127.0.0.1:5000/"


jpeg_image_payload_failure = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/ImgChkr/",
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
        "location": "/Users/kyrildoubson-remillard/Desktop/ImgChkr/",
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
        "location": "/Users/kyrildoubson-remillard/Desktop/ImgChkr/",
        "path": "test_images/png-image.png"
        
    },
    "notifications": {
     "onStart": "http://somevalidurl.com",
     "onSuccess": "http://somevalidurl.com",
     "onFailure": "http://somevalidurl.com"
   }
}


# TEST CASES

response = requests.post(BASE, json = jpeg_image_payload_failure)
print(response.json())

response = requests.post(BASE, json = jpeg_image_payload_success)
print(response.json())

response = requests.post(BASE, json = png_image_payload_failure)
print(response.json())


