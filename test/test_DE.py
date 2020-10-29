from src.app import isMobile

def test1():
    assert isMobile("DE","20-987-987-98") == True
def test2():
    assert isMobile("DE","+45-31-685-987") == True
def test3():
    assert isMobile("DE","41-713-987") == False
def test4():
    assert isMobile("DE","+45-51-703-987") == False