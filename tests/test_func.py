from synthetic.func import boo, mbi_func


def test_boo():
    assert boo(3) == 6


def test_mbi_func():
    """
    This is a test for mbi_func, it should return an exception.
    :return:
    """
    assert mbi_func() == 2
