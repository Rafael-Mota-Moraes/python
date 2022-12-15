# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar!')
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer!')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa...')
        return
    
    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue        
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue        
    else:
        adicionar(tarefa, tarefas)
        continue        
