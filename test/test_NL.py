from src.app import isMobile

def test1():
    assert isMobile("NL","06-987-987-23") == True
def test2():
    assert isMobile("NL","+31-06-987-987-23") == True
def test3():
    assert isMobile("NL","+31-03-987-987-23") == False
def test4():
    assert isMobile("NL","03-987-987-98") == False

