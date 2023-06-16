![Nota de Musica](assets/note.png){.center}
# Notas Musicais 

## Como execultando linha de comando

A aplicação funciona por linha de comando execultando o comando abaixo
```bash
poetry run escalas
```
Retonado a tabela abaixa
```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alterando a linha de comando com a tonica

A possibilidade de informa a tonica e ele ira retonar o sua escala consequentemente, como no exemplo abaixo:

```bash
poetry run escalas D

```
Trazendo o resultado abaixo:
```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D │ E  │ F#  │ G  │ A │ B  │ C#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alterando a linha de comando com a tonica e tonalidade
Pode tambem ser informado a tonica e a tonaidade, como no exemplo abaixo
```bash
poetry run escalas D maior

```
tendo o resultado abaixo:
```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D │ E  │ F#  │ G  │ A │ B  │ C#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Comandos de ajuda 

A infomações de ajuda poderam ser passasda do paramento --help, como no exemplo abaixo:
```bash
poetry run escalas --help
```


