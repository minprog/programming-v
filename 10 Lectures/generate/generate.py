import os

from jinja2 import Template

import template_values

def generate():
    for lecture_number in range(1, 10):
        directory = '{0} Lecture {1}'.format(str(lecture_number).rjust(3, '0'), lecture_number)
        directory = os.path.join('..', directory)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        md_file = os.path.join(directory, '10 Lecture {0}.md'.format(lecture_number))
        apply_template(md_file, template_values.lectures[lecture_number - 1])
    print "done"

def apply_template(path, values):
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'w') as f:
        f.write(template.render(**values))
        print "written", path


with open('template.md', 'r') as f:
    template = Template(f.read())

yes_no = raw_input("WARNING: this overrides all lecture files. Continue? [Y/n] ")
while True:
    if yes_no.upper() in ('Y', 'YES', ''):
        generate()
        break
    elif yes_no.upper() in ('N', 'NO'):
        break
    else:
        yes_no = raw_input("Please enter 'y' or 'n'. ")
