""" This module is for testing assets.__init__.py
"""
import assets as ast


class TestStockClass(object):
    """Class for testing the Stock class"""

    @classmethod
    def setup_class(cls):
        cls.ticker = 'ABC'
        cls.time = [0, 1, 2, 3]
        cls.value = [3]*len(cls.time)
        cls.stock_inst = ast.Crypto(cls.ticker, cls.time, cls.value)

    def test_attributes(self):
        assert self.stock_inst.ticker == self.ticker
        assert self.stock_inst.time == self.time
        assert self.stock_inst.value == self.value

    def test_import_data(self):
        _ = self.stock_inst.import_data()

    def test_plot_data(self):
        _ = self.stock_inst.import_data()

    def test_load_data(self):
        _ = self.stock_inst.import_data()

    def test_save_data(self):
        _ = self.stock_inst.import_data()
