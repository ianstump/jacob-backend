from django.urls import path

from project.apps.annotations.views import AnnotateText, GetAllHighlights

urlpatterns = [
    path('', AnnotateText.as_view(), name='annotated-text'),
    path('all/', GetAllHighlights.as_view(), name='get-annotated-text'),

]
