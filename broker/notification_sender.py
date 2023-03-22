import requests


class NotificationSender:
    def __init__(self, image_data):
        self.on_success = image_data["notifications"]["onSuccess"]
        self.on_failure = image_data["notifications"]["onFailure"]
        self.on_start = image_data["notifications"]["onstart"]
        self.id = image_data["id"]
        self.errors = image_data["errors"]

    def send_start_notification(self):
        webhook_url = self.on_start
        payload = {
            "id": self.id,
            "state": "started",
        }
        requests.post(webhook_url, payload, timeout=5)

    def send_failure_notification(self):
        webhook_url = self.on_failure
        payload = {"id": self.id, "state": "failed", "errors": self.errors}
        requests.post(webhook_url, payload, timeout=5)

    def send_success_notification(self):
        webhook_url = self.on_success
        payload = {
            "id": self.id,
            "state": "success",
        }
        requests.post(webhook_url, payload, timeout=5)
