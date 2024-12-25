# Trivial split for strings with multiple character delimiters, quotes and escaped characters

[![Downloads](https://pepy.tech/badge/tssplit/month)](https://pepy.tech/project/tssplit)
<a href="https://www.buymeacoffee.com/mezantrop" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Installation

```shell script
pip install tssplit
```

## Usage

### Syntax

```Python3
def tssplit(s:str, quote:str='"\'', quote_keep:bool=False, delimiter:str=':;,', escape:str='/^',
            trim:str='', remark:str='#') -> list[str]:

    """Split a string by delimiters with quotes and escaped characters, optionally trimming results

    :param s: A string to split into chunks
    :param quote: Quote chars to protect a part of s from parsing
    :param quote_keep: Preserve quote characters in the output or not
    :param delimiter: A chunk separator character
    :param escape: An escape character
    :param trim: Trim characters from chunks
    :param remark: Ignore all characters after remark sign
    :return: A list of chunks
    """
```

### Example

```Python3
import tssplit

tssplit('--:--;--,--"--/--"--\'--:--\'--/"--^--',
        quote='"\'', delimiter=':;,', escape='/^', trim='')
['--', '--', '--', '----/------:----"----']

tssplit('--:--;--,--"--/--"--\'--:--\'--/"--^--',
        quote='"\'', delimiter=':;,', escape='/^', trim='', quote_keep=True)
['--', '--', '--', '--"--/--"--\'--:--\'--"----']

tssplit('--:--;--,--"--/--"--\'--:--\'--# Ignore this',
        quote='"\'', delimiter=':;,', escape='/^', trim='', quote_keep=True, remark='#')
['--', '--', '--', '--"--/--"--\'--:--\'--']
```

## Changelog

* 2020.03.28    v1.0    Initial release
* 2020.03.28    v1.0.1  Many quick fixes to make all things work in PyPI
* 2020.03.29    v1.0.2  Minor fixes, Readme update, Long description provided
* 2020.03.29    v1.0.3  Trim option to strip() characters from chunks
* 2020.03.29    v1.0.4  Multiple characters for quotes, delimiters and escapes
* 2022.02.04    v1.0.5  Added `quote_keep` option to preserve quote marks in the output or not
* 2023.01.12    v1.0.6  Remark characters interrupt string parsing
* 2024.04.03    v1.0.7  Cosmetics to make pylint happy
* 2024.10.19    v1.0.8  Better module import; minor cosmetic changes
* 2024.12.25    v1.0.9  Type annotations by @mkupferman + misc minor changes
