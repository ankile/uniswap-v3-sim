from typing import Union
from .gbq import *
from .allium import *

Connector = Union[gbq, allium]
