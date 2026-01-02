from importlib.metadata import version

__version__ = version("lattica-pm")

from .polymarket.client import Polymarket
from .polymarket.config import PolymarketConfig

polymarket = Polymarket()

__all__ = ["__version__", "polymarket", "Polymarket", "PolymarketConfig"]
