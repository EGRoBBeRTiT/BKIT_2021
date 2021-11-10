from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    #использование внешнего пакета numpy
    a = numpy.array([1, 4, 5, 8], float)
    print(a)
    

if __name__ == "__main__":
    main()