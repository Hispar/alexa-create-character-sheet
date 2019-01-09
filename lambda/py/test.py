import io

from custom.template_manager import TemplateManager

# config = pdfkit.configuration(wkhtmltopdf="binaries/wkhtmltopdf")

template = TemplateManager(name="Pepe", clan="brujah")

print(template.get_html())
fileobj = io.StringIO()
x = template.get_document(fileobj)
# pdf = pdfkit.from_url('http://google.com', False)
# pdfkit.from_string(template.get_body(), 'out.pdf', configuration=config)

# HTML(string=template.get_body()).write_pdf('out.pdf')
