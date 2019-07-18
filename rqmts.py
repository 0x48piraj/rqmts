import subprocess

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


f=open('{}'.format(input("Enter the name of the python file : ")), 'r')
code = f.read()
requirements_list = []
data = subprocess.getoutput("pip freeze").split()

for i in parse_modules(code):
    pkg_info = subprocess.getoutput("pip show {}".format(i))
    try:
        requirements_list.append(query(pkg_info.split("Name: ")[1].split('\nVersion:')[0], data))
    except:
        print("`{}` is a system package.".format(i))
"""
if os.name == "nt": # import platform;platform.system() == "Windows";from sys import platform as _platform;print(_platform)
    for i in parse_modules(code):
        requirements_list.append(subprocess.getoutput("pip freeze | findstr {}".format(i)))

else:
    for i in parse_modules(code):
        requirements_list.append(subprocess.getoutput("pip freeze | grep {}".format(i)))
"""
print(requirements_list)