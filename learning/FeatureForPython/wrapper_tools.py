
"""
@Author: liujinjia
@Date:   2017-02-08 09:41:15
@Project : LearningPython
@File : wrapper_tools.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-02-20 20:39:48
"""
<<<<<<< HEAD
import time

=======
>>>>>>> 2d777c8d07e6d9efb3d061eeef9e444be6bca360
from functools import update_wrapper


def wrapper(f):
    """ test wrapper def """
    def wrap(*args, **kwargs):
<<<<<<< HEAD
        start = time.time()
        result = f(*args, **kwargs)
        print(time.time() - start)
=======
        print("func start !")
        result = f(*args, **kwargs)
        print("func ended !")
>>>>>>> 2d777c8d07e6d9efb3d061eeef9e444be6bca360
        return result
    return update_wrapper(wrap, f)


@wrapper
<<<<<<< HEAD
def test_def():
    return test_def.__name__


@wrapper
def test(name):
=======
def hello(name):
>>>>>>> 2d777c8d07e6d9efb3d061eeef9e444be6bca360
    """ test wrapper """
    return "hello wrapper ! my name is {0}".format(name)


class A:
    """pass"""
    @classmethod
    @wrapper
    def a(cls, module):
        """pass"""
        func = getattr(eval(module), 'c')
        return func()

    @staticmethod
    def b():
        """pass"""
<<<<<<< HEAD
        A.a(A.a.__qualname__.split('.')[0])
        return A

    @classmethod
    def c(cls):
        """ pass"""
        print("hello")

if __name__ == '__main__':
    class_a = A()
    class_a.a('A')
    print(A.b())
    class_a.c()
=======
        return A.a.__qualname__.split('.')[0]
>>>>>>> 2d777c8d07e6d9efb3d061eeef9e444be6bca360
