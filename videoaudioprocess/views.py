# views.py
import os
from django.conf import settings
from django.http import HttpResponse
import subprocess
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi


def run_subprocess_view(request):
    parameter1 = request.GET.get("url", None)
    video_id = get_youtube_video_id(parameter1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for text in transcript:
        result += f"{text['text']} "

    try:
        current_directory = os.path.dirname(__file__)
        script_path = os.path.join(current_directory, "process", "frameextracter.py")
        subprocess.run(["python", script_path, parameter1])
        script_path4 = os.path.join(current_directory, "process", "audio.py")
        subprocess.run(["python", script_path4, result])
        script_path_2 = os.path.join(current_directory, "process", "videoconverter.py")
        subprocess.run(["python", script_path_2])
        script_path_5 = os.path.join(current_directory, "process", "del.py")
        subprocess.run(["python", script_path_5])
        script_path_3 = os.path.join(current_directory, "process", "mirger.py")
        subprocess.run(["python", script_path_3])
        file_path = os.path.join(current_directory)
        l1 = os.path.abspath(os.path.join(file_path, os.pardir))
        # l2 = os.path.abspath(os.path.join(l1, os.pardir))
        file_name = "final_video.mp4"
        video_path = os.path.join(l1, file_name)
        print("parent", video_path)
        if not os.path.exists(video_path):
            return HttpResponse("Not Found", status=404)
        with open(video_path, "rb") as video_file:
            response = HttpResponse(video_file.read(), content_type="video/mp4")
            response["Content-Disposition"] = f'inline; filename="{video_path}"'
            return response

        # response = HttpResponse()
        # response["Content-Type"] = "video/mp4"
        # response["X-Sendfile"] = video_path
        # return response
        # return HttpResponse("Script executed successfully")
    except Exception as e:
        return HttpResponse(f"Error executing script: {e}")


import re


def get_youtube_video_id(link):
    """Extracts the YouTube video ID from a given link.

    Args:
        link (str): The YouTube video URL.

    Returns:
        str: The YouTube video ID, or None if no ID was found.
    """

    patterns = [
        r"youtube\.com/watch\?.*?v=([^&#]*)",  # Standard watch links
        r"youtu\.be/([^?#]*)",  # Shortened links
    ]

    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1)

    return None  # No match found
