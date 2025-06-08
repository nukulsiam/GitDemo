#any pytest file should start with this "test_" keyword or end with _test
#pytest method names should start with test
#Every code should be wrapped in method

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")
    print("Success message to confirm if the push is succcessful")
    print("Success message to confirm if the push is succcessful222222")

@pytest.mark.xfail
def test_creditcard():
    print("Hello Goodbye")


def test_program1(crossBrowser):
    print(crossBrowser)
