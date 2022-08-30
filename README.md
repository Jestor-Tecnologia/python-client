# Jestor SDK for Python - Version Beta

[![PyPI](https://img.shields.io/pypi/v/jestor.svg)](https://pypi.python.org/pypi/jestor)
[![PyPI](https://img.shields.io/pypi/pyversions/jestor.svg)](https://pypi.python.org/pypi/jestor)

Jestor client library for python.


## Documentation

Documentation with all available functions can be found [here](https://docs.jestor.com/docs/jestor-sdk-for-python)

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.

`pip install jestor`

If pip install fails on Windows, check the path length of the directory. If it is greater 260 characters then enable [Long Paths](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) or choose other shorter location.

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://bootstrap.pypa.io/get-pip.py | python


## Getting Started

Getting started with the Jestor API couldn't be easier. Create a
`Jestor` instance and you're ready to go.

```python
from jestor.Jestor import Jestor

jestor_client = Jestor('<api token>', '<account>')

result = jestor_client.table('sample_tab').get(limit=3) # result will be a python array with values
```
