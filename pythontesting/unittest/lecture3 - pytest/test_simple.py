#to run test with pytest just call in console 'pytest' in proper directory
#tests need to have name starting with 'test' otherwise pytest won't find them

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

def test_perimeter():
    assert rectangle_perimeter(5, 7) == 24
