import requests
import random
from random import randint
import time
print('Inserindo registros de temperatura e umidade/API')
for medida in range(1, 16):

    temperatura= randint(1, 25)
    field1='https://api.thingspeak.com/update?api_key=XL597MTQW9CFROGG&field1='
    field1= field1 + str(temperatura)
    print(field1)
    time.sleep(15)

    umidade=randint(25, 87)
    field2='https://api.thingspeak.com/update?api_key=XL597MTQW9CFROGG&field2='
    field2= field2 + str(umidade)
    print(field2)
    time.sleep(15)

    r=requests.get(field2, field1)