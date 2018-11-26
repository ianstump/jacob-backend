from django.contrib import admin

from project.base.apps.tags.models import Document_tags, Pdf_documents, Highlighted_text

admin.site.register(Document_tags)
admin.site.register(Pdf_documents)
admin.site.register(Highlighted_text)
