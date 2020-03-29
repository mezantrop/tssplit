# tssplit - Trivial split for strings with escaped characters and quotes

## Installation
```shell script
pip install tssplit
```

## Usage
```python
from tssplit import tssplit

tssplit('ooooo/ooo|/ooo"XXX/XXX"ooo/"ooo/ooooo',  quote='"', delimiter='/', escape='|', trim='')
['ooooo', 'ooo/oooXXX/XXXooo', 'ooo/ooooo']
```

## Changelog
* 2020.03.28    v1.0    Initial release
* 2020.03.28    v1.0.1  Many quick fixes to make all things work in PyPI
* 2020.03.29    v1.0.2  Minor fixes, Readme update, Long description provided
* 2020.03.29    v1.0.3  Trim option to strip() characters from chunks
