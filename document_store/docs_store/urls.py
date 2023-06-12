from django.urls import path
from .views import FolderList, FolderDetail, DocumentList, DocumentDetail, TopicList, TopicDetail


urlpatterns = [
    path('folders/', FolderList.as_view()),
    path('folders/<int:pk>/', FolderDetail.as_view()),
    path('documents/', DocumentList.as_view()),
    path('documents/<int:pk>/', DocumentDetail.as_view()),
    path('topics/', TopicList.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),
]
