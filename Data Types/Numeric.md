"""Numbers.
```python

In Python, there are three built-in numeric data types:

Integers (int): Integers are whole numbers without a decimal point. They can be positive, negative, or zero. For example, 42, -1, and 0 are all integers.
Floating-point numbers (float): Floating-point numbers are numbers with a decimal point. They can be positive, negative, or zero. For example, 3.14, -0.5, and 2.0 are all floats.
Complex numbers (complex): Complex numbers are numbers with a real and imaginary component. They are written in the form a + bj, where a is the real part and b is the imaginary part. For example, 3 + 2j, -1 - 2j, and 4j are all complex numbers.
Numeric data types in Python can be used in arithmetic expressions, such as addition, subtraction, multiplication, and division. Python also provides various built-in functions and modules for working with numeric data, such as abs() for finding the absolute value, round() for rounding to a specified number of decimal places, and math module for more advanced mathematical operations.

It's important to keep in mind that certain operations may produce unexpected results due to the limitations of floating-point arithmetic. For example, adding 0.1 and 0.2 may not result in exactly 0.3 due to rounding errors. To avoid such issues, you may need to use more advanced techniques or libraries that support arbitrary-precision arithmetic.


@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

There are three numeric types in Python:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Integer type

    Int, or integer, is a whole number, positive or negative,
    without decimals, of unlimited length.
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """Boolean

    Booleans represent the truth values False and True. The two objects representing the values
    False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
    and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
    exception being that when converted to a string, the strings "False" or "True" are returned,
    respectively.
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """Float type

    Float, or "floating point number" is a number, positive or negative,
    containing one or more decimals.
    """

    float_number = 7.0
    # Another way of declaring float is using float() function.
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Float can also be scientific numbers with an "e" to indicate
    # the power of 10.
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """Complex Type"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """Basic operations"""

    # Addition.
    assert 2 + 4 == 6

    # Multiplication.
    assert 2 * 4 == 8

    # Division always returns a floating point number.
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # Modulo operator returns the remainder of the division.
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # Floor division discards the fractional part.
    assert 17 // 3 == 5

    # Raising the number to specific power.
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7

    # There is full support for floating point; operators with
    # mixed type operands convert the integer operand to floating point.
    assert 4 * 3.75 - 1 == 14.0
