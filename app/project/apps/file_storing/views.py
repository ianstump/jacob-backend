import time

from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from project.base.apps.tags.models import Pdf_documents
from project.apps.file_storing.serializer import FileSerializer
import os
import pdftotext

class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        instance = Pdf_documents(report=myfile)
        instance.save()
        return HttpResponse("Working upload")

    """ the next function converts the pdf directly to text and saves it into the Pdf_documents model
     with a relation to report """

    def convertingPDFtoText(self, myfile):
        while not os.path.exists(f'/pdfs/{myfile}'):
            time.sleep(1)
        if os.path.isfile(f'/pdfs/{myfile}'):
            with open(f'/pdfs/{myfile}', "rb") as f:
                pdf = pdftotext.PDF(f)
                complete_pdf = ("\n\n".join(pdf))
                instance = Pdf_documents(report=myfile, text_document=complete_pdf)
                instance.save()


class GetPdfs(ListAPIView):
    permission_classes = []
    serializer_class = FileSerializer

    def get_queryset(self):
        params = self.request.query_params
        indexes = []
        for param in params:
            indexes.append(params[param])
        return Pdf_documents.objects.filter(id__in=indexes)