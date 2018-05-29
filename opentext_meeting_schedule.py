# -*- coding: utf-8 -*-


import os
import sys
import json
from bs4 import BeautifulSoup


def contents(element):
    return list(map(lambda x: x.next, element))


filepath = sys.argv[1]

soup = BeautifulSoup(open(filepath, encoding='utf-8'), 'lxml')

store = []

sections =  soup.find_all('div', {'class': 'team_name'})
store.append({'result': contents(sections)})    

out_filepath = os.path.splitext(filepath)[0] + '.json'
with open(out_filepath, 'w', encoding='utf-8') as out_file:
    json.dump(store, out_file, ensure_ascii=False)