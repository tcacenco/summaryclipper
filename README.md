# Summary Clipper

Summary Clipper is a backend application developed to extract and summarize audio from YouTube videos. It currently has two developed endpoints:
- /health
- /summarize_video

The latter will use OpenAI's Whisper speech-to-text model (tiny) to create a transcription of the audio downloaded. The application send a request to OpenAI API to get a summary of the transcribed audio using GPT-3.5.
