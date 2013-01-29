import code
import os

from jinja2 import Template

import template_values

LECTURES_TEMPLATE = 'lectures.md'
RECITATIONS_TEMPLATE = 'recitations.md'


def generate(template, values, parent_directory, label):
    """Generates a page from template for each set of values in values.
    All new pages are stored in parent_directory with label as their
    title.

    """
    videos = [(index + 1, video['id']) for index, video in enumerate(values)]
    for video_index, video_id in videos:
        directory = '{0} {1} {2}'.format(str(video_index).rjust(3, '0'), label, video_id)
        directory = os.path.join(parent_directory, directory)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        output_path = os.path.join(directory, '10 {0} {1}.md'.format(label, video_id))
        apply_template(output_path, template, values[video_index - 1])
    print

def apply_template(path, template, values):
    """Renders template with values and stores the result in path."""
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'w') as f:
        f.write(template.render(**values))
        print "written", path

def user_confirmation(about):
    prompt = "Generate {0} files? WARNING: this overrides all existing {0} files. [Y/n] ";
    yes_no = str.upper(raw_input(prompt.format(about)))
    while True:
        if yes_no in ('Y', 'YES', ''):
            return True
        elif yes_no in ('N', 'NO'):
            return False
        else:
            yes_no = str.upper(raw_input("Please enter 'y' or 'n'. "))


if __name__ == '__main__':
    if user_confirmation('lecture'):
        with open(LECTURES_TEMPLATE, 'r') as f:
            template = Template(f.read())
            generate(template, template_values.lectures,
                     os.path.join('..', '10 Lectures'), 'Lecture')
    
    if user_confirmation('recitation'):
        with open(RECITATIONS_TEMPLATE, 'r') as f:
            template = Template(f.read())
            generate(template, template_values.recitations,
                     os.path.join('..', '20 Recitations'), 'Recitation')

    print "done."
