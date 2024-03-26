# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não conheçe pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import sys

import modularizacao_module

print('Este módulo se chama:', __name__)
print(modularizacao_module.soma(1, 2))
print("O módulo se chama:", modularizacao_module.__name__)
print(*sys.path, sep='\n')
