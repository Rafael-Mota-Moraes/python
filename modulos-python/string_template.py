import json
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'string_template.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)

dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%y'),
    empresa='R. M.',
    telefone='+55 (99) 9 9999-9999'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

# texto = """
# Olá, $nome,

# $valor
# no dia $data

# Atenciosamente,
# ${empresa}
# """

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
