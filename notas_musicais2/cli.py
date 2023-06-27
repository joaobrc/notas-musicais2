from rich.console import Console
from rich.table import Table
from typer import Argument, Typer
from typing_extensions import Annotated

from notas_musicais2.acordes import acorde as _acorde
from notas_musicais2.escalas import escala as _escala

console = Console()

app = Typer()


@app.command()
def escala(
    tonica: Annotated[str, Argument(help='Tonica da escala')] = 'C',
    tonalidade: Annotated[
        str, Argument(help='Tonalidade da escala')
    ] = 'maior',
):

    tabela = Table()
    notas, graus = _escala(tonica, tonalidade).values()
    for grau in graus:
        tabela.add_column(grau)
    tabela.add_row(*notas)
    console.print(tabela)


@app.command()
def acorde(
    cifra: Annotated[str, Argument(help='Tonica da escala')] = 'C+',
):

    tabela = Table()
    notas, graus = _acorde(cifra).values()
    for grau in graus:
        tabela.add_column(grau)
    tabela.add_row(*notas)
    console.print(tabela)
