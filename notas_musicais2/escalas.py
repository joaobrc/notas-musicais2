NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma tonica  e uma tonalidade

    Parameters:
        tonica: Nota que sera a tonica da escala
        tonalidade: Tonalidade da escala

    Raises:
        ValuError: Nota ou tonica inexistente
        KeyError: Escala indisponivel ou inexistente
        AttributeError: Atributo Invalido

    Return:
        Retorna um dicionario com as notas e seu repectivos graus

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('B', 'maior')
        {'notas': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    try:
        tonica = tonica.upper()
        tonica_pos = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]
    except ValueError:
        raise ValueError('Nota invalida, tente uma destas {}'.format(NOTAS))
    except KeyError:
        raise KeyError(
            'escala inexistente ou indisponivel, '
            'tente uma destas {}'.format(list(ESCALAS.keys())),
        )
    except AttributeError:
        raise AttributeError('Atributo invalido, só permitido texto')
    temp = []
    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
