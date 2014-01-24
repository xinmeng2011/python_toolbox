# Copyright 2009-2014 Ram Rachum.
# This program is distributed under the MIT license.

from python_toolbox import cute_testing

from python_toolbox import monkeypatching_tools


def test():
    def f1(alpha, beta, *args, gamma=10, delta=20, **kwargs):
        return (alpha, beta, args, gamma, delta, kwargs)
    assert f1(1, 2) == (1, 2, (), 10, 20, {})
    
    monkeypatching_tools.change_defaults(f1, {'delta': 200,})
    assert f1(1, 2) == (1, 2, (), 10, 200, {})
    
    @monkeypatching_tools.change_defaults({'gamma': 100})
    def f2(alpha, beta, *args, gamma=10, delta=20, **kwargs):
        return (alpha, beta, args, gamma, delta, kwargs)
    assert f2(1, 2) == (1, 2, (), 100, 20, {})
        
    @monkeypatching_tools.change_defaults(new_defaults={'gamma': 1000})
    def f3(alpha, beta, *args, gamma=10, delta=20, **kwargs):
        return (alpha, beta, args, gamma, delta, kwargs)
    assert f3(1, 2) == (1, 2, (), 1000, 20, {})
        