# This will hold code that only goes with the template engine, 
# aka the create_doc_outline() function.
from dataclasses import dataclass
from unipath import Path
import json
import jinja2
import re 


def create_doc_outline(data):
    template_path = Path('doc.jinja2')
    template = jinja2.Template(template_path.read_file(), trim_blocks=True)
    # all these args are so the function knows to use those other functions/objs
    # they're mostly to make sure the jinja is handled correctly
    # Ruben goes into detail around ~12-16
    # WHAT IS HAPPENING HERE IN THIS LINE.
    doc_outline = template.render(data=data, j_dumps=j_dumps, j_loads=json.loads, TableCount=TableCount, re=re)
    return doc_outline

# oh ho!! in the new version this function will take the result of the api call as input.  
results_dict = load_data(r"C:\Users\estahl\projects\SDWAN-tire-kicking")

create_doc_outline(results_dict)
