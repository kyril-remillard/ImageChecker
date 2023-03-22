'''
Contains all helper functions used in the api
'''
import validators


def file_is_accessible(file_path):
    try:
        open(file_path, "r")
        return True
    except FileNotFoundError:
        return False


def validate_file_access(file_path):
    errors = {}

    if not file_is_accessible(file_path):
        errors["file access"] = "File is not accessible"

    return errors


def valid_url(url):
    if not validators.url(url):
        return False
    return True


def validate_urls(notifications):
    errors = {}

    for notification, url in notifications.items():
        if not valid_url(url):
            errors[f"{notification}"] = f"{url} is not a valid url"

    return errors
