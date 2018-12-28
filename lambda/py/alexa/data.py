# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "Vampiro"

HELP_MESSAGE = _("Esto está pendiente.")
GENERIC_REPROMPT = _("¿Con que te puedo ayudar?")

STOP_MESSAGE = _("De acuerdo, ¡bye!")
FALLBACK_MESSAGE = _("Algo ha pasado ¿Que has hecho?")

EXCEPTION_MESSAGE = _("Lo siento. No puedo ayudarte con eso.")

# Initial Request
WELCOME = _("¡Bienvenido al generador de personajes de vampiro!")

# Intent
CREATE_CHARACTER = _("Crear personaje")
CREATE_CHARACTER_ASK_NAME = _("¿Como quieres llamar a tu personaje?")
CREATE_CHARACTER_ASK_CLAN = _("¿A que clan quieres pertenecer?")

CREATE_CHARACTER_CONFIRMATION = _("Creando a {name} de los {clan}.")

REQUIRED_SLOTS = ["nombre", "clan"]

# convertHtmlToPdf(sourceHtml, outputFilename)
# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
             )

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
"""
