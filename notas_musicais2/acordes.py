from notas_musicais2.escalas import escala


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
        nota, _ = cifra.split('m')
        notas_acordes = triade(nota, 'menor')
        graus_acordes = ['I', 'III-', 'V']
    else:
        notas_acordes = triade(cifra, 'maior')
        graus_acordes = ['I', 'III', 'V']

    return {'notas': notas_acordes, 'graus': graus_acordes}
