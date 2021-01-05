from typing import Tuple, List, Dict
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
    names_blacklist: Tuple[str] = (
        "from",
        "global",
        "class"
    )

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
            return getattr(Types(self, def_name, definition), def_type)()  # FIXME: Types -> self.types

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

    def parse_object_properties(self, properties: dict) -> List[str]:
        """  """

        output = list()

        for k, v in properties.items():
            prop_type = v.get("type")

            name = self.check_property_name(k)

            if prop_type is None:
                prop_type = self.parse_ref(v["$ref"])
            elif isinstance(prop_type, list):
                property_types = PropertiesTypes(self)  # FIXME: proptypes -> self
                p_types = [
                    getattr(property_types, i)(v)
                    for i in prop_type
                ]
                prop_type = f"Union[{', '.join(p_types)}]"
            else:
                prop_type = getattr(PropertiesTypes(self), prop_type)(v)  # FIXME: proptypes -> self

            output.append(f"{name}: {prop_type}")

        return output

    def check_property_name(self, name: str) -> str:
        """  """

        if name[0].isdigit() or name in self.names_blacklist:
            name = "_" + name
        return name


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
        props = self.definition.get("properties")
        if props is None:
            props = ["allOf: Unsupported"]  # TODO: allOf support
        else:
            props = self.parser.parse_object_properties(props)
        return utils.form_render(
            "object_class.j2",
            name=self.name,
            props=props
        )

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


class PropertiesTypes:
    """  """

    parser: Parser

    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    def integer(self, prop: dict) -> str:
        return "int"

    def string(self, prop: dict) -> str:
        return "str"

    def boolean(self, prop: dict) -> str:
        return "bool"

    def array(self, prop: dict) -> str:
        prop_type = prop["items"].get("type")
        if prop_type is None:
            ref = self.parser.parse_ref(prop["items"]["$ref"])
        else:
            ref = getattr(self, prop_type)(prop["items"])
        return f"List[{ref}]"

    def object(self, prop: dict) -> str:
        return "object"  # TODO: CHECK

    def number(self, prop: dict) -> str:
        return "int"
