from src.app import isMobile

def test1():
    assert isMobile("GB","07-987-987-987") == True
def test2():
    assert isMobile("UK","+44-07-685-987-987") == True
def test3():
    assert isMobile("GB","06-713-987-987") == False
def test4():
    assert isMobile("UK","+44-703-987-987-98") == False