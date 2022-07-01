from django.shortcuts import render
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer
from rest_framework.views import APIView
# Create your views here.
class TopicList(APIView):
    def get(self, request):
        Topics = Topic.objects.all()
        data= TopicSerializer(Topics, many=True).data
        return Response(data)