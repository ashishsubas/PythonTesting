import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.skip
def test_calculationProgramOutput():
    print("Added Correctly")

