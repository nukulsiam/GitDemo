import pytest


@pytest.mark.usefixtures("data")
class TestExample2:

    def test_editProfile(self, data):
        print(data[1])
        print(data[2])

@pytest.mark.usefixtures("crossBrowser")
class TestExample3:
    def test_browser(self, crossBrowser):
        print(crossBrowser[1])

