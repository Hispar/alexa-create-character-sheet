# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _


# Permissions
PERMISSIONS = ["alexa::profile:email:read"]

SKILL_NAME = "Vampiro"

HELP_MESSAGE = _("Esto está pendiente.")
GENERIC_REPROMPT = _("¿Con que te puedo ayudar?")

STOP_MESSAGE = _("De acuerdo, ¡bye!")
FALLBACK_MESSAGE = _("Algo raro ha pasado ¿Puedes volver a intentarlo?")

EXCEPTION_MESSAGE = _("Lo siento. No puedo ayudarte con eso.")

NOTIFY_MISSING_PERMISSIONS = ("Es necesario que habilites el acceso a tu dirección de email "
                              "en la aplicación de Amazon Alexa.")

# Initial Request
WELCOME = _("¡Bienvenido al generador de personajes de vampiro!")

# Intent
CREATE_CHARACTER = _("Crear personaje")
CREATE_CHARACTER_ASK_NAME = _("¿Como quieres llamar a tu personaje?")
CREATE_CHARACTER_ASK_CLAN = _("¿A que clan quieres pertenecer?")

CREATE_CHARACTER_CONFIRMATION = _("Se ha creado a {name} de los {clan}. Revisa tu correo.")

# convertHtmlToPdf(sourceHtml, outputFilename)
# The subject line for the email.
SUBJECT = "Tu ficha de personaje - {name} {clan}"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = _("Aqui tienes tu personaje de vampiro\r\n"
             "{name} del clan {clan} ha sido creado."
             )

PROGRESSIVE_PDF_CREATION = _("Creando el la ficha de {name}, espera un momento.")

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Aqui tienes tu personaje de vampiro</h1>
  <p>{name} del clan {clan} ha sido creado.</p>
</body>
</html>
"""
