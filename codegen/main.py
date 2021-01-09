from typing import Tuple, List, Set, Dict
from pathlib import Path
import json

import networkx as nx

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
        classes = dict([
            parser.parse_definition(k, v)
            for k, v in data.items()
        ])

        definition_sorter = DefinitionSorter(
            classes,
            parser.def_reqs
        )
        definitions = definition_sorter.process()

        text = utils.form_render(
            "main.j2",
            classes=definitions,
            requirements=parser.requirements,
            names=parser.objects_names
        )

        Path(output_path).write_text(text)


class Parser:
    """ Весь парсинг """

    requirements: Set[str]
    objects_names: List[str]
    file_name: str
    def_reqs: Dict[str, List[str]]
    properties_types: "PropertiesTypes"
    names_blacklist: Tuple[str] = (
        "from",
        "global",
        "class"
    )

    def __init__(self, file_name: str) -> None:
        self.requirements = set()
        self.objects_names = list()
        self.def_reqs = dict()
        self.properties_types = PropertiesTypes(self)
        self.file_name = file_name

    def parse_definition(self, def_name: str, definition: dict) -> Tuple[str, str]:
        """

        Returns: Tuple[definition_name: str, definition: str]
        """

        def_name = utils.snake_to_camel(def_name)
        def_type = definition.get("type")
        self.def_reqs.update({def_name: list()})

        if def_type is None:
            ref = self.parse_ref(definition["$ref"], brackets=False)
            self.add_def_reqs(def_name, ref)
            text = utils.form_render("ref_clone.j2", name=def_name, ref=ref)

        else:
            if def_type == "object":
                self.objects_names.append(def_name)
            text = getattr(Types(self, def_name, definition), def_type)()

        return def_name, text

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
            self.requirements.add(req)
            output = f"{req}.{cls_name}"
        else:
            output = cls_name

        if brackets:
            output = f'"{output}"'

        return output

    def parse_object_properties(self, properties: dict) -> List[Tuple[str, str]]:
        """  """

        output = list()

        for k, v in properties.items():
            prop_type = v.get("type")

            name = self.check_property_name(k)

            if prop_type is None:
                prop_type = self.parse_ref(v["$ref"])
            elif isinstance(prop_type, list):
                p_types = [
                    getattr(self.properties_types, i)(v)
                    for i in prop_type
                ]
                prop_type = f"Union[{', '.join(p_types)}]"
            else:
                prop_type = getattr(self.properties_types, prop_type)(v)

            output.append((name, prop_type))

        return output

    def parse_all_of(self, all_of: List[dict]) -> Tuple[List[str], List[Tuple[str, str]]]:
        """

        Returns: Tuple[parents: List[str], props: Dict[str, str]]
        """

        parents = list()
        props = list()

        for i in all_of:
            ref = i.get("$ref")
            if ref is None:
                props.extend(self.parse_object_properties(i["properties"]))
            else:
                parents.append(self.parse_ref(ref, brackets=False))

        if len(parents) == 0:
            parents.append("PydanticModel")

        return parents, props

    def check_property_name(self, name: str) -> str:
        """  """

        if name[0].isdigit() or name in self.names_blacklist:
            name = "_" + name
        return name

    def add_def_reqs(self, def_name: str, *refs: str):
        """  """

        for ref in refs:
            if "." not in ref:
                self.def_reqs[def_name].append(ref)


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
            all_of = self.definition.get("allOf")
            if all_of is None:
                return utils.form_render(
                    "void_object_class.j2",
                    name=self.name
                )
            else:
                parents, props = self.parser.parse_all_of(all_of)
                self.parser.add_def_reqs(self.name, *parents)
                return utils.form_render(
                    "all_of_object_class.j2",
                    name=self.name,
                    parents=parents,
                    props=props
                )
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
        enum_names = self.definition.get("enumNames")
        if enum_names is None:
            enum_names = self.definition["enum"]
        data = {
            utils.to_upper_snakecase(
                enum_names[i]
            ): self.definition["enum"][i]
            for i in range(len(enum_names))
        }
        return utils.form_render(
            "string_class.j2",
            name=self.name,
            enum=data
        )

    def boolean(self) -> str:
        return utils.form_render("boolean_class.j2", cls=self)


class PropertiesTypes:
    """  """

    parser: Parser

    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    def integer(self, prop: dict) -> str:
        return "int"

    def number(self, prop: dict) -> str:
        return "int"

    def string(self, prop: dict) -> str:
        return "str"

    def boolean(self, prop: dict) -> str:
        return "bool"

    def array(self, prop: dict) -> str:
        items = prop.get("items")

        if len(items) == 0:
            return "List[PydanticModel]"

        else:
            prop_type = items.get("type")
            if prop_type is None:
                ref = self.parser.parse_ref(prop["items"]["$ref"])
            else:
                if isinstance(prop_type, list):
                    refs = ", ".join([
                        getattr(self, i)(prop["items"])
                        for i in prop_type
                    ])
                    ref = f"Union[{refs}]"
                else:
                    ref = getattr(self, prop_type)(prop["items"])
        return f"List[{ref}]"

    def object(self, prop: dict) -> str:
        return "dict"  # FIXME: please.


class DefinitionSorter:
    """  """

    graph: nx.DiGraph
    definitions: Dict[str, str]

    def __init__(
        self,
        definitions: Dict[str, str],
        def_reqs: Dict[str, List[str]]
    ) -> None:

        self.graph = nx.DiGraph()
        self.definitions = definitions

        self.graph.add_nodes_from(definitions.keys())
        for k, v in def_reqs.items():
            for i in v:
                self.graph.add_edge(k, i)

    def process(self) -> List[str]:
        names = list(nx.topological_sort(self.graph))[::-1]
        return [
            self.definitions[i]
            for i in names
            if i != "PydanticModel"
        ]
