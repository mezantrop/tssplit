# tssplit - Trivial split for strings with escaped characters and quotes

## Usage
```python
from tssplit import tssplit

tssplit('qqqqq/qqq"qqq/qq"qqq/qqqqqq|/qqqqq', quote='"', delimiter='/', escape='|')

```