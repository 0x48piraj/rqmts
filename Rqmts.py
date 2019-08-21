#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, argparse, textwrap
import pkg_resources, dis
from collections import defaultdict

if sys.platform.lower() == "win32":
    os.system('color')
    # Group of Different functions for different styles
    class style():
        BLACK = lambda x: '\033[30m' + str(x)
        RED = lambda x: '\033[31m' + str(x)
        GREEN = lambda x: '\033[32m' + str(x)
        YELLOW = lambda x: '\033[33m' + str(x)
        BLUE = lambda x: '\033[34m' + str(x)
        MAGENTA = lambda x: '\033[35m' + str(x)
        CYAN = lambda x: '\033[36m' + str(x)
        WHITE = lambda x: '\033[37m' + str(x)
        UNDERLINE = lambda x: '\033[4m' + str(x)
        RESET = lambda x: '\033[0m' + str(x)
else:
    class style():
        BLACK = ""
        RED = ""
        GREEN = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        UNDERLINE = ""
        RESET = ""

def _import(imports):
 modules = {}
 for module in imports:
    try:
        modules[module] = __import__(module)
    except ImportError:
        print(style.RED("[!] Error importing :"), style.CYAN(style.UNDERLINE(module)) + style.RESET('')) # TODO: RET err module, bug: system module found : this.module
 return modules

def parse(code):
    instructions = dis.get_instructions(code)
    imports = [__ for __ in instructions if 'IMPORT' in __.opname]
    grouped = defaultdict(list)
    for instr in imports:
        grouped[instr.opname].append(instr.argval)
    return grouped['IMPORT_NAME']

def fetch(package):
 return pkg_resources.get_distribution(package).project_name, pkg_resources.get_distribution(package).version

banner = textwrap.dedent('''\
    .===================================================================.
    ||      rqmts - Generate pip requirements.txt for any project      ||
    ||                                                                 ||
    ||                                                                 ||
    ||                            ___                                  ||
    ||                          .'   '.              requirements.txt  ||
    ||                         / rqmts \           oOoOo.              ||
    ||                        |    |    |       ,==|||||o.             ||
    ||                         \  pip  /       _|| |||||o. pip         ||
    ||                          '.___.'    _.-'^|| |||||               ||
    ||                        __/_______.-'     '==rqmts               ||
    ||                   _.-'` /                   """""               ||
    ||                .-'     /   oOoOo.                               ||
    ||                `-._   / ,==|||||o.                              ||
    ||                    '-/._|| |||||o. python                       ||
    ||                     /  ^|| |||||                                ||
    ||                    /    '==rqmts                                ||
    ||                   /________"""""                                ||
    ||                   `\       `\                                   ||
    ||                     \        `\                                 ||
    ||                      \         `\                               ||
    ||                      /           /                              ||
    ||                     /           /                               ||
    ||     [>] @0x48piraj /_____      /_____                           ||
    ||                                                                 ||
    '==================================================================='
    ''')

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=style.GREEN(banner) + style.RESET(''), usage=style.GREEN("rqmts ") + style.YELLOW("[-h] [-p '{}']").format(style.UNDERLINE("/path/to/file") + style.RESET('') + style.YELLOW('')) + style.RESET(''))
optional = parser._action_groups.pop() # popped default opt args
optional = parser.add_argument_group('Options')
optional.add_argument("-p", "--path", dest="path", metavar=style.CYAN("'/path/to/file'") + style.RESET(''), default=False, help= style.GREEN("Python script path (inside quotation marks)") + style.RESET(''))

file_path = parser.parse_args().path
print(style.GREEN(banner) + style.RESET(''))
if file_path == False:
    print(style.YELLOW("[*] Path not provided, invoking interactive mode ..."))
    print("[*] Enter the path of Python script" + style.RESET(''))
    file_path = input(style.GREEN("    ----> ") + style.RESET('')).strip()
else:
    file_path = file_path.strip()

if os.path.exists(file_path):
 dir_path = os.path.dirname(file_path)
 with open(file_path, 'r') as f:
    try:
        code = f.read()
        f.close()
    except:
        print(style.RED("[-] File failed to load. Exiting ...") + style.RESET(''))
        sys.exit(1)
else:
 print(style.RED("[-] Invalid path. Exiting ...") + style.RESET(''))
 sys.exit(1)

requirements_list = []
REQS_PATH = dir_path + "\\requirements.txt"
PARSED_PKG_LIST = parse(code)
modules = _import(PARSED_PKG_LIST) # must run w/o errors or you've some fucked up imports
for package in PARSED_PKG_LIST:
    try:
        # Unfortunately, fetch() can error out too as name in the package index is independent of the module name we import
        pkg_name, version = fetch(package) # pkg.__version__ sucks, because we suck (PEP 0396)
        result = pkg_name + '==' + version
        requirements_list.append(result)
    except Exception as e:
        if e.__class__.__name__ == "ModuleNotFoundError":
            print("[!] ERROR: {} !(valid || installed)".format(package))
        elif e.__class__.__name__ == "DistributionNotFound":
            # hacky patch
            # pkg_name, version = fetch(dir(package)[0]) # works on pymouse, strgen
            print(style.RED("[!] System package found :"), style.CYAN(style.UNDERLINE(package)) + style.RESET(''))

print(style.GREEN("[+] Success: Parsed all the dependencies") + style.RESET(''))
print(style.YELLOW("[*] Saving generated ") + style.UNDERLINE("requirements.txt") + style.RESET(''))

with open(REQS_PATH, 'w') as g:
    for req in requirements_list:
        g.write(req + '\n')
    g.close()

print(style.GREEN("[+] Success: ") + style.GREEN(style.UNDERLINE("requirements.txt")) + style.RESET('') + style.GREEN(" saved") + style.RESET(''))
print(style.GREEN("[+] Path where it can be found: %s") % (style.GREEN(style.UNDERLINE(REQS_PATH))) + style.RESET(''))