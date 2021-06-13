import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_assertionProgram():
    msg = "Hello"
    assert msg == "Hi","Test failed because strings do not match"

def test_calculationProgram():
    a=4
    b=6
    assert a+2==6,"Addition matches"