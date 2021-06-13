import pytest


@pytest.fixture(params=[("Chrome", "Ashish"), ("Firefox", "Subash"), ("IE", "ashishsibas@gmail.com")])
def crossbrowser(request):
    return request.param


@pytest.fixture(scope="class")
def setup():
    print("Start with Ashish")
    yield
    print("End with Legend")


@pytest.fixture()
def Data():
    print("User profile data is created")
    return ["Ashish", "Hello"]
