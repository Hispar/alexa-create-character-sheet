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
    "brujah": [
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
    "ventrue": [
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
        "Consciencia": 1,  # 1
        "Conducir": 1,  # 2
        "Interpretación": 1,  # 2
        "Latrocinio": 1,  # 2
        "Medicina": 1,  # 3
    },
    'Luchador': {  # 1
        'Atletismo': 1,  # 1
        'Pelea': 1,  # 1
        'Armas de Fuego': 1,  # 2
        'Pelea con Armas': 1,  # 1
        'Intimidación': 1  # 1
    },
    'Erudito': {  # 3
        'Leyes': 1,
        'Ocultismo': 1,
        'Política': 1,
        'Investigación': 1,
        'Academicismo': 1
    },
    'Urbanita': {  # 2
        'Alerta': 1,  # 1
        'Callejeo': 1,  # 1
        'Sigilo': 1,  # 2
        'Supervivencia': 1,  # 2
        'Trato con Animales': 1  # 2
    },
    'Social': {  # 1
        'Empatía': 1,  # 1
        'Subterfugio': 1,  # 1
        'Liderazgo': 1,  # 1
        'Etiqueta': 1,  # 2
        'Expresión': 1  # 1
    },
    'Actual': {  # 3
        'Tecnología': 1,  # 3
        'Ciencias': 1,  # 3
        'Finanzas': 1,  # 3
        'Informática': 1,  # 3
        'Artesania': 1,  # 2
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