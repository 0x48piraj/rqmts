import os, subprocess

def query(qry, data):
 for pkg in data:
     if qry in pkg:
         return pkg

def parse_modules(code):
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
    return modules

file_path = input("Enter path of the python script : ")
dir_path = os.path.dirname(file_path)
with open(file_path, 'r') as f:
    code = f.read()
    f.close()

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