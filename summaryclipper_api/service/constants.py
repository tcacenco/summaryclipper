import os

ROOT_MESSAGE = "Welcome to Summary Clipper. This is the root node of the API. Please refer to the documentation for more information."

VIDEO_EXTENSION = ".mp4"
AUDIO_EXTENSION = ".mp3"
MP3_BIT_RATE = "256k"
DOWNLOAD_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "downloads", ""
)

GPT_TURBO_MODEL = "gpt-3.5-turbo"
GPT_SYSTEM_CONTENT = "You are a helpful text organizer. You will first provide a summary on how to navigate through the text that you are rewritting. Then you will reorganize the entire text provided to you and make it more concise and of easy understanding. You will also summarize the parts that are long and repetitive and also whenever it makes sense to summaryze.\nThe text that you are rewritting was extracted from a Youtube video using a speech to text tool. Therefore, it may have a lot of typos. You will refer to the content as a video even though I am providing a text instead of a video."
GPT_PROMPT_PREFIX = "The text below was extracted from a Youtube video. Please organize and rewrite it, highlighting key aspects when possible.\n\n"
