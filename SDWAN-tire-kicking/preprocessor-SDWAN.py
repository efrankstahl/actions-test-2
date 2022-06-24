# Just the functions we need to set up the preprocessy bit
# this is the pre-processor for SD-WAN, specifically

from dataclasses import dataclass
from unipath import Path
from jinja2 import Template
import json
import jinja2
import re 
import requests


# TEMPORARY 
# from template_engine import create_doc_outline

# eventually this will have to receive an API 
# 6/24 for now we gotta make it take a single yaml file instead of going thru a directory.
file_directory = Path(r"C:\Users\estahl\projects\SDWAN-tire-kicking\Sample-unzipped")

# probably don't need this
class TableCount(object):
    def __init__(self, start_value=1):
        self.value = start_value

    def current(self):
        return self.value

    def next(self):
        v = self.value
        self.value += 1
        return v

# very possibly don't need this until the templating engine 
def j_dumps(raw_text):
    if isinstance(raw_text, (int, type(None))):
        raw_text = str(raw_text)
    json_txt = json.dumps(raw_text)
    return json_txt

# R: WE ARE NO LONGER GETTING A ZIP FILE, IT'S GONNA BE ONE BIG YAML FILE.
def load_data(files_path):
    loaded_data = {}
    for file_item in file_directory.listdir():
        # turning the json into a python dict
        # we'll also have to do a check for json vs yaml and handle it appropriately
        loaded_data[file_item.stem] = json.loads(file_item.read_file())
    return loaded_data

#  maybe after i load data, have it go thru this parse data thing 
#  just purely return the loaded data, in case people have to add methods later
def parse_data(loaded_data):
    return loaded_data

# this is a python dictionary 
full_data = load_data(file_directory)

# print(full_data)
print(type(full_data))  
# templated = create_doc_outline(full_data)

# Sends processed data to the API 
url = 'http://127.0.0.1:5000/to-template'

payload = {
    'raw_data': full_data,
    'product': 'SD-WAN',
    'replacement_values': '[ PLACEHOLDER FOR THE DOC ENGINE ]',
    'gdoc_type': True
}

response = requests.post(url, data=payload)

#print(response.text)



'''
API_VALUES_RECEIVED = {
    'raw_data': 'the yaml file with all the data',
    'product': 'SD-WAN', 
    'replacement_values':  <for the doc engine; we don't really have to care>
    'gdoc_type':  true
}
API_VALUES_PUSHED = {
    # aka the ones we send
    'parsed_data': 'this will be the document outline as a list',
    'product': 'SD-WAN',
    'replacement_values': '<who cares>',
    'gdoc_type': True
}
'''
