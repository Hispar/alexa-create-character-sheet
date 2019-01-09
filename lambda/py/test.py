from custom.template_manager import TemplateManager
from weasyprint import HTML

# config = pdfkit.configuration(wkhtmltopdf="binaries/wkhtmltopdf")

template = TemplateManager(name="Pepe", clan="brujah")

# pdf = pdfkit.from_url('http://google.com', False)
# pdfkit.from_string(template.get_body(), 'out.pdf', configuration=config)

HTML(string=template.get_body()).write_pdf('out.pdf')
