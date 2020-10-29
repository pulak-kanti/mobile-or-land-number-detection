from src.app import isMobile

def test1():
    assert isMobile("ES","698-987-383") == True
def test2():
    assert isMobile("ES","+34-685-987-987") == True
def test3():
    assert isMobile("ES","+34-713-987-987") == True
def test4():
    assert isMobile("ES","+34-703-987-987-98") == False