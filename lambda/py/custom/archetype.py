# -*- coding: utf-8 -*-
# Python imports
import random

# 3rd Party imports

# App imports
from alexa import template_data


class Archetype(object):

    def __init__(self, clan):
        self.clan = clan

    def get_attributes(self):
        attributes = template_data.attributes_archetypes[self.clan]
        archetype = dict()
        for subset in attributes:
            archetype.update(random.choice(subset))

        alias = template_data.attributes_access
        archetype = {value: archetype[key] for (key, value) in alias.items()}
        return archetype

    def get_skills(self):
        archetypes = template_data.skills_archetypes
        counters = template_data.skills_counters
        skills_set = random.choice(template_data.skills_sets)

        final_skills = {}
        for skill in skills_set:
            final_skills = dict(final_skills, **archetypes[skill])

        counters[template_data.skills_presets[skills_set[0]]] = 13
        counters[template_data.skills_presets[skills_set[1]]] = 9
        counters[template_data.skills_presets[skills_set[2]]] = 5

        for skill_type, value in counters.items():
            while value > 0:
                skill = self.get_random_skill(skill_type, final_skills)
                if final_skills[skill] < 3:
                    final_skills[skill] += 1
                    value -= 1

        print(final_skills)

        return final_skills

    def get_random_skill(self, skill_type, selected_skills):
        skills = template_data.skills
        skill = random.choice(skills[skill_type])
        if skill in selected_skills.keys():
            return skill
        return self.get_random_skill(skill_type, selected_skills)

    def get_disciplines(self):
        disciplines = template_data.disciplines
        return disciplines[self.clan]
