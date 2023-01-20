import os
import pathlib as pl
from enum import Enum
from typing import Union

import numpy as np

# Environment variables
numba_num_threads = os.getenv("NUMBA_NUM_THREADS")
if numba_num_threads is None:
    numba_num_threads = 0
else:
    numba_num_threads = int(numba_num_threads)

# Typing constants
fileish = Union[str, pl.Path]
listish = Union[str, list, tuple]

__pyswb_root__ = pl.Path(__file__).parent

CENTIMETERS_PER_INCH = 2.54
CUBIC_FT_PER_ACRE = 43560.0
INCHES_PER_FT = 12.0
