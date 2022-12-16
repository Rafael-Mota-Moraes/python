import json

CAMINHO_ARQUIVO = 'classe_para_json.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)    
p3 = Pessoa('Joana', 19)    

bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

print(__name__)
