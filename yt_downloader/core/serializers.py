from dataclasses import fields
from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=250, required=True)

    class Meta:
        fields = ("url",)


class YtSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250, required=True)
    thumbnail_url = serializers.CharField(max_length=250, required=True)
    channel_id = serializers.CharField(max_length=250)
    channel_url = serializers.CharField(max_length=250)
    length = serializers.IntegerField()

    class Meta:

        fields = (
            "title",
            "thumbnail_url",
            "channel_id",
            "channel_url",
            "length",
        )


class StreamSerializer(serializers.Serializer):
    yt = YtSerializer(read_only=True)
    default_filename = serializers.CharField(max_length=250, required=True)
    filesize = serializers.IntegerField()
    extension = serializers.CharField(max_length=10, required=True)
    resolution = serializers.CharField(max_length=10, required=True)

    class Meta:
        fields = ("yt", "default_filename", "filesize", "extension", "resolution")


class AudioSerializer(serializers.Serializer):
    stream = StreamSerializer(many=True)

    class Meta:
        fields = "stream"


class VideoSerializer(serializers.Serializer):
    stream = StreamSerializer(many=True)
    resolution = serializers.CharField(max_length=10, required=True)

    class Meta:
        fields = ("streal", "resolution")
