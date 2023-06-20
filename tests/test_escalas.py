from pytest import mark, raises

from notas_musicais2.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # montar ou arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # execulção
    results = escala(tonica, tonalidade)

    # resultado
    assert results


def test_deve_retorna_erro_ao_inserir_valor_nao_presente_nas_notas():
    # montar ou arruma
    tonica = 'q'
    tonalidade = 'maior'
    menssagem = 'Nota invalida, tente uma destas {}'.format(NOTAS)

    # execulção
    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    # resultado
    assert menssagem == error.value.args[0]


def test_deve_retorna_KeyErro_ao_inserir_uma_tonica_inexistente_e_apresenta_as_tonalidades_certas():
    # monta ou arruma
    tonica = 'C'
    tonalidade = 'i'
    menssagem = (
        'escala inexistente ou indisponivel, '
        'tente uma destas {}'.format(list(ESCALAS.keys()))
    )

    # execulção
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert menssagem == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('B', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),
        ('A', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
    ],
)
def test_deve_retornar_as_notas_esperados(tonica, esperado):

    escalas = escala(tonica, 'maior')
    assert esperado == escalas['notas']


def test_deve_retorna_erro_AttributeError_ao_informar_um_valor_invalido_e_informar_e_correto():
    # montar ou arruma
    tonica = 3
    tonalidade = 'maior'
    menssagem = 'Atributo invalido, só permitido texto'

    # execulção
    with raises(AttributeError) as error:
        escala(tonica, tonalidade)
    assert error.value.args[0] == menssagem
