#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, argparse, textwrap
import pkg_resources, dis
import ast
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
        if '.' in instr.argval:
            grouped[instr.opname].append(instr.argval.split('.')[0])
        else:
            grouped[instr.opname].append(instr.argval)
    return grouped['IMPORT_NAME']

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
optional = parser._action_groups.pop() # popped opt args
optional = parser.add_argument_group('Options')
optional.add_argument("-p", "--path", dest="path", metavar=style.CYAN("'/path/to/file'") + style.RESET(''), default=False, help= style.GREEN("Python script path (inside quotation marks)") + style.RESET(''))

file_path = parser.parse_args().path
print(style.GREEN(banner) + style.RESET(''))
try:
    if file_path == False:
        print(style.YELLOW("[*] Path not provided, invoking interactive mode ..."))
        print("[*] Enter the path of Python script" + style.RESET(''))
        file_path = input(style.GREEN("    ----> ") + style.RESET('')).strip()
    else:
        file_path = file_path.strip()
except KeyboardInterrupt:
    print('Interrupted.')
    sys.exit(0) # http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF

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
if dir_path == '': # bad code
    REQS_PATH = "requirements.txt"
else:
    REQS_PATH = dir_path + "\\requirements.txt"
PARSED_PKG_LIST = parse(code)
modules, errors = _import(PARSED_PKG_LIST)
if len(PARSED_PKG_LIST) != len(modules) or len(errors) != 0:
    ERROR_MSG = (
                '\n\n'
                'Some modules were not successfully imported, and it means either of the two things :\n'
                '1. No such module(s) (just ignore this warning then)\n'
                '2. Module(s) not found in your system. (pip install <module-name>)'
            )
    print(style.YELLOW(ERROR_MSG) + style.RESET(''))
    print(style.YELLOW('There seems to be discrepancies in following module(s) :') + style.RESET(''))
    for num, module in enumerate(errors):
        print(num + 1, module)
    print(style.RED('Quitting.') + style.RESET(''))
    sys.exit(0)

"""Yes, we're not using https://github.com/jackmaney/python-stdlib-list"""
for name, data in zip(modules.keys(), modules.values()): # removing built-in modules from PARSED_PKG_LIST
    if "(built-in)" in str(data): # dirty, but reliable
        print(style.RED("[!] System (built-in) package found :"), style.CYAN(style.UNDERLINE(name)) + style.RESET(''))
        try:
            PARSED_PKG_LIST.remove(name)
        except ValueError:
            pass
    elif "\\lib\\" in str(data):
        print(style.RED("[!] Library package found :"), style.CYAN(style.UNDERLINE(name)) + style.RESET(''))
        try:
            PARSED_PKG_LIST.remove(name)
        except ValueError:
            pass
print(style.YELLOW("[+] Total modules used in %s => %d" % (style.CYAN(style.UNDERLINE(file_path)) + style.RESET(''), len(PARSED_PKG_LIST))) + style.RESET(''))
print(style.YELLOW("[*] Fetching versions ...") + style.RESET(''))
for package in PARSED_PKG_LIST:
    try:
        # Unfortunately, fetch() can error out too as name in the package index is independent of the module name we import
        pkg_name, version = fetch(package) # pkg.__version__ sucks, because we suck (PEP 0396)
        result = pkg_name + '==' + version
        requirements_list.append(result)
    except Exception as e:
        print(e)
if len(requirements_list) != len(PARSED_PKG_LIST):
    print(style.RED("[!] Failed to extract all versions.") + style.RESET(''))
print(style.GREEN("[+] Success: Parsed all the dependencies") + style.RESET(''))
print(style.YELLOW("[*] Saving generated ") + style.UNDERLINE("requirements.txt") + style.RESET(''))
try:
    with open(REQS_PATH, 'w') as g:
        for req in requirements_list:
            g.write(req + '\n')
        # removing the trailing newline, https://stackoverflow.com/a/18139508
        g.truncate(g.tell() - len(os.linesep))
        g.close()
except PermissionError:
    print(style.RED('Quitting. No permission to write on {}'.format(REQS_PATH)) + style.RESET(''))
    sys.exit(0)
print(style.GREEN("[+] Success: ") + style.GREEN(style.UNDERLINE("requirements.txt")) + style.RESET('') + style.GREEN(" saved") + style.RESET(''))
print(style.GREEN("[+] Path where it can be found: %s") % (style.GREEN(style.UNDERLINE(REQS_PATH))) + style.RESET(''))