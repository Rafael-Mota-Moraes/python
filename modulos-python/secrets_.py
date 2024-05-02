# numeros aleatórios seguros

import secrets
import string as s
from secrets import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=6)))

random = secrets.SystemRandom()
print(secrets.randbelow(10))
print(secrets.choice(['a', 'b', 'c']))
print(random.randint(0, 10))
