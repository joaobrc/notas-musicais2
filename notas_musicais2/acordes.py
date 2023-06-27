from notas_musicais2.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')
    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas_acordes = [tonica, terca, semitom(quinta, intervalo=1)]
        graus_acordes = ['I', 'III-', 'V+']

    else:

        notas_acordes = triade(nota, 'menor')
        graus_acordes = ['I', 'III-', 'V']

    return notas_acordes, graus_acordes


def semitom(nota, intervalo):
    pos = NOTAS.index(nota) + intervalo
    return NOTAS[pos % 12]


def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas, _ = escala(nota, tonalidade).values()
    return [notas[grau] for grau in graus]


def acorde(cifra: str):
    """
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

    """
    if 'm' in cifra:
        notas_acordes, graus_acordes = _menor(cifra)
    elif '-' in cifra:
        nota, _ = cifra.split('-')
        tonica, terca, quinta = triade(nota, 'menor')
        notas_acordes = [tonica, terca, semitom(quinta, -1)]
        graus_acordes = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, _ = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas_acordes = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus_acordes = ['I', 'III', 'V+']
    else:
        notas_acordes = triade(cifra, 'maior')
        graus_acordes = ['I', 'III', 'V']

    return {'notas': notas_acordes, 'graus': graus_acordes}
