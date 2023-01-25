import os
import pathlib as pl
from enum import Enum
from typing import Union

import numpy as np

import sys    
print("In module constants sys.path[0], __package__ ==", sys.path[0], __package__)

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

DEGREES_TO_RADIANS = (2.0 * np.pi) / 360.0
RADIANS_TO_DEGREES = 360.0 / (2.0 * np.pi) 
#DEGREES_TO_RADIANS =  0.017453292519943295
#RADIANS_TO_DEGREES = 57.29577951308232
