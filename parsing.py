#!/usr/bin/env python3

import subprocess

def call(query):
    return subprocess.getoutput(query)

def check(qry, data):
 for pkg in data:
     if qry in pkg:
         return pkg

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
            print(item)
    return list(set(modules))