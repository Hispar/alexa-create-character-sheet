# -*- coding: utf-8 -*-
# Python imports
import logging

# 3rd party imports
import pdfkit

# App imports

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

configuration = pdfkit.configuration(wkhtmltopdf='binaries/wkhtmltopdf')


class PdfRenderer(object):

    def generate(self, html):
        return pdfkit.from_string(html, False, configuration=configuration)
