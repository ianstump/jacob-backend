from django.urls import path

from project.apps.tags.views import GetTags

urlpatterns = [
    path('', GetTags.as_view(), name='get-tags'),


]
