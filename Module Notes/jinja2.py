"""
This script renders packer files using jinja2

This allows different flavours of packer builds without code duplication
"""

import os
import jinja2
import subprocess
import json

#Define some variables
this_folder = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(this_folder, 'templates')

env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	#Becuase we are templating json we need to pick different variable start/end strings
	variable_start_string = '{{{',
	variable_end_string = '}}}'
)

files_to_render = [
	'template1.j2',
  'template2.j2',
  'template3.j2'
]

for r in files_to_render:
	template_file = os.path.join(template_dir, r)
	template = env.get_template(r)
	template_content = template.render()
	template_content = json.loads(template_content)

	base, ext = os.path.splitext(template_file)
	rendered_file = base + ".rendered.json"
	f = open(os.path.join(this_folder, rendered_file), 'w')
	f.write(json.dumps(template_content, indent=4))
	f.close()
