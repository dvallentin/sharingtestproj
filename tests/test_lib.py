# tests/test_lib.py
from sharingtestproj.lib import try_me

def test_sum():
    assert try_me(42, 84) == 126