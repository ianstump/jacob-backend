from django.urls import path

from project.apps.tags.views import GetTags, GetHighlightedTextOfTag

urlpatterns = [
    path('', GetTags.as_view(), name='get-tags'),
    path('phrases/<int:pk>/', GetHighlightedTextOfTag.as_view(), name='get-phrases')

]
