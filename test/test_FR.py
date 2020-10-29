from src.app import isMobile

def test1():
    assert isMobile("FR","07-987-987-98") == True
def test2():
    assert isMobile("FR","+33-06-685-987-98") == True
def test3():
    assert isMobile("FR","01-713-987-98") == False
def test4():
    assert isMobile("FR","+44-02-703-987-98") == False