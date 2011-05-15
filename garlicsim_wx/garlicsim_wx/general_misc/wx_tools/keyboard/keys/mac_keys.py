# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''This module defines Mac-specific keys.'''

from garlicsim.general_misc.wx_tools.keyboard import Key


back_keys = (
    Key(ord('['), cmd=True),
    Key(wx.WXK_LEFT, cmd=True)
)

back_key_string = u'\u2318\u00ab'

forward_keys = (
    Key(ord(']'), cmd=True),
    Key(wx.WXK_RIGHT, cmd=True)
)

forward_key_string = u'\u2318\u00bb'
