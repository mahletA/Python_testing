from computer import divide
from computer import multiply
import pytest
import numpy as np
from numpy.testing import assert_allclose
#from numpy.testing import assert

@pytest.mark.parametrize(
    'a,b,x',
    [(1,2,0.5),(4,2,2)]
)
def test_divide(a , b, x):
    res = divide(a, b)
    assert  res == pytest.approx(x)

#def test_divide(a , b, x):
#    res = divide(a, b)
#    assert  res == x

def test_multiply():
    assert multiply(2,2) == 4

def test_divide_array():
    a = np.array([1, 1, 1])
    b = np.array([2, 2, 2])
    x = divide(a, b)
    assert_allclose(x, np.array([0.5, 0.5, 0.5]))