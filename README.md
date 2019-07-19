# rqmts

<p align="center">
<b>rqmts - Generate pip requirements.txt file for any project by analysing package imports</b><br><br>
Click <a href="https://youtube.com/">here</a> to see the demo.<br>
  Click <a href="https://github.com/0x48piraj/rqmts/wiki">here</a> for documentation.<br><br>
</p>

## About the project

**rqmts** is a fantastic stand-alone tool which generates pip `requirements.txt` file for any project by analysing package imports.

It does not requires any dependency (works out-of-the-box), not needs internet to work _(is completely offline, upto this moment)_, nor uses regular expressions in such a violent way as existing projects do. Instead, it uses simple heuristic techniques and parse conditional trees, which is a better method for extracting imported names from statements, functions, etc.

## Why this project

### Questions

- **Why not just use pip’s freeze command** to generate a `requirements.txt` file for my project ?
- Why to **re-invent the wheel** when there are modules such as **pipreqs**, **pigar** already present ?
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
   * Sheer curiousity. _"I wonder if I can create a project that has potential of thosands of stars and most importantly, hundreds of contributors under 24 hours"_
* Manually ?
   * _Are you serious right now ?_

## Installation

```
pip install --user rqmts
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

If you have any issues or suggestions, please do not hesitate to [open an issue](https://github.com/0x48piraj/rqmts/issues/new) or a [pull request](https://github.com/0x48piraj/rqmts/pulls)!

## License

This software is licensed under BSD 3-Clause "New" or "Revised" License. To view a copy of this license, visit [BSD 3-Clause](LICENSE).