NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]: 
    """
    Gera uma escala apartir de uma tonica  e uma tonalidade

    Parameters:
        tonica: Nota que sera a tonica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionario com as informações da nota e seus graus, retonados de cada nota informado na escala
        
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}


        >>> escala('B', 'maior')
        {'notas': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)
    temp = []
    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
