"""This module is for pulling financial data using various APIs.
"""
import abc
import quandl


class AssetBaseClass(metaclass=abc.ABCMeta):
    """Base class for various assets."""
    def __init__(self, ticker):
        """
        ticker (str): Ticker or equivalent label for the asset.
        """
        self.ticker = ticker

    @abc.abstractmethod
    def import_data(self):
        """Import asset data."""
        pass

    @abc.abstractmethod
    def clean_data(self):
        """Clean asset data for plotting and analysis."""
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
    def __init__(self, ticker, raw_data=None, clean_data=None):
        super().__init__(ticker)
        self.raw_data = {} if raw_data is None else raw_data
        self.clean_data = None if clean_data is None else clean_data

    def import_data(self,
                    start=None,
                    end=None,
                    resolution=None,
                    market=None,
                    base=None,
                    code=None,
                    type='numpy'):
        """Import data using the QUANDL API.

        Args:
            start ():
            end ():
            resolution (): Resolution of the data.
            market (str): Market to get data from.
            base (str): Base currency to obtain data for.
            code (str): Code to extract data for.
            type (str): Data type to return.

        Return:
            data (variable type): Raw data. See datatype Arg for type info.
        """
        code = self.ticker + '/' + base if code is None else code
        raw_data = quandl.get(code)
        raw_data_update = {'raw_data': raw_data,
                           'start': start,
                           'end': end,
                           'resolution': resolution,
                           'market': market,
                           'base': base,
                           'code': code,
                           'type': type}
        self.raw_data.update(raw_data_update)
        return raw_data_update

    def clean_data(self, raw_data=None):
        """Extract clean, human-readable, data from raw_data.

        Args:
            raw_data (Optional[Dict]): Raw data dict, such as the one returned
                by import_data.

        Returns:
            clean_data (Dict): Dictionary containing human-readable data.
        """
        return NotImplementedError()

    def plot_data(self, clean_data=None, plot_type='close', axis=None):
        """Plot clean data.

        Args:
            clean_data (Optional[Dict]): Clean data, such as the data returned
                by clean_data.
            plot_type (str): Type of plot. Supported plots: open, close, min,
                max, candle.
            axis (Optional[matplotlib.Axes.axes]): Axes to plot data on.

        Returns:
            axis (matplotlib.Axes.axes): Axes on which data are plotted.
        """
        return NotImplementedError()

    def load_data(self, absolute_path):
        return NotImplementedError()

    def save_data(self, absolute_path):
        return NotImplementedError()

