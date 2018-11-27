from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
# from django.core.files.storage import FileSystemStorage
from project.apps.file_storing.serializer import FileSerializer
from project.base.apps.tags.models import Pdf_documents


class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # file_name = f'/media-files/{filename}'
        instance = Pdf_documents(report=myfile)
        instance.save()
        # print("filename", file_name)s
        return HttpResponse("Working upload")



class GetPdfs(ListAPIView):
    permission_classes = []
    serializer_class = FileSerializer

    def get_queryset(self):
        params = self.request.query_params
        indexes = []
        for param in params:
            indexes.append(params[param])
        return Pdf_documents.objects.filter(id__in=indexes)
