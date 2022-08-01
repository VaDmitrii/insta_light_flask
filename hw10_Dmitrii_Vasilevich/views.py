import json


def load_candidates():
    """ Загружает данные из файла 'candidates.json' """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


CANDIDATES = load_candidates()


def get_all():
    """Показывает всех кандидатов"""
    return CANDIDATES


def get_by_pk(pk):
    """Возвращает кандидата по pk"""
    for candidate in CANDIDATES:
        if pk == candidate['pk']:
            return candidate


def get_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates = []
    for candidate in CANDIDATES:
        if skill_name.lower() in candidate['skills'].lower():
            candidates.append(candidate)
    return candidates
