# -*- coding: utf-8 -*-

"""
Ole Martin Bjørndalen
ombdalen@gmail.com
http://nerdly.info/ole/
"""

__author__ = 'Ole Martin Bjørndalen'
__email__ = 'ombdalen@gmail.com'
__url__ = 'http://nerdly.info/ole/'
__license__ = 'MIT'
__version__ = '0.0.0'

__all__ = []  # Prevent splat import

from .parser import Parser, parse
from .serializer import serialize
# Todo: do this only if portmidi is found
# from .portmidi import Input, Output
