"""General utilities"""

import quandl
import os

API_KEYS_DIR = os.path.dirname(os.path.realpath(__file__))
API_KEYS_FILE = '/api_keys.rtf'


def get_api_key(directory=API_KEYS_DIR,
                filename=API_KEYS_FILE,
                source='QUANDL'):
    """Get API key for pulling data.
    
    It is assumed that API keys are stored in directory/filename: 
    
    Assumed file format:

    ***** TEXT START *****
    <source> <API key>
    <source 2> <API key>
    ...
    <source N> <API key>
    <new_line>
    ***** TEXT END *****
    
    Args: 
        directory (str): directory containing api key.
        filename (str): filename containing api key. 
        source (str): api source, e.g. QUANDL.


    """
    text = open(directory+filename, 'r').read()
    return text.split(source + ' ')[1].split('\\\n')[0]


def initialize_quandl(directory=API_KEYS_DIR,
                      filename=API_KEYS_FILE,
                      source='QUANDL'):
    """Initialize QUANDL API.

    mutates quandl.ApiConfig.api_key

    Args:
        directory (str): directory containing api key.
        filename (str): filename containing api key.
        source (str): api source, e.g. QUANDL.
    """
    quandl.ApiConfig.api_key = get_api_key(directory=directory,
                                           filename=filename,
                                           source=source)
