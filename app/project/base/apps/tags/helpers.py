import os

import pdftotext
from django.conf import settings


def converting_pdf_to_text(instance):
    myfile = instance.pdf
    with open(f'{settings.MEDIA_ROOT}/{myfile}', "rb") as f:
        pdf = pdftotext.PDF(f)
        complete_pdf = ("\n\n".join(pdf))
        # uncommented for formatting
        # complete_pdf_no_ext_spaces = ' '.join(complete_pdf.split())
        instance.text = complete_pdf
        instance.text_created = True
        instance.save()


def converting_pdf_to_html(myfile):
    os.system(f'pdf2htmlEX --zoom 1.3 {settings.MEDIA_ROOT}/{myfile} --dest-dir {settings.MEDIA_ROOT}/htmls/')
