from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PdfDocuments
from .helpers import converting_pdf_to_html, converting_pdf_to_text


@receiver(post_save, sender=PdfDocuments)
def convert_pdf_html(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.html_created:
        converting_pdf_to_html(instance.pdf)
        instance.html_created = True
        instance.save()
    if not instance.text_created:
        converting_pdf_to_text(instance)
        instance.save()
