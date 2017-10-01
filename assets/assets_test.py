""" This module is for testing assets.__init__.py
"""
import assets as ast


class TestStockClass(object):
    """Class for testing the Stock class"""

    @classmethod
    def setup_class(cls):
        cls.ticker = 'ABC'

    def test_attributes(self):
        assert self.stock_inst.ticker == self.ticker

    def test_import_data(self):
        _ = self.stock_inst.import_data()

    def test_plot_data(self):
        _ = self.stock_inst.import_data()

    def test_load_data(self):
        _ = self.stock_inst.import_data()

    def test_save_data(self):
        _ = self.stock_inst.import_data()
