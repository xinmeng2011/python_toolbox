# Copyright 2009-2012 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''Defines exceptions.'''

from python_toolbox.exceptions import CuteException


class SleekRefDied(CuteException):
    '''You tried to access a sleekref's value but it's already dead.'''