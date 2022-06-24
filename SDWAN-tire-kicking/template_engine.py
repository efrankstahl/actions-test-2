# This will hold code that only goes with the template engine, 
# aka the create_doc_outline() function.
from dataclasses import dataclass
from unipath import Path
import json
import jinja2
from jinja2 import Template
import requests
import re 

# 6/23 API: This has to receive the API data 
# 6/23 API: AND IT WILL SEND THE DOCUMENT OUTLINE AS A LIST (like JSON, but a python object)


class TableCount(object):
    def __init__(self, start_value=1):
        self.value = start_value

    def current(self):
        return self.value

    def next(self):
        v = self.value
        self.value += 1
        return v
# currently have this in both the preprocessor and the templating engine ..prolly just need it here. 
def j_dumps(raw_text):
    if isinstance(raw_text, (int, type(None))):
        raw_text = str(raw_text)
    json_txt = json.dumps(raw_text)
    return json_txt

# 6/23: Code to, hopefully, receive api info

url = 'http://127.0.0.1:5000/to-template'

response = requests.get(url)
print(response.text)

# 6/24 : THIS CODE STILL NOT WORKING. Sometimes it's a path issue. 
# but when I fix that, I get: jinja2.exceptions.UndefinedError: "stack_info" is undefined 
'''
def create_doc_outline(data):
    template_path = Path('doc.jinja2')
    template = jinja2.Template(template_path.read_file(), trim_blocks=True)
    doc_outline = template.render(data=data, j_dumps=j_dumps, j_loads=json.loads, TableCount=TableCount, re=re)
    return doc_outline
'''
# oh ho!! in the new version this function will take the result of the api call as input.  
# results_dict = load_data(r"C:\Users\estahl\projects\SDWAN-tire-kicking")

#create_doc_outline(results_dict)
