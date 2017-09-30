"""This module is for pulling financial data using various APIs.
"""
import abc


class AssetBaseClass(metaclass=abc.ABCMeta):
    """Base class for various assets."""
    def __init__(self, ticker, time, value):
        """
        ticker (str): Ticker or equivalent label for the asset.
        time (list-like): Time axis for the asset. Corresponds to value.
        value (list-like): Value of the asset. Corresponds to time.
        """
        self.ticker = ticker
        self.time = time
        self.value = value

    @abc.abstractmethod
    def import_data(self):
        """Import asset data."""
        pass

    @abc.abstractmethod
    def plot_data(self):
        """Plot asset data."""
        pass

    @abc.abstractmethod
    def load_data(self):
        """Load data from disk."""

    @abc.abstractmethod
    def save_data(self):
        """Save data to disk."""
        pass


class Crypto(AssetBaseClass):
    def __init__(self, ticker, time, value):
        super().__init__(ticker, time, value)

    def import_data(self):
        return NotImplementedError()

    def plot_data(self):
        return NotImplementedError()

    def load_data(self):
        return NotImplementedError()

    def save_data(self):
        return NotImplementedError()

