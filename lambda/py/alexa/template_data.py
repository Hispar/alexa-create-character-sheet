attributes_headers = ['Físicos', 'Sociales', 'Mentales']
skill_headers = ['Talentos', 'Técnicas', 'Conocimientos']
advantages_headers = ['Disciplinas', 'Transfondos', 'Virtudes']

attributes_access = {
    'F': 'Fuerza',
    'D': 'Destreza',
    'R': 'Resistencia',
    'C': 'Carisma',
    'M': 'Manipulación',
    'A': 'Apariencia',
    'P': 'Percepción',
    'I': 'Inteligencia',
    'AS': 'Astucia',
}

attributes = {
    'Físicos': [
        'Fuerza',
        'Destreza',
        'Resistencia',
    ],
    'Sociales': [
        'Carisma',
        'Manipulación',
        'Apariencia',
    ],
    'Mentales': [
        'Percepción',
        'Inteligencia',
        'Astucia',
    ]
}

skills = {
    "Talentos": [
        "Alerta",
        "Atletismo",
        "Callejeo",
        "Consciencia",
        "Empatía",
        "Expresión",
        "Intimidación",
        "Liderazgo",
        "Pelea",
        "Subterfugio",
    ],
    "Técnicas": [
        "Armas de Fuego",
        "Artesania",
        "Conducir",
        "Etiqueta",
        "Interpretación",
        "Latrocinio",
        "Pelea con Armas",
        "Sigilo",
        "Supervivencia",
        "Trato con Animales",
    ],
    "Conocimientos": [
        "Academicismo",
        "Ciencias",
        "Finanzas",
        "Informática",
        "Investigación",
        "Leyes",
        "Medicina",
        "Ocultismo",
        "Política",
        "Tecnología",
    ],
}

