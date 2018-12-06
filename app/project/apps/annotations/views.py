from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from project.apps.annotations.serializers import HighlightedTextSerializer
from project.base.apps.tags.models import HighlightedText


class AnnotateText(APIView):
    """
    Annotate text in a document
    """

    def post(self, request, **kwargs):
        serializer = HighlightedTextSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            text = serializer.save()
        return Response(HighlightedTextSerializer(text).data)
