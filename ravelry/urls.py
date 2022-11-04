from django.urls import path

from .views import YarnList

urlpatterns = [
    path('yarns/', YarnList.as_view(), name='yarn-list'),
]
