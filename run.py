import json
import subprocess
import sys
from os import remove
import shutil
from datetime import datetime

args = [*sys.argv][1:]
if args:
    kwargs = '+'.join(args)
else:
    kwargs = None
    print('Not enough params.')
    exit()

print('Spider is running (check all items, create temp file: attrs.json)...')
# subprocess.call('scrapy crawl main -a params={kw} -o attrs.json'.format(kw=kwargs), shell=True)
print('Spider closed.')

try:
    with open('attrs.json') as f:
        data = json.load(f)
        try:
            fail = list(map(lambda f: f['fail'], data))[0]
        except (KeyError, IndexError):
            fail = False
        try:
            cat = list(map(lambda c: c['category'].replace('/', ' '), data))[0]
        except IndexError:
            cat = ''
        except KeyError:
            cat = ''
            remove('attrs.json')
            print('Finished. Incorrect catalog.')
            exit()
except (FileNotFoundError, ValueError):
    cat = ''
    fail = False

date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
no_name = 'no_name_%s' % date
if cat:
    cat = cat.replace(' ', '_').replace('.', '').replace(',', '').lower()
else:
    cat = no_name


print('Spider is running (start scraped info about items, create temp file info.csv)...')
# subprocess.call('scrapy crawl info', shell=True)

print('Rename temp csv file...')
try:
    shutil.move('info.csv', 'scraped_info/{filename}.csv'.format(filename='_'.join([cat, date])))
except FileNotFoundError:
    print('Error! Nothing to rename!')

print('Move temp json file...')
try:
    shutil.move('attrs.json', 'attrs/{filename}.json'.format(filename='_'.join([cat, date])))
except FileNotFoundError:
    print('Error! Nothing to move!')

print('Complete.')
