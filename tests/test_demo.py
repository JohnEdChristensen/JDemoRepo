"""Tests the mathematical functions defined in demo/trail.py
"""

import pytest

def test_sqaure():
    """Tests the squaring function"""

    from JPackage.trial import square

    assert 4 == square(2)

def test_factorial():
    """Tests the factorial function."""

    from JPackage.trial import factorial

    assert 24 == factorial(4)
    assert 6 == factorial(3.0)
    assert 1 == factorial(0)
    assert 1 == factorial(-1)

    with pytest.raises(ValueError):
        factorial(3.5) 
