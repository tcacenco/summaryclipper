from service.app import application
from service.app_tools import extract_utils, text_utils
import service.constants as const
from flask import Flask, jsonify, request, make_response
import flask
from ddtrace import tracer


@tracer.wrap(name="index")
@application.route("/")
def index():
    """
    Index endpoint
    No usage attached to it, just returns root node
    access message

    Returns:
        a string with the root node access message
    """
    return const.ROOT_MESSAGE


@tracer.wrap(name="health")
@application.route("/health", methods=["GET"])
def health() -> flask.Response:
    """
    The health check endpoint of the application.

    Returns:
        response: The status of the application.
    """
    response = {"message": "ok"}
    return make_response(jsonify(response), 200)


@tracer.wrap(name="summarize_video")
@application.route("/summarize_video", methods=["POST"])
def summarize_video() -> flask.Response:
    """
    The summarize video endpoint of the application.

    Returns:
        response: The status of the application.
    """
    input = {
        "youtube_url": request.form.get("youtube_url", None),
        "language": request.form.get("language", None),
    }
    print(input)

    try:
        dict_result = extract_utils.download_audio_from_youtube(
            youtube_url=input["youtube_url"], output_path=const.DOWNLOAD_PATH
        )
        dict_result["full_text"] = text_utils.speech_to_text(
            const.DOWNLOAD_PATH + dict_result["filename"]
        )
        dict_result["summary"] = text_utils.text_completion(
            dict_result["full_text"]
        )

        response = dict_result
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(e)
        response = {"message": str(e)}
        return make_response(jsonify(response), 500)
