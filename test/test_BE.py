from src.app import isMobile

def test1():
    assert isMobile("BE","04-987-987-23") == True
def test2():
    assert isMobile("BE","+32-04-987-987-23") == True

def test3():
    assert isMobile("BE","+32-07-987-987-98") == False
def test4():
    assert isMobile("BE","07-987-987-98") == False
