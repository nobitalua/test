import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_firstAutomation():
    print("Good everning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])