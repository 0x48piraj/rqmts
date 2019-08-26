# Rqmts

[![PyPI Download/Month](https://img.shields.io/pypi/dm/rqmts.svg)](https://pypi.python.org/pypi/rqmts/)
[![PyPI Version](https://img.shields.io/pypi/v/rqmts.svg)](https://pypi.python.org/pypi/rqmts/)
[![PyPI license](https://img.shields.io/pypi/l/rqmts.svg)](https://pypi.python.org/pypi/rqmts/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rqmts.svg)](https://pypi.python.org/pypi/rqmts/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/rqmts.svg)](https://pypi.python.org/pypi/rqmts/)

<p align="center">
<b>Rqmts - Generate requirements.txt file for any project by analysing package imports</b><br><br>
    <img alt="Rqmts logo" src="https://i.imgur.com/czbQOUj.png" width="400"><br>
<b>Click <a href="https://youtube.com/">here</a> to see the demo.<br>
  Click <a href="https://github.com/0x48piraj/rqmts/wiki">here</a> for documentation.<br><br></b>
</p>

## About the project

**Rqmts** is a fantastic stand-alone tool which generates `requirements.txt` file for any project by analysing package imports.

It does not requires any dependency (works out-of-the-box), not needs internet to work _(is completely offline, upto this moment)_, nor uses regular expressions in such a violent way as existing projects do. Instead, it uses simple heuristic techniques and parse conditional trees, which is a better method for extracting imported names from statements, functions, etc.

## Why this project

### Questions

- **Why not just use pip's freeze command** to generate a `requirements.txt` file for my project ?
- Why to **re-invent the wheel** when there are modules such as **pipreqs**, **pigar**, **poetry** already present ?
- Why not manually ?

### Answers

* **Why not just pip freeze?**
   * ``pip freeze`` only saves the packages that are installed with ``pip install`` in your environment. 
   * ``pip freeze`` saves all packages in the environment including those that you don't use in your current project. _(if you don't have virtualenv)_
* Why **re-invent the wheel** ?
   * **pipreqs** fails on many occasions _(see - [pipreqs/issues](https://github.com/bndr/pipreqs/issues))_
   * I found this repository and thought, _"Hmm.. I think I can simply this problem while trying to match **pipreqs** results"_
   * **pigar** queries pypi servers, big no-no. Ideally, it should be local. _(on fallback? then maybe ..)_
   * Other than that, **pigar** recommends using Pipenv ([pipenv has serious issues](https://news.ycombinator.com/item?id=18612590))
   * **poetry** quotes "Be aware, however, that it will also install poetry's dependencies which might cause conflicts."
   * Sheer curiousity. _"can I create a project that has potential of collecting thosands of stars and most importantly, hundreds of contributors?"_
* Manually ?
   * _Are you serious right now ?_

## Installation

**Rqmts** provides a custom script that will run a **rqmts instance** isolated from the rest of your system by using file-less/memory-based execution. This is the recommended way of running Rqmts.

```
curl -sSL https://raw.githubusercontent.com/0x48piraj/rqmts/master/Rqmts.py | python
```

Alternatively, you can download `Rqmts.py` from the root directory and execute it separately.

Using **pip** to install [rqmts](https://pypi.org/project/rqmts/) is also possible.

```
pip install --user rqmts (windows)
pip3 install rqmts       (linux)
```

## Usage

#### Command-line Interface

```
C:\rqmts>py -m rqmts -h
usage: __main__.py [-h] [-p FILE]

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

Options:
  -p FILE, --path FILE  Path of the Python script (inside quotation marks)

--REDACTED--
C:\rqmts>py -m rqmts -p "C:\test_proj\run.py"

--REDATED--

[!] System package found : string
[!] System package found : time
[!] System package found : random
[!] System package found : os
[!] System package found : re
[+] Success: Parsed the dependencies correctly
[*] Saving generated requirements.txt
[+] Success: requirements.txt saved
[+] Path where it can be found: C:\test_proj\requirements.txt

```
[ ](ezgif-3-9a572478638c.gif)

#### Interactive mode

```
C:\rqmts>py -m rqmts
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

[*] Path not provided, invoking interactive mode ...
[*] Enter the path of Python script
    ----> C:\test_proj\run.py
[!] System package found : random
[!] System package found : os
[!] System package found : re
[!] System package found : time
[!] System package found : string
[+] Success: Parsed the dependencies correctly
[*] Saving generated requirements.txt
[+] Success: requirements.txt saved
[+] Path where it can be found: C:\test_proj\requirements.txt
```

## Contribute

The major challenge of this project is to extract the required metadata from modules which are first extracted from the input script.

#### Challenges

- **Version numbers in python can be in very different places depending on the case**
- **Package name in the package index is independent of the module name we import**

and these quirks make this project interesting. There's a funny comment in the source which reflects the diversity between us and it goes like :

```py
# module_name.__version__ sucks, because we suck (PEP 0396)
```

This project aims to combine the best existing strategies to cover the broadest possible set of cases _(if not all)_. The project was built keeping in mind the modular programming paradigms and so other than being readable it's easily extensible making it possible to add new strategies/algorithms quickly.

If you have any issues or suggestions, please do not hesitate to **[open an issue](https://github.com/0x48piraj/rqmts/issues/new)** or a **[pull request](https://github.com/0x48piraj/rqmts/pulls)**!

## License

This software is licensed under **BSD 3-Clause "New" or "Revised" License**. To view a copy of this license, visit **[BSD 3-Clause](LICENSE)**.
