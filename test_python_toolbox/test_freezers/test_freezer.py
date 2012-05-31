# Copyright 2009-2012 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''Testing package for `freezers.Freezer`.'''

from __future__ import with_statement

from python_toolbox import cute_testing

from python_toolbox.freezers import Freezer


class MyFreezer(Freezer):
    
    def __init__(self):
        Freezer.__init__(self)
        self.freeze_counter = 0
        self.thaw_counter = 0
        
    def freeze_handler(self):
        self.freeze_counter += 1
        return self.freeze_counter
        
    def thaw_handler(self):
        self.thaw_counter += 1


class MyException(Exception):
    ''' '''
        
        
def test():
            
    my_freezer = MyFreezer()
    assert not my_freezer.frozen
    assert my_freezer.frozen == 0
    
    with my_freezer as enter_return_value:
        assert my_freezer.frozen
        assert my_freezer.frozen == 1
        assert my_freezer.freeze_counter == enter_return_value == 1
        assert my_freezer.thaw_counter == 0
        with my_freezer as enter_return_value:
            assert my_freezer.frozen
            assert my_freezer.frozen == 2
            assert enter_return_value == 1
            assert my_freezer.freeze_counter == 1
            assert my_freezer.thaw_counter == 0
            with my_freezer as enter_return_value:
                assert my_freezer.frozen
                assert my_freezer.frozen == 3
                assert enter_return_value == 1
                assert my_freezer.freeze_counter == 1
                assert my_freezer.thaw_counter == 0
        assert my_freezer.frozen
        assert my_freezer.frozen == 1
        assert my_freezer.freeze_counter == 1
        assert my_freezer.thaw_counter == 0
    assert not my_freezer.frozen
    assert my_freezer.frozen == 0
    assert my_freezer.freeze_counter == 1
    assert my_freezer.thaw_counter == 1
    with my_freezer as enter_return_value:
        assert enter_return_value == 2
        assert my_freezer.freeze_counter == 2
        
    assert my_freezer.freeze_counter == 2
    assert my_freezer.thaw_counter == 2
    
    @my_freezer
    def f():
        pass
    
    f()
    
    assert my_freezer.freeze_counter == 3
    assert my_freezer.thaw_counter == 3
    
        
        
    
def test_exception():
    my_freezer = MyFreezer()
    with cute_testing.RaiseAssertor(MyException):
        assert not my_freezer.frozen
        assert my_freezer.freeze_counter == my_freezer.thaw_counter == 0
        with my_freezer:
            raise MyException
    assert my_freezer.freeze_counter == my_freezer.thaw_counter == 1
            
            
        