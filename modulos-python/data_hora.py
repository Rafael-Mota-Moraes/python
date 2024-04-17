# Criando datas com módulo datetime

from datetime import datetime

data_str = '2024-04-17 07:49:24'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime(2024, 4, 17, 10, 40, 00)
print(data)
data = datetime.now()
print(data)
data = datetime.strptime(data_str, data_str_fmt)
print(data)
