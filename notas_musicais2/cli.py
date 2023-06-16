from rich.console import Console
from rich.table import Table
from typer import Argument, Typer
from typing_extensions import Annotated

from notas_musicais2.escalas import escala

console = Console()

app = Typer()


@app.command()
def escalas(
    tonica: Annotated[str, Argument(help='Tonica da escala')] = 'C',
    tonalidade: Annotated[
        str, Argument(help='Tonalidade da escala')
    ] = 'maior',
):

    tabela = Table()
    notas, graus = escala(tonica, tonalidade).values()
    for grau in graus:
        tabela.add_column(grau)
    tabela.add_row(*notas)
    console.print(tabela)
