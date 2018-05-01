import yaml
from jinja2 import Template


def main():
    with open('resume.yml', 'r') as f:
        context = yaml.load(f)
    with open('resume.tex.j2', 'r') as f:
        template = Template(f.read())
    rendered = template.render(**context)
    print(rendered)


if __name__ == '__main__':
    main()
