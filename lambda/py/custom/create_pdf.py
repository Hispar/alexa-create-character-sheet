# -*- coding: utf-8 -*-
# Python imports
import logging

# 3rd party imports
from weasyprint import HTML

# App imports

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# config = pdfkit.configuration(wkhtmltopdf="binaries/wkhtmltopdf")


class PdfRenderer(object):

    # Utility function
    def generate(self, html):
        # result_file2 = open('binaries/wkhtmltopdf', "r")
        # logger.info(result_file2)

        # convert HTML to PDF
        return HTML(string=html).write_pdf()
        # return pdfkit.from_string(html, False)
        # pisa_status = pisa.CreatePDF(
        #     html  # the HTML to convert
        # )  # file handle to recieve result
        #
        # # close output file
        # # result_file.close()  # close output file

        # return pisa_status.dest
