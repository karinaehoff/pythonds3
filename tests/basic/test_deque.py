'''
Testing the Deque module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import sys, os
print(sys.path)
sys.path.insert(0, os.path.abspath('../..'))

import pytest
from pythonds3.basic.deque import Deque
      
class TestDequeMethods:
    
    @pytest.fixture(scope = 'function', autouse = True)
    def setup_class(cls):
        '''Setting up'''
        cls.deque = Deque()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        assert self.deque.is_empty()
        self.deque.add_front(42)
        assert not self.deque.is_empty()

    def test_size(self):
        '''Testing size() method'''
        assert self.deque.size() == 0
        self.deque.add_front(42)
        assert self.deque.size() == 1

    def test_add_front(self):
        '''Testing add_front() method'''
        self.deque.add_front(42)
        assert self.deque.size() == 1

    def test_add_rear(self):
        '''Testing add_rear() method'''
        self.deque.add_rear(42)
        assert self.deque.size() == 1

    def test_remove_front(self):
        '''Testing remove_front() method'''
        self.deque.add_front(42)
        assert self.deque.remove_front() == 42
        assert self.deque.is_empty()

    def test_remove_rear(self):
        '''Testing remove_rear() method'''
        self.deque.add_rear(42)
        assert self.deque.remove_rear() == 42
        assert self.deque.is_empty()

if __name__ == '__main__':
    pytest.main(['test_deque.py'])