attributes_archetypes = {
    "brujah": [  # 1 Físico 2 Social 3 Mental
        (
            {'F': 3, 'D': 4, 'R': 3},  # Destreza
            {'F': 4, 'D': 3, 'R': 3},  # Fuerza
            {'F': 3, 'D': 3, 'R': 4},  # Resistencia
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
        ), (
            {'P': 1, 'I': 3, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 2},  # Equilibrado
            {'P': 1, 'I': 1, 'AS': 3},  # Astucia
        ),
    ],
    "ventrue": [  # 1 Social 2 Mental 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 4, 'A': 3},  # Manipulación
            {'C': 4, 'M': 3, 'A': 3},  # Carisma
            {'C': 3, 'M': 3, 'A': 4},  # Apariencia
        ), (
            {'P': 2, 'I': 3, 'AS': 3},  # Equilibrado
            {'P': 2, 'I': 4, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 4},  # Astucia
        ),
    ],
    "assamita": [  # 1 Físico 2 Social 3 Mental
        (
            {'F': 3, 'D': 4, 'R': 3},  # Destreza
            {'F': 4, 'D': 3, 'R': 3},  # Fuerza
            {'F': 3, 'D': 3, 'R': 4},  # Resistencia
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
        ), (
            {'P': 1, 'I': 3, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 2},  # Equilibrado
            {'P': 1, 'I': 1, 'AS': 3},  # Astucia
        ),
    ],
    "gangrel": [  # 1 Físico 2 Mental 3 Social
        (
            {'F': 3, 'D': 4, 'R': 3},  # Destreza
            {'F': 4, 'D': 3, 'R': 3},  # Fuerza
            {'F': 3, 'D': 3, 'R': 4},  # Resistencia
        ), (
            {'C': 2, 'M': 2, 'A': 2},  # Equilibrado
            {'C': 2, 'M': 3, 'A': 1},  # Manipulacion
        ), (
            {'P': 2, 'I': 3, 'AS': 3},  # Equilibrado
            {'P': 2, 'I': 4, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 4},  # Astucia
        ),
    ],
    "seguidores de set": [  # 1 Social 2 Mental 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 4, 'A': 3},  # Manipulación
            {'C': 4, 'M': 3, 'A': 3},  # Carisma
            {'C': 3, 'M': 3, 'A': 4},  # Apariencia
        ), (
            {'P': 2, 'I': 3, 'AS': 3},  # Equilibrado
            {'P': 2, 'I': 4, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 4},  # Astucia
        ),
    ],
    "giovanni": [  # 1 Mental 2 Social 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
            {'C': 2, 'M': 4, 'A': 2},  # Manipulacion
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
    "lasombra": [  # 1 Mental 2 Social 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
            {'C': 2, 'M': 4, 'A': 2},  # Manipulacion
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
    "malkavian": [  # 1 Mental 2 Social 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
    "nosferatu": [  # 1 Mental 2 Fisico 3 Social
        (
            {'F': 3, 'D': 2, 'R': 3},  # Equilibrado
            {'F': 4, 'D': 2, 'R': 2},  # Fuerza
            {'F': 2, 'D': 2, 'R': 4},  # Resistencia
            {'F': 4, 'D': 2, 'R': 2},  # Destreza
        ), (
            {'C': 3, 'M': 2, 'A': 0},  # Carisma
            {'C': 2, 'M': 3, 'A': 0},  # Manipulacion
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
    "ravnos": [  # 1 Social 2 Físico 3 Mental
        (
            {'F': 3, 'D': 2, 'R': 3},  # Equilibrado
            {'F': 4, 'D': 2, 'R': 2},  # Fuerza
            {'F': 2, 'D': 2, 'R': 4},  # Resistencia
            {'F': 4, 'D': 2, 'R': 2},  # Destreza
        ), (
            {'C': 3, 'M': 4, 'A': 3},  # Manipulación
            {'C': 4, 'M': 3, 'A': 3},  # Carisma
            {'C': 3, 'M': 3, 'A': 4},  # Apariencia
        ), (
            {'P': 1, 'I': 3, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 2},  # Equilibrado
            {'P': 1, 'I': 1, 'AS': 3},  # Astucia
        ),
    ],
    "toreador": [  # 1 Social 2 Mental 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 4, 'A': 3},  # Manipulación
            {'C': 4, 'M': 3, 'A': 3},  # Carisma
            {'C': 3, 'M': 3, 'A': 4},  # Apariencia
        ), (
            {'P': 2, 'I': 3, 'AS': 3},  # Equilibrado
            {'P': 2, 'I': 4, 'AS': 2},  # Inteligencia
            {'P': 2, 'I': 2, 'AS': 4},  # Astucia
        ),
    ],
    "tremere": [  # 1 Mental 2 Social 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
            {'C': 2, 'M': 4, 'A': 2},  # Manipulacion
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
    "tzimisce": [  # 1 Mental 2 Social 3 Físico
        (
            {'F': 2, 'D': 2, 'R': 2},  # Equilibrado
        ), (
            {'C': 3, 'M': 2, 'A': 3},  # Equilibrado
            {'C': 4, 'M': 2, 'A': 2},  # Carisma
            {'C': 2, 'M': 2, 'A': 4},  # Apariencia
            {'C': 2, 'M': 4, 'A': 2},  # Manipulacion
        ), (
            {'P': 3, 'I': 4, 'AS': 3},  # Inteligencia
            {'P': 4, 'I': 3, 'AS': 3},  # Perspicacia
            {'P': 3, 'I': 3, 'AS': 4},  # Astucia
        ),
    ],
}

# primary = 13
# secondary = 9
# terciary = 5

skills_counters = {
    "Talentos": 0,
    "Técnicas": 0,
    "Conocimientos": 0
}

skills_sets = [
    ('Ecléctico', 'Actual', 'Social'),
    ('Ecléctico', 'Erudito', 'Social'),
    ('Ecléctico', 'Actual', 'Luchador'),
    ('Ecléctico', 'Erudito', 'Luchador'),
    ('Luchador', 'Erudito', 'Urbanita'),
    ('Luchador', 'Actual', 'Urbanita'),
    ('Luchador', 'Erudito', 'Ecléctico'),
    ('Luchador', 'Actual', 'Ecléctico'),
    ('Erudito', 'Ecléctico', 'Luchador'),
    ('Erudito', 'Urbanita', 'Luchador'),
    ('Erudito', 'Ecléctico', 'Social'),
    ('Erudito', 'Urbanita', 'Social'),
    ('Urbanita', 'Social', 'Actual'),
    ('Urbanita', 'Social', 'Erudito'),
    ('Urbanita', 'Luchador', 'Actual'),
    ('Urbanita', 'Luchador', 'Erudito'),
    ('Social', 'Urbanita', 'Actual'),
    ('Social', 'Ecléctico', 'Actual'),
    ('Social', 'Urbanita', 'Erudito'),
    ('Social', 'Ecléctico', 'Erudito'),
    ('Actual', 'Urbanita', 'Social'),
    ('Actual', 'Ecléctico', 'Social'),
    ('Actual', 'Urbanita', 'Luchador'),
    ('Actual', 'Ecléctico', 'Luchador'),
]

skills_presets = {
    'Ecléctico': 'Técnicas',
    'Luchador': 'Talentos',
    'Erudito': 'Conocimientos',
    'Urbanita': 'Técnicas',
    'Social': 'Talentos',
    'Actual': 'Conocimientos'
}

skills_archetypes = {
    'Ecléctico': {  # 2
        'Consciencia': 0,  # 1
        'Conducir': 0,  # 2
        'Interpretación': 0,  # 2
        'Latrocinio': 0,  # 2
        'Artesania': 0,  # 2
        'Trato con Animales': 0  # 2
    },
    'Luchador': {  # 1
        'Alerta': 0,  # 1
        'Atletismo': 0,  # 1
        'Pelea': 0,  # 1
        'Armas de Fuego': 0,  # 2
        'Pelea con Armas': 0,  # 1
        'Intimidación': 0  # 1
    },
    'Erudito': {  # 3
        'Leyes': 0,
        'Ocultismo': 0,
        'Política': 0,
        'Investigación': 0,
        'Academicismo': 0
    },
    'Urbanita': {  # 2
        'Alerta': 0,  # 1
        'Callejeo': 0,  # 1
        'Sigilo': 0,  # 2
        'Supervivencia': 0,  # 2
        'Trato con Animales': 0,  # 2
        'Armas de Fuego': 0,  # 2
        'Etiqueta': 0,  # 2
    },
    'Social': {  # 1
        'Empatía': 0,  # 1
        'Subterfugio': 0,  # 1
        'Liderazgo': 0,  # 1
        'Etiqueta': 0,  # 2
        'Expresión': 0,  # 1
        'Consciencia': 0,  # 1
    },
    'Actual': {  # 3
        'Tecnología': 0,  # 3
        'Ciencias': 0,  # 3
        'Finanzas': 0,  # 3
        'Informática': 0,  # 3
        'Medicina': 0,  # 3
    }
}

disciplines = {
    "assamita": ['Celeridad', 'Ofuscación', 'Extinción'],
    "brujah": ['Celeridad', 'Potencia', 'Presencia'],
    "gangrel": ['Animalismo', 'Fortaleza', 'Protean'],
    "seguidores de set": ['Ofuscación', 'Presencia', 'Serpentis'],
    "giovanni": ['Dominación', 'Nigromancia', 'Potencia'],
    "lasombra": ['Dominación', 'Obtenebración', 'Potencia'],
    "malkavian": ['Auspex', 'Dementación', 'Ofuscación'],
    "nosferatu": ['Animalismo', 'Ofuscación', 'Potencia'],
    "ravnos": ['Animalismo', 'Quimerismo', 'Fortaleza'],
    "toreador": ['Auspex', 'Celeridad', 'Presencia'],
    "tremere": ['Auspex', 'Dominación', 'Taumaturgia'],
    "tzimisce": ['Animalismo', 'Auspex', 'Vicisitud'],
    "ventrue": ['Dominación', 'Fortaleza', 'Presencia'],
}

virtues = {
    0: 'Conciencia/Convicción',
    2: 'Autocontrol/Instinto',
    4: 'Coraje'
}

health = [
    'Magullado',
    'Lastimado -1',
    'Lesionado -1',
    'Herido -2',
    'Malherido -3',
    'Tullido -5',
    'Incapacitado',
]
