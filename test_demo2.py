#any pytest file should start with this "test_" keyword or end with _test
#pytest method names should start with test
#Every code should be wrapped in method
#Method name should have sense
# -k stands for method name selection, -s stands for logs in output, -v stands for more information like meta deta
#You can run specific file with py.test <filename>
#You can mark @pytest.mark.smoke and then run with -m
#you can skip the test cases with @pytest.mark.skip
#@pytest.mark.xfail is used to run the test but not reporting
#fixtures are used for setup and tear down methods for test cases- conftest file to generalise the fixture test
#fixture and make available to all the test cases
#Data driven adn paramaterization can be done with return
#When you define fixture scope to class only, it will run before class is initiated and class method are over


import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hello s", "test failed because condition string did not match"


def test_creditcard ():
    a = 2
    b = 3

    assert a + 1 == b, "test failed because the sum is not equal"

@pytest.fixture()
def setup():
    print("I will be executed first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")