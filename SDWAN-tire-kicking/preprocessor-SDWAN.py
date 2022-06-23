# Just the functions we need to set up the preprocessy bit
# this is the pre-processor for SD-WAN, specifically

from dataclasses import dataclass
from unipath import Path
import json
import jinja2
import re 


file_directory = Path(r"C:\Users\estahl\CodingProjects\lubensDEMONSTRATION\Sample-unzipped")

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

returned = load_data(file_directory)
 
print(type(returned))

'''
API_VALUES_RECEIVED = {
    'raw_data': 'The File/Folder with all the data',
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
