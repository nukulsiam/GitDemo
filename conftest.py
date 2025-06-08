import pytest


# @pytest.fixture(scope="class")                      #before the class initialise and after the class is executed
# def setup():
#     print("I will be executed first")
#     yield
#     print("I will be executed after the fixtureDemo method is executed")
@pytest.fixture()
def setup():
    print("setting up the setup method")


@pytest.fixture()
def data():
    print("User profile data has been created")
    return ["Nukul","Saxena","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Nukul", "Saxena"), ("firefox", "Gaurav"), ("edge", "Vedant")])                #the () bracket is used such that those values will used for first run and then in the second run the second firefox value will be done.
def crossBrowser(request):
    return request.param
