import os
import openai
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

application = Flask(__name__)

@application.before_first_request
def before_first_request() -> None:
    """
    This function is called before the first request is processed.
    It get the hash of the current run.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")


import service.routes
