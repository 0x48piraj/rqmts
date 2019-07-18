#!/usr/bin/env python3

import os, sys, argparse
from parsing import check, parse, call

parser = argparse.ArgumentParser(description='rqmts - Generate pip requirements.txt file for any project')
#optional = parser._action_groups.pop() # popped opt args
#optional = parser.add_argument_group('Parameters')
parser.add_argument("-p", "--path", dest="path", default=False, help= "Path of the Python script")

file_path = parser.parse_args().path
if file_path == False:
    print("[*] Path not provided, invoking interactive mode ...")
    file_path = input("Enter the path of Python script : ")

if os.path.exists(file_path):
 dir_path = os.path.dirname(file_path)
 with open(file_path, 'r') as f:
    try:
        code = f.read()
        f.close()
    except:
        print("[-] File failed to load. Exiting ...")
        sys.exit(1)
else:
 print("[-] Invalid path. Exiting ...")
 sys.exit(1)

requirements_list = []
pfreeze_cmd = "pip freeze"
pshow_cmd = "pip show {}"
REQS_PATH = dir_path + "\\requirements.txt"
INSTALLED_PKGS = call(pfreeze_cmd).split()
PARSED_PKG_LIST = parse(code)

for package in PARSED_PKG_LIST:
    pkg_info = call(pshow_cmd.format(package))
    try:
        pkg_query = pkg_info.split("Name: ")[1].split('\nVersion:')[0]
        result = check(pkg_query, INSTALLED_PKGS)
        requirements_list.append(result)
    except:
        print("[!] System package found : %s" % package)

print("[+] Success: Parsed the dependencies correctly")
print("[*] Saving generated requirements.txt")

with open(REQS_PATH, 'w') as g:
    for req in requirements_list:
        g.write(req + '\n')
    g.close()

print("[+] Success: requirements.txt saved")
print("[+] Path where it can be found: {}".format(REQS_PATH))