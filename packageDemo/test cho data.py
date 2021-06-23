import pytest

@pytest.mark.usefixtures("dataload")
class TestExample2:
    def test_chaydulieu (self,dataload):
        print(dataload)
        print(dataload[1])