from pytest import mark
from typer.testing import CliRunner

from notas_musicais2.cli import app

runner = CliRunner()


def test_cli_comando_esta_funcionando():
    # monta ou arruma
    comando = runner.invoke(app)

    # execucao
    result = comando.exit_code

    # RESULTADO
    assert result == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_ao_excultar_o_comando_todas_as_notas_estao_presentes_na_nota_default(
    nota,
):
    # arruma ou montar
    comando = runner.invoke(app)

    # execulçao
    result = comando.stdout

    # resultado
    assert nota in result


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_verifica_se_os_grau_estao_no_cli(grau):
    comando = runner.invoke(app)

    result = comando.stdout

    assert grau in result


@mark.parametrize(
    'nota, esperado',
    [
        ('D', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('E', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_ao_excultar_o_comando_todas_as_notas_estao_presentes_na_nota_passando_uma_nota(
    nota, esperado
):
    # arrumar
    comando = runner.invoke(app, nota)
    # execulcao
    result = comando.stdout

    for tonica in esperado:
        assert tonica in result
