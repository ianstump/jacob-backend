from rest_framework.generics import ListAPIView

from project.apps.tags.serializers import TagsSerializer
from project.base.apps.tags.models import Document_tags


class GetTags(ListAPIView):
    queryset = Document_tags.objects.all()
    serializer_class = TagsSerializer