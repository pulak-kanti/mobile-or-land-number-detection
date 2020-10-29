from src.app import isMobile

def test1():
    assert isMobile("IT","32-987-987-23") == True
def test2():
    assert isMobile("IT","+39-34-987-987-23") == True

def test3():
    assert isMobile("IT","+39-07-987-987-98") == False
def test4():
    assert isMobile("IT","07-987-987-98") == False