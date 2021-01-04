from pathlib import Path

import jinja2


def snake_to_camel(text: str) -> str:
    """ Convert snake_case to CamelCase """

    data = [
        i.capitalize()
        for i in text.split("_")
    ]
    return "".join(data)

def to_upper_snakecase(text: str) -> str:
    """ Convert text to UPPER_SNAKE_CASE """

    data = text.replace(" ", "_").upper()
    if data[0].isdigit():
        data = "_" + data
    return data


def form_render(path: str, **kwargs) -> str:
    """ Just jinja2 """

    file_text = Path(f"codegen\\templates\\{path}").read_text()
    template = jinja2.Template(file_text)
    return template.render(**kwargs)
