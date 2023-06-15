from pytest import raises

from notas_musicais2.escalas import NOTAS, escala


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
