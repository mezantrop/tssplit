# Trivial split for strings with quotes and escaped characters

## Installation
```shell script
pip install tssplit
```

## Usage
```python
from tssplit import tssplit

tssplit('--:--;--,--"--/--"--\'--:--\'--/"--^--', quote='"\'', delimiter=':;,', escape='/^', trim='') 
['--', '--', '--', '----/------:----"----']
```

## Changelog
* 2020.03.28    v1.0    Initial release
* 2020.03.28    v1.0.1  Many quick fixes to make all things work in PyPI
* 2020.03.29    v1.0.2  Minor fixes, Readme update, Long description provided
* 2020.03.29    v1.0.3  Trim option to strip() characters from chunks
* 2020.03.29    v1.0.4  Multiple characters for quotes, delimiters and escapes
