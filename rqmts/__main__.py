#!/usr/bin/env python3

import os, sys, argparse, textwrap
from .parsing import parse, fetch, _import

def main():
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
	    ||        @0x48piraj  /_____      /_____                           ||
	    ||                                                                 ||
	    '==================================================================='
	    ''')

	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=banner)
	optional = parser._action_groups.pop() # popped opt args
	optional = parser.add_argument_group('Options')
	optional.add_argument("-p", "--path", dest="path", metavar="FILE", default=False, help= "Path of the Python script (inside quotation marks)")

	file_path = parser.parse_args().path
	print(banner)
	if file_path == False:
	    print("[*] Path not provided, invoking interactive mode ...")
	    print("[*] Enter the path of Python script")
	    file_path = input("    ----> ")

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
	            print("[!] System package found :", package)

	print("[+] Success: Parsed the dependencies correctly")
	print("[*] Saving generated requirements.txt")

	with open(REQS_PATH, 'w') as g:
	    for req in requirements_list:
	        g.write(req + '\n')
	    g.close()

	print("[+] Success: requirements.txt saved")
	print("[+] Path where it can be found: %s" % (REQS_PATH))

if __name__ == "__main__":
    main()