import pytest

# bo set up de tao ket noi voi test_fixtureDemo, chi co bo setup vo moi co tac dung
#scope: co nghia la chi chay 1 lan trongp ham vi class, ko can phai lap di lap lai cho tat ca cac lan chay
#vi du:
#test_fixtureDemo.py::TestExample::test_fixtureDemo1 do it first
#test_fixtureDemo.py::TestExample::test_fixtureDemo2 PASSED
#test_fixtureDemo.py::TestExample::test_fixtureDemo4 PASSED
#do it last


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("do it in fixturedemo1 method")

    def test_fixtureDemo2(self):
        print("do it in fixturedemo2 method")

    def test_fixtureDemo3(self):
        print("do it in fixturedemo3 method")

    def test_fixtureDemo4(self):
        print("do it in fixturedemo4 method")
