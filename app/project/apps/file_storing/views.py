from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .serializer import FileSerializer
from rest_framework.response import Response


class FileView(APIView):
    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        file_name = f'/media-files/documents/{filename}'
        print("filename", file_name)
        return HttpResponse("Working upload")
