#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pkg_resources, dis, ast
import importlib.util
from collections import defaultdict

def _import(imports):
    modules = {}
    errors = []
    for module in imports:
        try:
            modules[module] = __import__(module)
        except ImportError:
            errors.append(module)
    return modules, errors

def find_version(PKG_DIR):
    """
    Return value of __version__ (works on Python > 3.4)
    Reference: https://stackoverflow.com/a/42269185/
    """
    file_path = importlib.util.find_spec(PKG_DIR).origin
    with open(file_path) as file_obj:
        root_node = ast.parse(file_obj.read())
    for node in ast.walk(root_node):
        if isinstance(node, ast.Assign):
            if len(node.targets) == 1 and node.targets[0].id == "__version__":
                return node.value.s
    raise RuntimeError("Unable to find __version__ string.")

def fetch(package):
    try:
        pkg_name, pkg_version = pkg_resources.get_distribution(package).project_name, pkg_resources.get_distribution(package).version
    except:
        pkg_name, pkg_version = package, find_version(package)
    return pkg_name, pkg_version

def parse(code):
    instructions = dis.get_instructions(code)
    imports = [__ for __ in instructions if 'IMPORT' in __.opname]
    grouped = defaultdict(list)
    for instr in imports:
        if '.' in instr.argval: # dirty code
            grouped[instr.opname].append(instr.argval.split('.')[0])
        else:
            grouped[instr.opname].append(instr.argval)
    return grouped['IMPORT_NAME']