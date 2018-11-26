# !/usr/bin/env python

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.views import APIView
import os

from project.base.apps.tags.models import Pdf_documents
import subprocess


class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        print("name of file", myfile)
        fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # file_name = f'/media-files/{filename}'
        instance = Pdf_documents(report=myfile)
        instance.save()
        success = subprocess.call(f'pdf2htmlEX --zoom 1.3 /backend/pdfs/{myfile}')
        print(success)
        # print("filename", file_name)
        return HttpResponse("Working upload")
