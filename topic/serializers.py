from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.Serializer):
    class Meta:
        model = Topic
        fields ='__all__'