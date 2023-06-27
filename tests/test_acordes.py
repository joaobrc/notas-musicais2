from pytest import mark

from notas_musicais2.acordes import acorde


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('D', ['D', 'F#', 'A']),
        ('F#', ['F#', 'A#', 'C#']),
        ('Cm', ['C', 'D#', 'G']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('C-', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
    ],
)
def test_deve_retunr_notas_presente_no_acorede(cifra, esperado):

    notas, _ = acorde(cifra).values()

    assert notas == esperado


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C-', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_deve_retorna_os_graus_presente_no_acorede(cifra, esperado):

    _, graus = acorde(cifra).values()

    assert graus == esperado
