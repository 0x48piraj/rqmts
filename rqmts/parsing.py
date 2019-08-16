#!/usr/bin/env python3

import pkg_resources

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
    modules = []
    code = code.splitlines()
    for item in code:
        if item[:7] == "import " and ", " not in item:
            if " as " in item:
                modules.append(item[7:item.find(" as ")])
            else:
                modules.append(item[7:])
        elif item[:5] == "from ":
            if "." in item[5:item.find(" import ")]:
                modules.append(item[5:item.find(" import ")].split(".")[0])
            else:
                modules.append(item[5:item.find(" import ")])
        elif ", " in item:
            item = item[7:].split(", ")
            modules = modules+item
        else:
            pass
    return list(set(modules))