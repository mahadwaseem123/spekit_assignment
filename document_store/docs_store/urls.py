from django.urls import path
from django.shortcuts import redirect
from .views import FolderList, FolderDetail, DocumentList, DocumentDetail, TopicList, TopicDetail, FolderDocumentTopicView


urlpatterns = [
    path('folders/', FolderList.as_view()),
    path('', lambda req: redirect('/folders/')),
    path('folders/<int:pk>/', FolderDetail.as_view()),
    path('documents/', DocumentList.as_view()),
    path('documents/<int:pk>/', DocumentDetail.as_view()),
    path('topics/', TopicList.as_view()),
    path("folders/<str:folder_name>/<str:topic_short_desc>/", FolderDocumentTopicView.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),
]
