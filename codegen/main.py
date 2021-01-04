from typing import Tuple, List
from pathlib import Path
import json

from . import utils


class Generator:
    """  """

    schema_path: str

    def __init__(self, schema_path: str) -> None:
        self.schema_path = schema_path

    def read_data(self) -> Tuple[str, dict]:
        """

        Returns: Tuple[file_name: str, definitions: dict]
        """

        json_data = json.loads(Path(self.schema_path).read_text())
        return json_data["title"], json_data["definitions"]

    def write_file(self, output_path: str):
        """  """

        file_name, data = self.read_data()
        parser = Parser(file_name)
        classes = [
            parser.parse_definition(k, v)
            for k, v in data.items()
        ]

        text = utils.form_render(
            "main.j2",
            classes=classes,
            requirements=parser.requirements,
            names=parser.objects_names
        )

        Path(output_path).write_text(text)


class Parser:
    """ Весь парсинг """

    requirements: List[str]
    objects_names: List[str]
    file_name: str

    def __init__(self, file_name: str) -> None:
        self.requirements = list()
        self.objects_names = list()
        self.file_name = file_name

    def parse_definition(self, def_name: str, definition: dict) -> str:
        """  """

        def_name = utils.snake_to_camel(def_name)
        def_type = definition.get("type")

        if def_type is None:
            ref = self.parse_ref(definition["$ref"], brackets=False)
            return utils.form_render("ref_clone.j2", name=def_name, ref=ref)

        else:
            if def_type == "object":
                self.objects_names.append(def_name)
            return getattr(Types(self, def_name, definition), def_type)()

    def parse_ref(
        self,
        text: str,
        brackets: bool = True
    ) -> str:
        """ Получает имя класса в нужном формате """

        data = text.split("/")

        cls_name = utils.snake_to_camel(data[2])
        req = data[0].replace(".json#", "")

        if req != self.file_name:
            self.requirements.append(req)
            output = f"{req}.{cls_name}"
        else:
            output = cls_name

        if brackets:
            output = f'"{output}"'

        return output


class Types:
    """  """

    parser: "Parser"
    name: str
    definition: dict

    def __init__(
        self,
        parser: "Parser",
        name: str,
        definition: dict
    ) -> None:

        self.parser = parser
        self.name = name
        self.definition = definition

    def object(self) -> str:
        return ""

    def array(self) -> str:
        return utils.form_render(
            "array_class.j2",
            name=self.name,
            ref=self.parser.parse_ref(self.definition["items"]["$ref"])
        )

    def integer(self) -> str:
        data = {
            utils.to_upper_snakecase(
                self.definition["enumNames"][i]
            ): self.definition["enum"][i]
            for i in range(len(self.definition["enum"]))
        }
        return utils.form_render(
            "integer_class.j2",
            name=self.name,
            enum=data
        )

    def string(self) -> str:
        return utils.form_render("string_class.j2", cls=self)

    def boolean(self) -> str:
        return utils.form_render("boolean_class.j2", cls=self)
