"""Tests YAML utils."""
import io
import unittest

from ruamel.yaml import YAML, RoundTripRepresenter


def repr_str(dumper: RoundTripRepresenter, data: str):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class TestYAML(unittest.TestCase):
    def test_dump_load(self):
        # previous versions of ruamel.yaml would generate unparsable yaml
        # for certain combinations of whitespace and embedded yaml tokens
        cases = [
            "\nfoo: bar",
            " \nfoo: bar",
            " \n   foo: bar",
            " \n   foo: bar\n{}",
            " \n   foo: bar\n{}  ",
            " \n   foo: bar\n{}\n|\n{",
        ]
        for case in cases:
            obj = {"a": case}
            # yaml = YAML(typ="safe")
            yaml = YAML()
            yaml.representer.add_representer(str, repr_str)
            yaml.default_flow_style = False
            yaml.indent(sequence=4, offset=2)
            file = io.StringIO()
            yaml.dump(obj, file)
            ys = file.getvalue()
            # print(ys)
            yaml = YAML()
            r = yaml.load(ys)
            self.assertEqual(r, obj)
