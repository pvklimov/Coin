""" This module is for testing assets.__init__.py
"""
import assets as ast


class TestCryptoClass(object):
    """Class for testing the Stock class"""

    @classmethod
    def setup_class(cls):
        cls.ticker = 'ABC'
        cls.crypto_inst = ast.Crypto(cls.ticker)

    def test_attributes(self):
        assert self.crypto_inst.ticker == self.ticker

