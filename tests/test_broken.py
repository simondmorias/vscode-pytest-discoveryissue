import pytest
# This next line causes test discovery to break - comment it out and everything works
from src import broken

def test_simple():
    assert True