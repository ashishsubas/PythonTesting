import pytest


def test_CrossBrowser(crossbrowser):
    print(crossbrowser[1])


@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixtures(self):
        print("i will execute first")

    def test_fixtures1(self):
        print("i will execute second")

    def test_fixture(self):
        print("i will execute third")


