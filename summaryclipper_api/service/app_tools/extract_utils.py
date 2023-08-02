import os
import service.constants as const
from pytube import YouTube
from pydub import AudioSegment


def save_compressed_audio(
    input_video_path, compressed_mp3_path, bitrate="256k"
):
    """
    Save compressed audio file from a video file

    Parameters:
        input_video_path (str): Path to the input video file
        compressed_mp3_path (str): Path to save the compressed audio file
        bitrate (str): Bitrate of the compressed audio file

    Returns:
        None
    """

    try:
        audio = AudioSegment.from_file(input_video_path, format="mp4")
        audio.export(compressed_mp3_path, format="mp3", bitrate=bitrate)
        print(f"MP3 file compressed and saved as {compressed_mp3_path}")
    except Exception as e:
        print(f"Error: {e}")


def download_audio_from_youtube(youtube_url, output_path):
    """
    Download audio from a YouTube video

    Parameters:
        youtube_url (str): YouTube video URL
        output_path (str): Path to save the audio file
    Returns:
        response (dict): The status of the function along with filename.
    """
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)

        # Get the best available video stream
        audio_stream = yt.streams.first()

        print("Downloading video...")
        # Download the video stream to a temporary location (MP4 format)
        if youtube_url.__contains__("www.youtube.com/watch?v="):
            filename = (
                youtube_url.split("www.youtube.com/watch?v=")[1]
                + const.VIDEO_EXTENSION
            )
        tmp_video_path = audio_stream.download(
            output_path=output_path, filename=filename
        )

        print("Video download successful!")

        audio_file_path = tmp_video_path.replace(
            const.VIDEO_EXTENSION, const.AUDIO_EXTENSION
        )

        print("Extracting audio...")
        save_compressed_audio(
            tmp_video_path, audio_file_path, bitrate=const.MP3_BIT_RATE
        )
        print("Audio extraction successful!")

        os.remove(tmp_video_path)

        return {
            "filename": os.path.basename(audio_file_path),
            "success": True,
            "error_message": None,
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "filename": None,
            "success": False,
            "error_message": str(e),
        }
