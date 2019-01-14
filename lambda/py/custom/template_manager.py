# -*- coding: utf-8 -*-
# Python imports
import logging

# 3rd Party imports
from jinja2 import Environment, PackageLoader, select_autoescape

# App imports
from alexa import data, template_data
from custom.archetype import Archetype

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

env = Environment(
    loader=PackageLoader('alexa', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


class TemplateManager(object):

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan

    def get_subject(self):
        return data.SUBJECT.format(name=self.name, clan=self.clan)

    def get_html(self):
        template = env.get_template('template2.html')

        archetype = Archetype(self.clan)

        return template.render(
            name=self.name,
            clan=self.clan,
            skill_headers=template_data.skill_headers,
            skills=template_data.skills,
            skills_archetype=archetype.get_skills(),
            attributes_headers=template_data.attributes_headers,
            attributes=template_data.attributes,
            attributes_archetype=archetype.get_attributes(),
            advantages_headers=template_data.advantages_headers,
            virtues=template_data.virtues,
            disciplines=archetype.get_disciplines(),
            health=template_data.health
        )

    def get_body_text(self):
        return data.BODY_TEXT.format(name=self.name, clan=self.clan)
