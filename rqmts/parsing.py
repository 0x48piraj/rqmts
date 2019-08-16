#!/usr/bin/env python3

import pkg_resources, dis
from collections import defaultdict

def _import(imports):
 modules = {}
 for module in imports:
    try:
        modules[module] = __import__(module)
    except ImportError:
        print ("Error importing", module)
 return modules

def fetch(package):
 return pkg_resources.get_distribution(package).project_name, pkg_resources.get_distribution(package).version

def parse(code):
    instructions = dis.get_instructions(code)
    imports = [__ for __ in instructions if 'IMPORT' in __.opname]
    grouped = defaultdict(list)
    for instr in imports:
        grouped[instr.opname].append(instr.argval)
    return grouped['IMPORT_NAME']