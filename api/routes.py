import uuid
from flask import request, jsonify
from api_request_validator import ApiRequestValidator



def configure_routes(app):
    @app.route("/assets/images", methods=["POST"])
    def handle_request():
        errors = ApiRequestValidator(request.get_json()).validate_post_request()

        if errors:
            response = {"state": "failed", "errors": errors}
            return jsonify(response), 400

        image_id = uuid.uuid4()
        # TODO: implement --> send image_id && the request data to the Broker
        # it will add it to the database and add it to the queue

        response = {
            "id": image_id,
            "state": "queued",
        }
        return jsonify(response), 202

    @app.route("/assets/images/<id>", methods=["GET"])
    def get_image_info(id):
        return jsonify(id), 200
        # if id in labelbox_image_data:
        #   response = {
        #     "id" : id,
        #     "state" : labelbox_image_data[id]["state"]
        #   }
        #   return jsonify(response), 200
        # else:
        #   response = {
        #     "errors" : f'the provided image id is invalid [{id}]'
        #   }
        #   return jsonify(response), 404
