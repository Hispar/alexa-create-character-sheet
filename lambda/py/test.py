import io

from custom.template_manager import TemplateManager
from custom.mailer import Mailer


# config = pdfkit.configuration(wkhtmltopdf="binaries/wkhtmltopdf")

template = TemplateManager(name="Pepe", clan="brujah")

# print(template.get_html())
# fileobj = io.StringIO()
# x = template.get_document(fileobj)

# bytesObj = io.BytesIO()
# bytesObj.write(str(fileobj).encode('utf-8'))
# Convert to a "unicode" object
# text_obj = byte_str.decode('UTF-8')
document = template.get_html()
# print(document.decode('utf8'))
print(document.encode('utf8'))
mail = Mailer()
mail.create_mail(subject='a', sender='s', recipient='s', body=document)
mail.create_attachment(document, 'personaje.html')

print(document)
# mail.send()
# pdf = pdfkit.from_url('http://google.com', False)
# pdfkit.from_string(template.get_body(), 'out.pdf', configuration=config)

# HTML(string=template.get_body()).write_pdf('out.pdf')
