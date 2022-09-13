"""
Tests for our array class
"""

from array_class import Array
import pytest
import unittest

# 1D tests (Task 4)

a1 = Array((2,),1,2)

def test_str_1d():
    #Given:
    a1 = Array((2,),1,2)
    #When:
    representation_a1 = a1.__str__()
    #Then:
    assert isinstance(representation_a1, str)


def test_add_1d():
    #Given
    a1 = Array((4,), 4, 6, 2, 1)
    a2 = Array((4,), 2, 3, 1, 0)
    a3 = Array((4,), 1.5, 2.5, 3.4, 4.2)
    a4 = Array((4,), True, False, True, True)

    # Testing adding to arrays of ints. __add__() and __radd()__ is tested.
    # Adding of int, float and Array is tested.

    #when
    sum1 = a1 + 10
    #Then
    assert sum1.__str__() == "[14, 16, 12, 11]"

    rsum1 = 10 + a2
    assert rsum1.__str__() == "[12, 13, 11, 10]"

    sum2 = a1 + 1.5
    assert sum2.__str__() == "[5.5, 7.5, 3.5, 2.5]"

    rsum2 = 1.5 + a2
    assert rsum2.__str__() == "[3.5, 4.5, 2.5, 1.5]"

    sum3 = a1 + a2
    assert sum3.__str__() == "[6, 9, 3, 1]"

    # Testing adding to arrays of floats. __add__() and __radd()__ is tested.
    # Adding of int, float and Array is tested.

    #when
    sum1 = a3 + 10
    #Then
    assert sum1.__str__() == "[11.5, 12.5, 13.4, 14.2]"

    rsum1 = 10 + a3
    assert rsum1.__str__() == "[11.5, 12.5, 13.4, 14.2]"

    sum2 = a3 + 1.5
    assert sum2.__str__() == "[3.0, 4.0, 4.9, 5.7]"

    rsum2 = 1.5 + a3
    assert rsum2.__str__() == "[3.0, 4.0, 4.9, 5.7]"

    sum3 = a1 + a3
    assert sum3.__str__() == "[5.5, 8.5, 5.4, 5.2]"

    sum4 = a3 + a3
    assert sum4.__str__() == "[3.0, 5.0, 6.8, 8.4]"

    # Testing adding to Arrays of booleans and adding booleans to Arrays.
    # Since these attempts return 'NotImplemented', Python raises
    # a TypeError:

    with pytest.raises(TypeError):
        a4 + 10

    with pytest.raises(TypeError):
        10 + a4

    with pytest.raises(TypeError):
        a1 + True



def test_sub_1d():
    #Given
    a1 = Array((2,), 4, 6)
    a2 = Array((2,), 3.4, 4.2)
    a3 = Array((2,), True, False)

    # Testing subtraction from arrays of ints. __add__() and __radd()__ is tested.
    # Subtraction of int, float and Array is tested.

    #when
    dif1 = a1 - 2
    #Then
    assert dif1.__str__() == "[2, 4]"

    rdif1 = 2 - a1
    assert rdif1.__str__() == "[-2, -4]"

    dif2 = a1 - 1.5
    assert dif2.__str__() == "[2.5, 4.5]"

    rdif2 = 3.5 - a1
    assert rdif2.__str__() == "[-0.5, -2.5]"

    dif3 = a1 - a1
    assert dif3.__str__() == "[0, 0]"

    # Testing subtraction from arrays of floats. __add__() and __radd()__ is tested.
    # Subtraction of int, float and Array is tested.

    #when
    dif4 = a2 - 2
    #Then

    assert pytest.approx(1.4, 0.1) == dif4[0]
    assert pytest.approx(2.2, 0.1) == dif4[1]

    rdif3 = 2 - a2
    assert pytest.approx(rdif3[0], 0.1) == -1.4
    assert pytest.approx(rdif3[1], 0.1) == -2.2

    dif5 = a2 - 1.5
    assert pytest.approx(dif5[0], 0.1) == 1.9
    assert pytest.approx(dif5[1], 0.1) == 2.7

    dif6 = a2 - a1
    assert pytest.approx(-0.6, 0.2) == dif6[0]
    assert pytest.approx(-1.8, 0.2) == dif6[1]


    # Testing subtraction from Arrays of booleans and subtraction of booleans from Arrays.
    # Since these attempts return 'NotImplemented', Python raises
    # a TypeError:

    with pytest.raises(TypeError):
        a3 - 10

    with pytest.raises(TypeError):
        10 - a3

    with pytest.raises(TypeError):
        a2 - True


def test_mul_1d():
    #Given
    a1 = Array((2,), 4, 6)
    a2 = Array((2,), 2, 3)
    a3 = Array((2,), 3.4, 4.2)
    a4 = Array((4,), True, False, True, True)

    # Testing multiplication of arrays and int. __add__() and __radd()__ is tested.
    # Adding of int, float and Array is tested.

    #when
    mul1 = a1 * 10
    #Then
    assert mul1.__str__() == "[40, 60]"

    rmul1 = 10 * a2
    assert rmul1.__str__() == "[20, 30]"

    mul2 = a1 * 1.5
    assert mul2.__str__() == "[6.0, 9.0]"

    rmul2 = 1.5 * a1
    assert rmul2.__str__() == "[6.0, 9.0]"

    mul3 = a1 * a2
    assert mul3.__str__() == "[8, 18]"

    # Testing multiplication with arrays of floats. __add__() and __radd()__ is tested.
    # Multiplication of int, float and Array is tested.

    #when
    mul4 = a3 * 2
    #Then

    assert pytest.approx(6.8, 0.1) == mul4[0]
    assert pytest.approx(8.4, 0.1) == mul4[1]

    mul3 = 2 * a3
    assert pytest.approx(6.8, 0.1) == mul4[0]
    assert pytest.approx(8.4, 0.1) == mul4[1]

    mul5 = a2 * 1.5
    assert pytest.approx(mul5[0], 0.1) == 3.0
    assert pytest.approx(mul5[1], 0.1) == 4.5

    mul6 = a3 * a1
    assert pytest.approx(13.6, 0.2) == mul6[0]
    assert pytest.approx(25.2, 0.2) == mul6[1]

    # Testing multiplication with Arrays of booleans and multiplication of booleans to Arrays.
    # Since these attempts return 'NotImplemented', Python raises
    # a TypeError:

    with pytest.raises(TypeError):
        a4 * 10

    with pytest.raises(TypeError):
        10 * a4

    with pytest.raises(TypeError):
        a2 - True


def test_eq_1d():
    #Given
    a1 = Array((2,), 4, 6)
    a2 = Array((2,), 4, 3)
    #Then
    assert (a1 == a2) == True

    #Given
    a1 = Array((3,), 4, 6, 7)
    a2 = Array((2,), 4, 3)
    #Then
    assert (a1 == a2) == False

def test_same_1d():
    #Given
    a1 = Array((2,), 4, 6)
    a2 = Array((2,), 4, 3)
    #Then
    assert a1.is_equal(a2).__str__() == "[True, False]"

def test_smallest_1d():
    #given
    a1 = Array((3,),1,2,3)

    assert a1.min_element() == 1

def test_mean_1d():
    #given
    a1 = Array((4,),4,2,1,5)

    assert a1.mean_element() == 3


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
