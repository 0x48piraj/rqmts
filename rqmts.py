#!/usr/bin/env python3

import os, sys
from parsing import check, parse, call

requirements_list = []
pfreeze_cmd = "pip freeze"
pshow_cmd = "pip show {}"

file_path = input("Enter path of the python script : ")
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

INSTALLED_PKGS = call(pfreeze_cmd).split()
PARSED_PKG_LIST = parse(code)
for package in PARSED_PKG_LIST:
    pkg_info = call(pshow_cmd.format(package))
    pkg_query = pkg_info.split("Name: ")[1].split('\nVersion:')[0]
    try:
        result = check(pkg_query, INSTALLED_PKGS)
        requirements_list.append(result)
    except:
        print("[!] System package found : %s" % package)

print("[+] Success: Parsed the dependencies correctly")
print("[*] Saving generated requirements.txt")

REQS_PATH = dir_path + "\\requirements.txt"
with open(REQS_PATH, 'w') as g:
    for req in requirements_list:
        g.write(req + '\n')
    f.close()

print("[+] Success: requirements.txt saved")
print("[+] Path where it can be found: {}".format(REQS_PATH))