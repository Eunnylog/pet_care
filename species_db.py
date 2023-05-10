import csv
import os
import django
import sys
from os.path import abspath, dirname

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

# BASE_DIR = dir(dirname(dirname(dirname(abspath(__file__)))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_care.settings')
django.setup()

from owners.models import Species

CSV_PATH = './species_breeds.csv'

with open(CSV_PATH, newline='', encoding='UTF8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        Species.objects.create(
            species=row['species'],
            breeds=row['breeds']
        )
        