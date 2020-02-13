import pytest
from src import works

def test_aPlusb():
    assert works.Works(1,1).answer == 2