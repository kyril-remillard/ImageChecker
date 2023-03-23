import sys

sys.path.append("..")
from api.api_functions import (
    file_is_accessible,
    valid_url,
    validate_urls,
    validate_file_access,
)


def test_file_is_accessible():
    valid_file_path = (
        "/Users/kyrildoubson-remillard/Desktop/image_checker/"
        + "test_images/butterfly-blue-insect-drawing.jpeg"
    )
    invalid_file_path = (
        "/Users/kyrildoubson-remillard/Desktop/image_checker/" + "/invalid_location"
    )
    assert file_is_accessible(valid_file_path) == True
    assert file_is_accessible(invalid_file_path) == False


def test_valid_url():
    valid_link = "http://somevalidurl.com"
    invalid_link = "invalid"

    assert valid_url(valid_link) == True
    assert valid_url(invalid_link) == False


def test_validate_urls():
    valid_notifications = {
        "onStart": "http://somevalidurl.com",
        "onSuccess": "http://somevalidurl.com",
        "onFailure": "http://somevalidurl.com",
    }
    invalid_notifications = {
        "onStart": "invalid_url",
        "onSuccess": "http://somevalidurl.com",
        "onFailure": "http://somevalidurl.com",
    }

    assert validate_urls(valid_notifications) == {}
    assert validate_urls(invalid_notifications) == {
        "onStart": "invalid_url is not a valid url"
    }


def test_validate_file_access():
    valid_file_path = (
        "/Users/kyrildoubson-remillard/Desktop/image_checker/"
        + "test_images/butterfly-blue-insect-drawing.jpeg"
    )
    invalid_file_path = (
        "/Users/kyrildoubson-remillard/Desktop/image_checker/" + "/invalid_location"
    )

    assert validate_file_access(valid_file_path) == {}
    assert validate_file_access(invalid_file_path) == {
        "file access": "File is not accessible"
    }
