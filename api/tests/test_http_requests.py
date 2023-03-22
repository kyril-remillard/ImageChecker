from flask import Flask
import json
import sys
sys.path.append('..//api')
from api.routes import configure_routes
POST_URL = "http://127.0.0.1:5000/assets/images"

def test_post_route_success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    mock_request_headers = {
      'Content-Type': 'application/json'
    }
    mock_request_data = {
      "assetPath": { 
          "location": "/Users/kyrildoubson-remillard/Desktop/image_checker/",
          "path": "test_images/butterfly-blue-insect-drawing.jpeg"
      },
      "notifications": {
      "onStart": "http://somevalidurl.com",
      "onSuccess": "http://somevalidurl.com",
      "onFailure": "http://somevalidurl.com"
      }
    }
    response = client.post(POST_URL, data=json.dumps(mock_request_data), headers=mock_request_headers)
    
    assert response.status_code == 202
    assert json.loads(response.data)["state"] == "queued"

def test_post_route_failure_file_not_found():
  app = Flask(__name__)
  configure_routes(app)
  client = app.test_client()
  
  mock_request_headers = {
    'Content-Type': 'application/json'
  }
  mock_request_data = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/image_checker/",
        "path": "invalid_path"
    },
    "notifications": {
    "onStart": "http://somevalidurl.com",
    "onSuccess": "http://somevalidurl.com",
    "onFailure": "http://somevalidurl.com"
    }
  }
  response = client.post(POST_URL, data=json.dumps(mock_request_data), headers=mock_request_headers)
  expected_response = {
    "errors": {
        "file access": "File is not accessible"
    },
    "state": "failed"
  }
  assert response.status_code == 400
  assert json.loads(response.data) == expected_response
  
def test_post_route_failure_invalid_notification_urls():
  app = Flask(__name__)
  configure_routes(app)
  client = app.test_client()
  
  mock_request_headers = {
    'Content-Type': 'application/json'
  }
  mock_request_data = {
    "assetPath": { 
        "location": "/Users/kyrildoubson-remillard/Desktop/image_checker/",
        "path": "test_images/Random_pyramids.jpeg"
        
    },
    "notifications": {
     "onStart": "invalid_url_1",
     "onSuccess": "invalid_url_2",
     "onFailure": "invalid_url_3"
   }
}
  response = client.post(POST_URL, data=json.dumps(mock_request_data), headers=mock_request_headers)
  expected_response = {
    "errors": {
        "onFailure": "invalid_url_3 is not a valid url",
        "onStart": "invalid_url_1 is not a valid url",
        "onSuccess": "invalid_url_2 is not a valid url"
    },
    "state": "failed"
  }
  assert response.status_code == 400
  assert json.loads(response.data) == expected_response
