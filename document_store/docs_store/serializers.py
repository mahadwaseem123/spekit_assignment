from rest_framework import serializers
from .models import Folder, Document, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)
    #documents = serializers.StringRelatedField(many=True)

    class Meta:
        model = Folder
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Document
        fields = '__all__'


