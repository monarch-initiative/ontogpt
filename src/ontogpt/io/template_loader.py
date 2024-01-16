"""Loader functions for extraction templates."""

import importlib
import logging
from pathlib import Path

from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import ClassDefinition

TEMPLATE_NAME = str

this_path = Path(__file__).parent
logger = logging.getLogger(__name__)


def get_template_details(template: TEMPLATE_NAME) -> ClassDefinition:
    """
    Get the LinkML class, module, and schemaview for a template.

    :param template: template name of the form module.ClassName
    :return: tuple of (LinkML class definition, module, specific
    Python class, schemaview)
    """
    logger.info(f"Loading schema for {template}")
    if "." in template:
        module_name, class_name = template.split(".", 1)
    else:
        module_name = template
        class_name = None
    templates_path = this_path.parent / "templates"
    path_to_template = str(templates_path / f"{module_name}.yaml")
    sv = SchemaView(path_to_template)
    if class_name is None:
        roots = [c.name for c in sv.all_classes().values() if c.tree_root]
        if len(roots) != 1:
            raise ValueError(f"Template {template} does not have singular root: {roots}")
        class_name = roots[0]
    mod = importlib.import_module(f"ontogpt.templates.{module_name}")
    pyclass = mod.__dict__[class_name]

    logger.info(f"Getting class for template {template}")
    cls = None
    for c in sv.all_classes().values():
        if c.name == class_name:
            cls = c
            break
    if not cls:
        raise ValueError(f"Template {template} not found")
    return (cls, mod, pyclass, sv)
