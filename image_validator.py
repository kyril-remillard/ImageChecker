from helper_functions import is_accessible, validate_image_attributes, send_start_notification, send_failure_notification, send_success_notification, set_validation_state


def validate_image(image_data):
  # STEP 1: Notify validation start
  set_validation_state(image_data["id"], "started")
  send_start_notification(image_data)
  
  errors = {}
  
  image_path = image_data["image_path"]
  
  # STEP 2: Check if image is accessible by the server
  if not is_accessible(image_path):
    errors["access"] = 'File is not reachable by the server'
    set_validation_state(image_data["id"], "failed")
    send_failure_notification(image_path, errors)
    return
  
  # STEP 3: Validate image attributes: height, width, file size & file type
  errors = validate_image_attributes(image_path)
  
  if errors:
    set_validation_state(image_data["id"], "failed")
    send_failure_notification(image_path, errors)
    return
  
  else:
    set_validation_state(image_data["id"], "success")
    send_success_notification(image_data)
    return
