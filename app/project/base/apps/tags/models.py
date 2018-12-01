import os
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import pdftotext


class DocumentTags(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200,
    )

    pdf_documents = models.ManyToManyField(
        verbose_name='pdf_documents',
        related_name='document_tags',
        to='tags.PdfDocuments',
        blank=True
    )

    parent_tag = models.ForeignKey(
        verbose_name='parent_tag',
        related_name='children',
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    color = models.CharField(
        verbose_name='color',
        max_length=7
    )

    def __str__(self):
        return str(self.name)


class PdfDocuments(models.Model):
    pdf = models.FileField(upload_to='./pdfs', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="text", null=True)
    html_created = models.BooleanField(verbose_name='html_created', default=False)
    text_created = models.BooleanField(verbose_name='html_created', default=False)

    def __str__(self):
        return str(self.pdf)


@receiver(post_save, sender=PdfDocuments)
def convert_pdf_html(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.html_created:
        convertingPDFtoHTML(instance.pdf)
        instance.html_created = True
        instance.save()
    if not instance.text_created:
        convertingPDFtoText(instance)
        instance.save()


def convertingPDFtoText(instance):
    myfile = instance.pdf
    with open(f'{settings.MEDIA_ROOT}/{myfile}', "rb") as f:
        pdf = pdftotext.PDF(f)
        complete_pdf = ("\n\n".join(pdf))
        # uncommented for formatting
        # complete_pdf_no_ext_spaces = ' '.join(complete_pdf.split())
        instance.text = complete_pdf
        instance.text_created = True
        instance.save()


def convertingPDFtoHTML(myfile):
    os.system(f'pdf2htmlEX --zoom 1.3 {settings.MEDIA_ROOT}/{myfile} --dest-dir {settings.MEDIA_ROOT}/htmls/')


class HighlightedText(models.Model):
    selected_text = models.TextField(
        verbose_name='selected_text',
    )
    document_tags = models.ForeignKey(
        verbose_name='document_tags',
        related_name='highlighted_text',
        to='tags.DocumentTags',
        on_delete=models.CASCADE,

    )
    pdf_documents = models.ForeignKey(
        verbose_name='pdf_documents',
        related_name='highlighted_text',
        to='tags.PdfDocuments',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.selected_text)
