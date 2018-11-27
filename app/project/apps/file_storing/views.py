# !/usr/bin/env python
import time
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
import os
from project.base.apps.tags.models import Pdf_documents
from project.apps.file_storing.serializer import FileSerializer


class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        instance = Pdf_documents(report=myfile)
        instance.save()
        return HttpResponse("Working upload")

    def convertingPDFtoHTML(self, myfile):
        while not os.path.exists(f'/pdfs/{myfile}'):
            time.sleep(1)
        if os.path.isfile(f'/pdfs/{myfile}'):
            os.system(f'pdf2htmlEX --zoom 1.3 /pdfs/{myfile} --dest-dir /htmls/')




class GetPdfs(ListAPIView):
    permission_classes = []
    serializer_class = FileSerializer

    def get_queryset(self):
        params = self.request.query_params
        indexes = []
        for param in params:
            indexes.append(params[param])
        return Pdf_documents.objects.filter(id__in=indexes)

