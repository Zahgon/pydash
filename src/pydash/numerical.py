"""
Numerical/mathematical related functions.

.. versionadded:: 2.1.0
"""

from __future__ import annotations

import math
import operator
import typing as t

import pydash as pyd

from .helpers import UNSET, Unset, iterator, iterator_with_default, iteriteratee
from .types import IterateeObjT, NumberNoDecimalT, NumberT, SupportsMul, SupportsRound


if t.TYPE_CHECKING:
    from decimal import Decimal  # pragma: no cover

    from _typeshed import SupportsAdd, SupportsRichComparisonT, SupportsSub  # pragma: no cover


__all__ = (
    "add",
    "ceil",
    "clamp",
    "divide",
    "floor",
    "max_",
    "max_by",
    "mean",
    "mean_by",
    "median",
    "min_",
    "min_by",
    "moving_mean",
    "multiply",
    "power",
    "round_",
    "scale",
    "slope",
    "std_deviation",
    "sum_",
    "sum_by",
    "subtract",
    "transpose",
    "variance",
    "zscore",
)

T = t.TypeVar("T")
T2 = t.TypeVar("T2")
T3 = t.TypeVar("T3")


INFINITY = float("inf")


@t.overload
def add(a: "SupportsAdd[T, T2]", b: T) -> T2: pass


@t.overload
def add(a: T, b: "SupportsAdd[T, T2]") -> T2: pass


def add(a, b):
    """
    Adds two numbers.

    Args:
        a: First number to add.
        b: Second number to add.

    Returns:
        number

    Example:

        >>> add(10, 5)
        15

    .. versionadded:: 2.1.0

    .. versionchanged:: 3.3.0
        Support adding two numbers when passed as positional arguments.

    .. versionchanged:: 4.0.0
        Only support two argument addition.
    """
    pass


@t.overload
def sum_(collection: t.Mapping[t.Any, "SupportsAdd[int, T]"]) -> T: pass


@t.overload
def sum_(collection: t.Iterable["SupportsAdd[int, T]"]) -> T: pass


def sum_(collection):
    """
    Sum each element in `collection`.

    Args:
        collection: Collection to process or first number to add.

    Returns:
        Result of summation.

    Example:

        >>> sum_([1, 2, 3, 4])
        10

    .. versionadded:: 2.1.0

    .. versionchanged:: 3.3.0
        Support adding two numbers when passed as positional arguments.

    .. versionchanged:: 4.0.0
        Move iteratee support to :func:`sum_by`. Move two argument addition to
        :func:`add`.
    """
    pass


@t.overload
def sum_by(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T, t.Dict[T, T2]], "SupportsAdd[int, T3]"],
) -> T3: pass


@t.overload
def sum_by(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], "SupportsAdd[int, T3]"]
) -> T3: pass


@t.overload
def sum_by(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], "SupportsAdd[int, T3]"]
) -> T3: pass


@t.overload
def sum_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], "SupportsAdd[int, T2]"]
) -> T2: pass


@t.overload
def sum_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int], "SupportsAdd[int, T2]"]
) -> T2: pass


@t.overload
def sum_by(collection: t.Iterable[T], iteratee: t.Callable[[T], "SupportsAdd[int, T2]"]) -> T2: pass


@t.overload
def sum_by(collection: t.Mapping[t.Any, "SupportsAdd[int, T]"], iteratee: None = None) -> T: pass


@t.overload
def sum_by(collection: t.Iterable["SupportsAdd[int, T]"], iteratee: None = None) -> T: pass


