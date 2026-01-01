from importlib.metadata import version

__version__ = version("lattica-pm")

from .polymarket.api import PolymarketAPI

polymarket = PolymarketAPI()

__all__ = ["__version__", "PolymarketAPI"]
