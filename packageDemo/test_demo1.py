import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "hi", "hien tai so sanh 2 chuoi dang la sai do"

@pytest.mark.xfail
def test_secondautomation():
    a = 6
    b = 4
    assert b + 2 == a, "dung roi"

@pytest.mark.smoke
def test_them():
    print("them coi co thay doi gi khong")
