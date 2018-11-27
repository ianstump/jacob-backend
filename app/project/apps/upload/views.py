from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from project.base.apps.tags.models import PdfDocuments
from project.apps.upload.serializer import FileSerializer


class FileView(APIView):
    """
    View to upload file, convert it to html and text.
    """
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        instance = PdfDocuments(pdf=myfile)
        instance.save()
        return HttpResponse("Working upload")


class GetPdfs(ListAPIView):
    """
    View to get pdf related information based on the id of the pdfs passed in the GET request.
    """
    permission_classes = []
    serializer_class = FileSerializer

    def get_queryset(self):
        params = self.request.query_params
        indexes = []
        for param in params:
            indexes.append(params[param])
        return PdfDocuments.objects.filter(id__in=indexes)

class GetAllPdfs(ListAPIView):
    """
    View to get all pdf info.
    """
    permission_classes = []
    serializer_class = FileSerializer

    def get_queryset(self):
        return PdfDocuments.objects.all()

