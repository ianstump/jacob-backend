from django.urls import path
from project.apps.file_storing.views import FileView, GetPdfs

urlpatterns = [
    path('upload/', FileView.as_view(), name='storing_file'),
    path('get/', GetPdfs.as_view(), name='storing_file'),

]
