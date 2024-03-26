import importlib
import recarregando_modulos_module
print(recarregando_modulos_module.variavel)

for i in range(5):
    importlib.reload(recarregando_modulos_module)

print('FIM')
