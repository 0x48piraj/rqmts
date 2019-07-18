import os, sys, subprocess
from parsing import query, parse_modules

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

requirements_list = []
data = subprocess.getoutput("pip freeze").split()

for i in parse_modules(code):
    pkg_info = subprocess.getoutput("pip show {}".format(i))
    try:
        requirements_list.append(query(pkg_info.split("Name: ")[1].split('\nVersion:')[0], data))
    except:
        print("`{}` is a system package.".format(i))

print("[+] Success: Parsed the dependencies correctly")
print("[*] Saving generated requirements.txt")
REQS_PATH = dir_path + "\\requirements.txt"
with open(REQS_PATH, 'w') as g:
    for req in requirements_list:
        g.write(req + '\n')
    f.close()
print("[+] Success: requirements.txt saved")
print("[+] Path where it can be found: {}".format(REQS_PATH))