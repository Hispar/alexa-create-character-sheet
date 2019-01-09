# -*- coding: utf-8 -*-
"""Simple fact sample app."""
import io
import logging

from ask_sdk_core.api_client import DefaultApiClient
from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.dialog import ElicitSlotDirective, DelegateDirective
from ask_sdk_model import (Intent, IntentConfirmationStatus, Slot, SlotConfirmationStatus, DialogState)
from ask_sdk_model.services import ServiceException

from ask_sdk_model.ui import SimpleCard, AskForPermissionsConsentCard
from ask_sdk_model import Response

from alexa import data
from alexa import constants
from custom.mailer import Mailer
from custom.template_manager import TemplateManager

# =========================================================================================================================================
# Editing anything below this line might break your skill.
# =========================================================================================================================================

sb = CustomSkillBuilder(api_client=DefaultApiClient())
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
class RequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RequestHandler")
        handler_input.response_builder.speak(data.WELCOME).set_should_end_session(
            False)
        return handler_input.response_builder.response


class CreateCharacterIntent(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CreateCharacterIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CreateCharacterIntent")

        req_envelope = handler_input.request_envelope
        response_builder = handler_input.response_builder
        service_client_fact = handler_input.service_client_factory

        if not (req_envelope.context.system.user.permissions and
                req_envelope.context.system.user.permissions.consent_token):
            response_builder.speak(data.NOTIFY_MISSING_PERMISSIONS)
            response_builder.set_card(
                AskForPermissionsConsentCard(permissions=data.PERMISSIONS))
            return response_builder.response

        try:
            user_service = service_client_fact.get_ups_service()
            recipient = user_service.get_profile_email()
        except ServiceException:
            response_builder.speak(data.FALLBACK_MESSAGE)
            return response_builder.response
        except Exception as e:
            raise e

        dialog_state = req_envelope.request.dialog_state
        if dialog_state != DialogState.COMPLETED:
            directive = DelegateDirective()
            response_builder.add_directive(directive)
        else:
            slots = req_envelope.request.intent.slots
            name = slots['nombre'].value
            clan = slots['clan'].value
            speech = data.CREATE_CHARACTER_CONFIRMATION.format(name=name, clan=clan)
            response_builder.speak(speech)
            # Replace sender@example.com with your "From" address.
            # This address must be verified with Amazon SES.
            sender = constants.sender

            # Replace recipient@example.com with a "To" address. If your account
            # is still in the sandbox, this address must be verified.
            template = TemplateManager(name=name, clan=clan)
            subject = template.get_subject()

            document = io.BytesIO()
            template.get_document(document)

            bytesObj = io.BytesIO()
            bytesObj.write(str(document).encode('utf-8'))

            mail = Mailer()
            mail.create_mail(subject=subject, sender=sender, recipient=recipient, body=template.get_html())
            mail.create_attachment(bytesObj, 'personaje.html')
            mail.send()

        return response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(data.HELP_MESSAGE).ask(
            data.GENERIC_REPROMPT).set_card(SimpleCard(data.SKILL_NAME, data.HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(data.STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(data.FALLBACK_MESSAGE).ask(
            data.GENERIC_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(data.EXCEPTION_MESSAGE).ask(
            data.GENERIC_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""

    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""

    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(RequestHandler())
sb.add_request_handler(CreateCharacterIntent())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
