# Criando datas com módulo datetime

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone

data = datetime.now()

data_str = '2024-04-17 07:49:24'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime(2024, 4, 17, 10, 40, 00)
print(data)
data = datetime.now(timezone('America/Sao_Paulo'))
print(data.timestamp())
data = datetime.strptime(data_str, data_str_fmt)
print(data)

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
print(data_inicio)
print(data_fim)
print(data_fim > data_inicio)
print(data_fim < data_inicio)
delta = data_fim - data_inicio
print(delta.days)
print(delta.total_seconds())
delta = timedelta(days=10)
print(delta)
print(data_fim + relativedelta(seconds=60))
delta = relativedelta(data_fim, data_inicio)
print(delta)

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'), data.hour)
