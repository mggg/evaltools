
"""
Provides ease-of-use functionality for geographic and geometric operations.
"""

from .dissolve import dissolve
from .dualgraph import dualgraph
from .unitmap import unitmap, invert
from .dataframe import dataframe
from .compactness import _reock
from gerrychain import Graph, Partition

from .optimize import (
    minimize_dispersion, minimize_dispersion_with_parity, minimize_parity,
    calculate_dispersion
)

from .updater import dispersion_updater_closure

__all__ = [
    "minimize_dispersion",
    "minimize_dispersion_with_parity",
    "minimize_parity",
    "calculate_dispersion",
    "dispersion_updater_closure",
    "dissolve",
    "dualgraph",
    "unitmap",
    "invert",
    "dataframe",
    "_reock"
]
