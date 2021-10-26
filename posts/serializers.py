from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    title = serializers.CharField(max_length=250, required=True)
    content = serializers.CharField(required=True)
    likes = serializers.IntegerField(required=False)
