from importlib.metadata import version

__version__ = version("lattica-pm")

from . import polymarket

__all__ = ["__version__", "polymarket"]
