from computer import divide
from computer import multiply
import pytest

@pytest.mark.parametrize(
    'a,b,x',
    [(1,2,0.5),(4,2,2)]
)
def test_divide(a , b, x):
    res = divide(a, b)
    assert  res == x

def test_multiply():
    assert multiply(2,2) == 4