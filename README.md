# Python basic exampels

This repo is for my colleagues to get started with python to see some bsaic python concepts.

Also trying some pytest

## Virtual env handling

### Install our virtual env handler
```pip3 install pipenv```

### Start the virtual env
```pipenv shell```

### Install requests package
```pipenv install requests```

### Install pytest
```pipenv install --dev pytest```

## Good articels

### For a good article about requests check out
https://realpython.com/python-requests/

### Article about pathlib
https://realpython.com/python-pathlib/

### Article about f string
https://realpython.com/python-f-strings/

### Type hints
https://realpython.com/python-type-checking/

If you want real typeing use [mypy](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
)

Developed by dropbox and python language creator
Guido van Rossum


Microsoft have also written type checker called [pyright](https://github.com/microsoft/pyright
) that they say is much quicker then mypy.

But mypy is more used and if you don't write a realy big project you won't need it.

## Libaries

### Codeformater use black
Sadly [black](https://github.com/python/black) don't work great with pipenv due to that still say they are in beta...

And pipenv is not a big fan of the beta stuff that is possible in pip. To install black write:

```pipenv install black --skip-lock --dev```

Sadly this ruins your lock file and creates
