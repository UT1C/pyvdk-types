from typing import List, Dict
from pathlib import Path
import json

from .objects_gen import PropertiesTypes


class Generator:
    """  """

    categories: Dict[str, Dict[str, dict]]

    def __init__(self, schema_path: str) -> None:
        data = json.loads(Path(schema_path).read_text())
        self.categories = sort_on_categories(data["methods"])


class SingleGenerator:
    """  """

    ...


class Parser:
    """  """

    ...


# FIXME: factory pattern
def sort_on_categories(methods: List[dict]) -> Dict[str, Dict[str, dict]]:
    """ Sorts methods on categories

    Returns: Dict[category: str, Dict[method_name: str, method: dict]]
    """

    categories: Dict[str, Dict[str, dict]] = {}

    for method in methods:
        category, method_name = method["name"].split(".")

        if category not in categories:
            categories.update({category: dict()})

        categories[category].update({method_name: method})

    return categories
