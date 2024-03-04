# subtitles_api/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from youtube_transcript_api import YouTubeTranscriptApi


@api_view(['GET'])
def get_subtitles(request, video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = [entry['text'] for entry in transcript]
        return Response({'subtitles': subtitles})
    except Exception as e:
        return Response({'error': str(e)})