def sum_by(collection, iteratee=None):
    """
    Sum each element in `collection`. If iteratee is passed, each element of `collection` is passed
    through an iteratee before the summation is computed.

    Args:
        collection: Collection to process or first number to add.
        iteratee: Iteratee applied per iteration or second number to add.

    Returns:
        Result of summation.

    Example:

        >>> sum_by([1, 2, 3, 4], lambda x: x**2)
        30

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def mean(collection: t.Mapping[t.Any, "SupportsAdd[int, t.Any]"]) -> float: pass


@t.overload
def mean(collection: t.Iterable["SupportsAdd[int, t.Any]"]) -> float: pass


def mean(collection):
    """
    Calculate arithmetic mean of each element in `collection`.

    Args:
        collection: Collection to process.

    Returns:
        Result of mean.

    Example:

        >>> mean([1, 2, 3, 4])
        2.5

    .. versionadded:: 2.1.0

    .. versionchanged:: 4.0.0

        - Removed ``average`` and ``avg`` aliases.
        - Moved iteratee functionality to :func:`mean_by`.
    """
    pass


@t.overload
def mean_by(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T, t.Dict[T, T2]], "SupportsAdd[int, t.Any]"],
) -> float: pass


@t.overload
def mean_by(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], "SupportsAdd[int, t.Any]"]
) -> float: pass


@t.overload
def mean_by(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], "SupportsAdd[int, t.Any]"]
) -> float: pass


@t.overload
def mean_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], "SupportsAdd[int, t.Any]"]
) -> float: pass


@t.overload
def mean_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int], "SupportsAdd[int, t.Any]"]
) -> float: pass


@t.overload
def mean_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T], "SupportsAdd[int, t.Any]"]
) -> float: pass


@t.overload
def mean_by(
    collection: t.Mapping[t.Any, "SupportsAdd[int, t.Any]"], iteratee: None = None
) -> float: pass


@t.overload
def mean_by(collection: t.Iterable["SupportsAdd[int, t.Any]"], iteratee: None = None) -> float: pass


def mean_by(collection, iteratee=None):
    """
    Calculate arithmetic mean of each element in `collection`. If iteratee is passed, each element
    of `collection` is passed through an iteratee before the mean is computed.

    Args:
        collection: Collection to process.
        iteratee: Iteratee applied per iteration.

    Returns:
        Result of mean.

    Example:

        >>> mean_by([1, 2, 3, 4], lambda x: x**2)
        7.5

    .. versionadded:: 4.0.0
    """
    pass


def ceil(x: NumberT, precision: int = 0) -> float:
    """
    Round number up to precision.

    Args:
        x: Number to round up.
        precision: Rounding precision. Defaults to ``0``.

    Returns:
        Number rounded up.

    Example:

        >>> ceil(3.275) == 4.0
        True
        >>> ceil(3.215, 1) == 3.3
        True
        >>> ceil(6.004, 2) == 6.01
        True

    .. versionadded:: 3.3.0
    """
    pass


NumT = t.TypeVar("NumT", int, float, "Decimal")
NumT2 = t.TypeVar("NumT2", int, float, "Decimal")
NumT3 = t.TypeVar("NumT3", int, float, "Decimal")


def clamp(x: NumT, lower: NumT2, upper: t.Union[NumT3, None] = None) -> t.Union[NumT, NumT2, NumT3]:
    """
    Clamps number within the inclusive lower and upper bounds.

    Args:
        x: Number to clamp.
        lower: Lower bound.
        upper: Upper bound

    Returns:
        number

    Example:

        >>> clamp(-10, -5, 5)
        -5
        >>> clamp(10, -5, 5)
        5
        >>> clamp(10, 5)
        5
        >>> clamp(-10, 5)
        -10

    .. versionadded:: 4.0.0
    """
    pass


def divide(dividend: t.Union[NumberT, None], divisor: t.Union[NumberT, None]) -> float:
    """
    Divide two numbers.

    Args:
        dividend: The first number in a division.
        divisor: The second number in a division.

    Returns:
        Returns the quotient.

    Example:

        >>> divide(20, 5)
        4.0
        >>> divide(1.5, 3)
        0.5
        >>> divide(None, None)
        1.0
        >>> divide(5, None)
        5.0

    .. versionadded:: 4.0.0
    """
    pass


def floor(x: NumberT, precision: int = 0) -> float:
    """
    Round number down to precision.

    Args:
        x: Number to round down.
        precision: Rounding precision. Defaults to ``0``.

    Returns:
        Number rounded down.

    Example:

        >>> floor(3.75) == 3.0
        True
        >>> floor(3.215, 1) == 3.2
        True
        >>> floor(0.046, 2) == 0.04
        True

    .. versionadded:: 3.3.0
    """
    pass


@t.overload
def max_(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def max_(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def max_(
    collection: t.Iterable["SupportsRichComparisonT"], default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def max_(
    collection: t.Iterable["SupportsRichComparisonT"], default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


def max_(collection, default=UNSET):
    """
    Retrieves the maximum value of a `collection`.

    Args:
        collection: Collection to iterate over.
        default: Value to return if `collection` is empty.

    Returns:
        Maximum value.

    Example:

        >>> max_([1, 2, 3, 4])
        4
        >>> max_([], default=-1)
        -1

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Moved iteratee iteratee support to :func:`max_by`.
    """
    pass


@t.overload
def max_by(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"],
    iteratee: None = None,
    default: Unset = UNSET,
) -> "SupportsRichComparisonT": pass


@t.overload
def max_by(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    default: Unset = UNSET,
) -> T2: pass


@t.overload
def max_by(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    *,
    default: T,
) -> t.Union[T2, T]: pass


@t.overload
def max_by(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], iteratee: None = None, *, default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def max_by(
    collection: t.Iterable["SupportsRichComparisonT"], iteratee: None = None, default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def max_by(
    collection: t.Iterable[T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    default: Unset = UNSET,
) -> T2: pass


@t.overload
def max_by(
    collection: t.Iterable[T2], iteratee: t.Callable[[T2], "SupportsRichComparisonT"], *, default: T
) -> t.Union[T2, T]: pass


@t.overload
def max_by(
    collection: t.Iterable["SupportsRichComparisonT"], iteratee: None = None, *, default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def max_by(collection: t.Iterable[T], iteratee: IterateeObjT, default: Unset = UNSET) -> T: pass


@t.overload
def max_by(collection: t.Iterable[T], iteratee: IterateeObjT, default: T2) -> t.Union[T, T2]: pass


def max_by(collection, iteratee=None, default=UNSET):
    """
    Retrieves the maximum value of a `collection`.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        default: Value to return if `collection` is empty.

    Returns:
        Maximum value.

    Example:

        >>> max_by([1.0, 1.5, 1.8], math.floor)
        1.0
        >>> max_by([{"a": 1}, {"a": 2}, {"a": 3}], "a")
        {'a': 3}
        >>> max_by([], default=-1)
        -1

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def median(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(
    collection: t.Iterable[T], iteratee: t.Callable[[T], NumberT]
) -> t.Union[float, int]: pass


@t.overload
def median(collection: t.Iterable[NumberT], iteratee: None = None) -> t.Union[float, int]: pass


def median(collection, iteratee=None):
    """
    Calculate median of each element in `collection`. If iteratee is passed, each element of
    `collection` is passed through an iteratee before the median is computed.

    Args:
        collection: Collection to process.
        iteratee: Iteratee applied per iteration.

    Returns:
        Result of median.

    Example:

        >>> median([1, 2, 3, 4, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5

    .. versionadded:: 2.1.0
    """
    pass


@t.overload
def min_(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def min_(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def min_(
    collection: t.Iterable["SupportsRichComparisonT"], default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def min_(
    collection: t.Iterable["SupportsRichComparisonT"], default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


def min_(collection, default=UNSET):
    """
    Retrieves the minimum value of a `collection`.

    Args:
        collection: Collection to iterate over.
        default: Value to return if `collection` is empty.

    Returns:
        Minimum value.

    Example:

        >>> min_([1, 2, 3, 4])
        1
        >>> min_([], default=100)
        100

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Moved iteratee iteratee support to :func:`min_by`.
    """
    pass


@t.overload
def min_by(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"],
    iteratee: None = None,
    default: Unset = UNSET,
) -> "SupportsRichComparisonT": pass


@t.overload
def min_by(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    default: Unset = UNSET,
) -> T2: pass


@t.overload
def min_by(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    *,
    default: T,
) -> t.Union[T2, T]: pass


@t.overload
def min_by(
    collection: t.Mapping[t.Any, "SupportsRichComparisonT"], iteratee: None = None, *, default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def min_by(
    collection: t.Iterable["SupportsRichComparisonT"], iteratee: None = None, default: Unset = UNSET
) -> "SupportsRichComparisonT": pass


@t.overload
def min_by(
    collection: t.Iterable[T2],
    iteratee: t.Callable[[T2], "SupportsRichComparisonT"],
    default: Unset = UNSET,
) -> T2: pass


@t.overload
def min_by(
    collection: t.Iterable[T2], iteratee: t.Callable[[T2], "SupportsRichComparisonT"], *, default: T
) -> t.Union[T2, T]: pass


@t.overload
def min_by(
    collection: t.Iterable["SupportsRichComparisonT"], iteratee: None = None, *, default: T
) -> t.Union["SupportsRichComparisonT", T]: pass


@t.overload
def min_by(collection: t.Iterable[T], iteratee: IterateeObjT, default: Unset = UNSET) -> T: pass


@t.overload
def min_by(collection: t.Iterable[T], iteratee: IterateeObjT, default: T2) -> t.Union[T, T2]: pass


def min_by(collection, iteratee=None, default=UNSET):
    """
    Retrieves the minimum value of a `collection`.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        default: Value to return if `collection` is empty.

    Returns:
        Minimum value.

    Example:

        >>> min_by([1.8, 1.5, 1.0], math.floor)
        1.8
        >>> min_by([{"a": 1}, {"a": 2}, {"a": 3}], "a")
        {'a': 1}
        >>> min_by([], default=100)
        100

    .. versionadded:: 4.0.0
    """
    pass


def moving_mean(array: t.Sequence["SupportsAdd[int, t.Any]"], size: t.SupportsInt) -> t.List[float]:
    """
    Calculate moving mean of each element of `array`.

    Args:
        array: List to process.
        size: Window size.

    Returns:
        Result of moving average.

    Example:

        >>> moving_mean(range(10), 1)
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        >>> moving_mean(range(10), 5)
        [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
        >>> moving_mean(range(10), 10)
        [4.5]

    .. versionadded:: 2.1.0

    .. versionchanged:: 4.0.0
        Rename to ``moving_mean`` and remove ``moving_average`` and ``moving_avg`` aliases.
    """
    pass


@t.overload
def multiply(multiplier: SupportsMul[int, T2], multiplicand: None) -> T2: pass


@t.overload
def multiply(multiplier: None, multiplicand: SupportsMul[int, T2]) -> T2: pass


@t.overload
def multiply(multiplier: None, multiplicand: None) -> int: pass


@t.overload
def multiply(multiplier: SupportsMul[T, T2], multiplicand: T) -> T2: pass


@t.overload
def multiply(multiplier: T, multiplicand: SupportsMul[T, T2]) -> T2: pass


def multiply(multiplier, multiplicand):
    """
    Multiply two numbers.

    Args:
        multiplier: The first number in a multiplication.
        multiplicand: The second number in a multiplication.

    Returns:
        Returns the product.

    Example:

        >>> multiply(4, 5)
        20
        >>> multiply(10, 4)
        40
        >>> multiply(None, 10)
        10
        >>> multiply(None, None)
        1

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def power(x: int, n: int) -> t.Union[int, float]: pass


@t.overload
def power(x: float, n: t.Union[int, float]) -> float: pass


@t.overload
def power(x: t.List[int], n: int) -> t.List[t.Union[int, float]]: pass


@t.overload
def power(x: t.List[float], n: t.List[t.Union[int, float]]) -> t.List[float]: pass


def power(x, n):
    """
    Calculate exponentiation of `x` raised to the `n` power.

    Args:
        x: Base number.
        n: Exponent.

    Returns:
        Result of calculation.

    Example:

        >>> power(5, 2)
        25
        >>> power(12.5, 3)
        1953.125

    .. versionadded:: 2.1.0

    .. versionchanged:: 4.0.0
        Removed alias ``pow_``.
    """
    pass


@t.overload
def round_(x: t.List[SupportsRound[NumberT]], precision: int = 0) -> t.List[float]: pass


@t.overload
def round_(x: SupportsRound[NumberT], precision: int = 0) -> float: pass


def round_(x, precision=0):
    """
    Round number to precision.

    Args:
        x: Number to round.
        precision: Rounding precision. Defaults to ``0``.

    Returns:
        Rounded number.

    Example:

        >>> round_(3.275) == 3.0
        True
        >>> round_(3.275, 1) == 3.3
        True

    .. versionadded:: 2.1.0

    .. versionchanged:: 4.0.0
        Remove alias ``curve``.
    """
    pass


@t.overload
def scale(array: t.Iterable["Decimal"], maximum: "Decimal") -> t.List["Decimal"]: pass


@t.overload
def scale(array: t.Iterable[NumberNoDecimalT], maximum: NumberNoDecimalT) -> t.List[float]: pass


@t.overload
def scale(array: t.Iterable[NumberT], maximum: int = 1) -> t.List[float]: pass


def scale(array, maximum: NumberT = 1):
    """
    Scale list of value to a maximum number.

    Args:
        array: Numbers to scale.
        maximum: Maximum scale value.

    Returns:
        Scaled numbers.

    Example:

        >>> scale([1, 2, 3, 4])
        [0.25, 0.5, 0.75, 1.0]
        >>> scale([1, 2, 3, 4], 1)
        [0.25, 0.5, 0.75, 1.0]
        >>> scale([1, 2, 3, 4], 4)
        [1.0, 2.0, 3.0, 4.0]
        >>> scale([1, 2, 3, 4], 2)
        [0.5, 1.0, 1.5, 2.0]

    .. versionadded:: 2.1.0
    """
    pass


@t.overload
def slope(
    point1: t.Union[t.Tuple["Decimal", "Decimal"], t.List["Decimal"]],
    point2: t.Union[t.Tuple["Decimal", "Decimal"], t.List["Decimal"]],
) -> "Decimal": pass


@t.overload
def slope(
    point1: t.Union[t.Tuple[NumberNoDecimalT, NumberNoDecimalT], t.List[NumberNoDecimalT]],
    point2: t.Union[t.Tuple[NumberNoDecimalT, NumberNoDecimalT], t.List[NumberNoDecimalT]],
) -> float: pass


def slope(point1, point2):
    """
    Calculate the slope between two points.

    Args:
        point1: X and Y coordinates of first point.
        point2: X and Y cooredinates of second point.

    Returns:
        Calculated slope.

    Example:

        >>> slope((1, 2), (4, 8))
        2.0

    .. versionadded:: 2.1.0
    """
    pass


def std_deviation(array: t.List[NumberT]) -> float:
    """
    Calculate standard deviation of list of numbers.

    Args:
        array: List to process.

    Returns:
        Calculated standard deviation.

    Example:

        >>> round(std_deviation([1, 18, 20, 4]), 2) == 8.35
        True

    .. versionadded:: 2.1.0

    .. versionchanged:: 4.0.0
        Remove alias ``sigma``.
    """
    pass


@t.overload
def subtract(minuend: "SupportsSub[T, T2]", subtrahend: T) -> T2: pass


@t.overload
def subtract(minuend: T, subtrahend: "SupportsSub[T, T2]") -> T2: pass


def subtract(minuend, subtrahend):
    """
    Subtracts two numbers.

    Args:
        minuend: Value passed in by the user.
        subtrahend: Value passed in by the user.

    Returns:
        Result of the difference from the given values.

    Example:

        >>> subtract(10, 5)
        5
        >>> subtract(-10, 4)
        -14
        >>> subtract(2, 0.5)
        1.5

    .. versionadded:: 4.0.0
    """
    pass


def transpose(array: t.Iterable[t.Iterable[T]]) -> t.List[t.List[T]]:
    """
    Transpose the elements of `array`.

    Args:
        array: List to process.

    Returns:
        Transposed list.

    Example:

        >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    .. versionadded:: 2.1.0
    """
    pass


@t.overload
def variance(array: t.Mapping[t.Any, "SupportsAdd[int, t.Any]"]) -> float: pass


@t.overload
def variance(array: t.Iterable["SupportsAdd[int, t.Any]"]) -> float: pass


def variance(array):
    """
    Calculate the variance of the elements in `array`.

    Args:
        array: List to process.

    Returns:
        Calculated variance.

    Example:

        >>> variance([1, 18, 20, 4])
        69.6875

    .. versionadded:: 2.1.0
    """
    pass


@t.overload
def zscore(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], NumberT]
) -> t.List[float]: pass


@t.overload
def zscore(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], NumberT]
) -> t.List[float]: pass


@t.overload
def zscore(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], NumberT]
) -> t.List[float]: pass


@t.overload
def zscore(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], NumberT]
) -> t.List[float]: pass


@t.overload
def zscore(collection: t.Iterable[T], iteratee: t.Callable[[T, int], NumberT]) -> t.List[float]: pass


@t.overload
def zscore(collection: t.Iterable[T], iteratee: t.Callable[[T], NumberT]) -> t.List[float]: pass


@t.overload
def zscore(collection: t.Iterable[NumberT], iteratee: None = None) -> t.List[float]: pass


def zscore(collection, iteratee=None):
    """
    Calculate the standard score assuming normal distribution. If iteratee is passed, each element
    of `collection` is passed through an iteratee before the standard score is computed.

    Args:
        collection: Collection to process.
        iteratee: Iteratee applied per iteration.

    Returns:
        Calculated standard score.

    Example:

        >>> results = zscore([1, 2, 3])

        # [-1.224744871391589, 0.0, 1.224744871391589]

    .. versionadded:: 2.1.0
    """
    pass


#
# Utility methods not a part of the main API
#


def call_math_operator(value1, value2, op, default):
    """Return the result of the math operation on the given values."""
    pass


def rounder(func, x, precision):
    pass
