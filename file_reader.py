import json
import sys
import random
import psycopg2
from db_commands import address_insert, address_selection
host = user = password = db_name = port = ''
region = ['Київська', 'Житомирська', 'Херсонська', 'Львівська', 'Запорізька']
settlement = []
settlement_file = []
street = []
street_file = []
house = []
postal_code = ''
with open('.env') as dotenv:
    dotenv = json.load(dotenv)
    for k,v in dotenv.items():
        globals()[k] = v

if len(sys.argv) > 1:
    with open(f'./filesToRead/{sys.argv[1]}.txt', encoding="UTF-8") as processing_file:
        for line in processing_file:
            one_address = line.strip()
            one_address = one_address.split('\t')
            one_address = one_address[1]
            one_address = one_address.replace(', ', ',').split(',')
            one_address = one_address[1:3]
            settlement.append(one_address[0])
            if ' ' in one_address[1]:
                one_address = one_address[1].split(' ')[1]
            else:
                one_address = one_address[1]
            street.append(one_address)
settlement = list(set(settlement))
settlement.sort()
for item in settlement:
  if len(item) > 5:
      settlement_file.append(item)


settlement_file = settlement_file[:20]
street = list(set(street))
street.sort()

for item in street:
    if len(item) > 5:
        street_file.append(item)

street_file = street_file[:20]

street_prefix = ['вулиця', 'вул.', 'провулок', 'пров.', 'проспект', 'пр.']

def randomizer(street_prefix, street_file, settlement_file, region):
    return f'\
{random.choice(region)} область, \
{random.choice(settlement_file)}, \
{random.choice(street_prefix)} \
{random.choice(street_file)}, \
{random.randint(1,150)}, \
{str(random.randint(0,99999)).zfill(5)}\
'

connection = psycopg2.connect(host=host, user=user, password=password, dbname=db_name, port=port)
connection.autocommit = True

for i in range(20):
    address_to_db = randomizer(street_prefix, street_file, settlement_file, region)
    print(address_to_db)
    address_to_db = address_to_db.split(', ')
    address_insert(connection, *address_to_db)

    #print(address_select)

if connection:
    connection.close()

