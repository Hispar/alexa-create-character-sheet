# -*- coding: utf-8 -*-
# Python imports
import logging
import os

# 3rd party imports
import pdfkit

# App imports

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
here = lambda *x: os.path.abspath(os.path.join(BASE_DIR, *x))

binary_path = here('wkhtmltopdf')
configuration = pdfkit.configuration(wkhtmltopdf=binary_path)


class PdfRenderer(object):

    def generate(self, html):
        return pdfkit.from_string(html, False, configuration=configuration)
