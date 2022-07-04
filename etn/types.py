from typing import Optional, Union
from collections.abc import Iterable

SQL_PARAM = tuple[Union[int, str, bool, float], ...]
SQL_PARAMS = Optional[Union[SQL_PARAM, Iterable[SQL_PARAM]]]
