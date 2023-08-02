import os
import service.constants as const
import whisper
import openai


def speech_to_text(mp3_file_path):
    """
    Convert speech to text using Mozilla's DeepSpeech library

    Parameters:
        mp3_file_path (str): Path to the MP3 file

    Returns:
        result (str): The text extracted from the speech
    """
    print("Running whisper speech to text ...")
    model = whisper.load_model("tiny")
    result = model.transcribe(mp3_file_path)
    print("Text extractiom successful!")
    return result["text"]


def text_completion(prompt_input) -> str:
    print("OpenAI Chat Completion API call ...")

    new_prompt = const.GPT_PROMPT_PREFIX + prompt_input

    completion = openai.ChatCompletion.create(
        model=const.GPT_TURBO_MODEL,
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": new_prompt},
        ],
    )
    print("OpenAI Chat Completion API call successful!")
    return completion.choices[0].message.content
