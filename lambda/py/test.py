import pdfkit as pdfkit
from custom.template_manager import TemplateManager
from custom.mailer import Mailer


template = TemplateManager(name="Pepe", clan="brujah")

document = template.get_html()

mail = Mailer()
mail.create_mail(subject='a', sender='s', recipient='s', body=document)
mail.create_attachment(document, 'personaje.html')

# print(document)

# pdf = pdfkit.from_url('http://google.com', False)
# config = pdfkit.configuration(wkhtmltopdf="binaries/wkhtmltopdf")
pdfkit.from_string(document, 'out.pdf')
