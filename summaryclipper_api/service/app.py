import os
import openai
from flask import Flask
from dotenv import load_dotenv
from ddtrace import tracer

load_dotenv()


application = Flask(__name__)

tracer.configure(
    hostname="datadog-agent",
    port=8126,
)


@application.before_first_request
def before_first_request() -> None:
    """
    This function is called before the first request is processed.
    It get the hash of the current run.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")


import service.routes
