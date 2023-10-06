from src.meta.singleton import SingletonMeta


def test_singleton_just_create_an_instance():
    class A(metaclass=SingletonMeta):
        pass

    i1 = A()
    i2 = A()
    assert i1 is i2
