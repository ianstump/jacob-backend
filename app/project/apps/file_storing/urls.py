from django.urls import path

# from project.apps.file_storing import views
from project.apps.file_storing.views import FileView

urlpatterns = [
    path('upload/', FileView.as_view(), name='storing_file'),
]
