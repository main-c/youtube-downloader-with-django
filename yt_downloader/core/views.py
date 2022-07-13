from pytube import YouTube
from rest_framework.response import Response
from core.serializers import (
    AudioSerializer,
    StreamSerializer,
    UrlSerializer,
    YtSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework import status


class DownloadView(GenericAPIView):
    serializer_class = UrlSerializer
    queryset = []

    def post(self, request, *args, **kwargs):
        serializer = UrlSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data.get("url")
        yt = YouTube(url)

        yt_file = YtSerializer(
            instance={
                "title": yt.title,
                "thumbnail_url": yt.thumbnail_url,
                "channel_id": yt.channel_id,
                "channel_url": yt.channel_url,
                "length": yt.length,
            }
        )
        stream_list = []
        for stream in yt.streams.filter(only_audio=True):
            instance = {
                "yt": yt_file.data,
                "default_filename": stream.default_filename,
                "filesize": stream.filesize,
                "extension": stream.mime_type,
                "resolution": stream.abr,
            }
            stream_list.append(instance)
        stream_serializer = StreamSerializer(stream_list, many=True)
        return Response(stream_serializer.data, status=status.HTTP_200_OK)
