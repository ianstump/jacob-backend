from rest_framework.generics import ListAPIView
from project.apps.tags.serializers import TagsSerializer, HighlightedTextSerializer
from project.base.apps.tags.models import Document_tags, Highlighted_text


class GetTags(ListAPIView):
    queryset = Document_tags.objects.all()
    serializer_class = TagsSerializer


class GetHighlightedTextOfTag(ListAPIView):
    serializer_class = HighlightedTextSerializer

    def get_queryset(self):
        return Highlighted_text.objects.filter(pdf_documents=self.kwargs['pk'])
