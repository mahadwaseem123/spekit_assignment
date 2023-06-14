from django.shortcuts import render

from rest_framework import generics
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from .models import Folder, Document, Topic
from .serializers import FolderSerializer, DocumentSerializer, TopicSerializer


class FolderList(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    #authentication_classes = [authentication.BasicAuthentication]
    #permission_classes = [IsAuthenticated]


class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FolderDocumentTopicView(generics.ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        topic_short_desc = self.kwargs["topic_short_desc"]
        folder_name = self.kwargs["folder_name"]
        queryset = Document.objects.filter(
            topics__short_desc=topic_short_desc,
            folder__name=folder_name,
        )
        return queryset



