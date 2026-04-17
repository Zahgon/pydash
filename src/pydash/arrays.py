"""
Functions that operate on lists.

.. versionadded:: 1.0.0
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from math import ceil
import typing as t

import pydash as pyd

from .helpers import base_get, iteriteratee, parse_iteratee
from .types import IterateeObjT


if t.TYPE_CHECKING:
    from _typeshed import SupportsRichComparisonT  # pragma: no cover


__all__ = (
    "chunk",
    "compact",
    "concat",
    "difference",
    "difference_by",
    "difference_with",
    "drop",
    "drop_right",
    "drop_right_while",
    "drop_while",
    "duplicates",
    "fill",
    "find_index",
    "find_last_index",
    "flatten",
    "flatten_deep",
    "flatten_depth",
    "from_pairs",
    "head",
    "index_of",
    "initial",
    "intercalate",
    "interleave",
    "intersection",
    "intersection_by",
    "intersection_with",
    "intersperse",
    "last",
    "last_index_of",
    "mapcat",
    "nth",
    "pull",
    "pull_all",
    "pull_all_by",
    "pull_all_with",
    "pull_at",
    "push",
    "remove",
    "reverse",
    "shift",
    "slice_",
    "sort",
    "sorted_index",
    "sorted_index_by",
    "sorted_index_of",
    "sorted_last_index",
    "sorted_last_index_by",
    "sorted_last_index_of",
    "sorted_uniq",
    "sorted_uniq_by",
    "splice",
    "split_at",
    "tail",
    "take",
    "take_right",
    "take_right_while",
    "take_while",
    "union",
    "union_by",
    "union_with",
    "uniq",
    "uniq_by",
    "uniq_with",
    "unshift",
    "unzip",
    "unzip_with",
    "without",
    "xor",
    "xor_by",
    "xor_with",
    "zip_",
    "zip_object",
    "zip_object_deep",
    "zip_with",
)

T = t.TypeVar("T")
T2 = t.TypeVar("T2")
T3 = t.TypeVar("T3")
T4 = t.TypeVar("T4")
T5 = t.TypeVar("T5")
SequenceT = t.TypeVar("SequenceT", bound=t.Sequence[t.Any])
MutableSequenceT = t.TypeVar("MutableSequenceT", bound=t.MutableSequence[t.Any])


def chunk(array: t.Sequence[T], size: int = 1) -> t.List[t.Sequence[T]]:
    """
    Creates a list of elements split into groups the length of `size`. If `array` can't be split
    evenly, the final chunk will be the remaining elements.

    Args:
        array: List to chunk.
        size: Chunk size. Defaults to ``1``.

    Returns:
        New list containing chunks of `array`.

    Example:

        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]

    .. versionadded:: 1.1.0
    """
    pass


def compact(array: t.Iterable[t.Union[T, None]]) -> t.List[T]:
    """
    Creates a list with all falsey values of array removed.

    Args:
        array: List to compact.

    Returns:
        Compacted list.

    Example:

        >>> compact(["", 1, 0, True, False, None])
        [1, True]

    .. versionadded:: 1.0.0
    """
    pass


def concat(*arrays: t.Iterable[T]) -> t.List[T]:
    """
    Concatenates zero or more lists into one.

    Args:
        arrays: Lists to concatenate.

    Returns:
        Concatenated list.

    Example:

        >>> concat([1, 2], [3, 4], [[5], [6]])
        [1, 2, 3, 4, [5], [6]]

    .. versionadded:: 2.0.0

    .. versionchanged:: 4.0.0
        Renamed from ``cat`` to ``concat``.
    """
    pass


def difference(array: t.Iterable[T], *others: t.Iterable[T]) -> t.List[T]:
    """
    Creates a list of list elements not present in others.

    Args:
        array: List to process.
        others: Lists to check.

    Returns:
        Difference between `others`.

    Example:

        >>> difference([1, 2, 3], [1], [2])
        [3]

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def difference_by(
    array: t.Iterable[T],
    *others: t.Iterable[T],
    iteratee: t.Union[IterateeObjT, t.Callable[[T], t.Any], None],
) -> t.List[T]: pass


@t.overload
def difference_by(
    array: t.Iterable[T], *others: t.Union[IterateeObjT, t.Iterable[T], t.Callable[[T], t.Any]]
) -> t.List[T]: pass


def difference_by(array, *others, **kwargs):
    """
    This method is like :func:`difference` except that it accepts an iteratee which is invoked for
    each element of each array to generate the criterion by which they're compared. The order and
    references of result values are determined by `array`. The iteratee is invoked with one
    argument: ``(value)``.

    Args:
        array: The array to find the difference of.
        others: Lists to check for difference with `array`.

    Keyword Args:
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        Difference between `others`.

    Example:

        >>> difference_by([1.2, 1.5, 1.7, 2.8], [0.9, 3.2], round)
        [1.5, 1.7]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def difference_with(
    array: t.Iterable[T],
    *others: t.Iterable[T2],
    comparator: t.Union[t.Callable[[T, T2], t.Any], None],
) -> t.List[T]: pass


@t.overload
def difference_with(
    array: t.Iterable[T], *others: t.Union[t.Iterable[T2], t.Callable[[T, T2], t.Any]]
) -> t.List[T]: pass


def difference_with(array, *others, **kwargs):
    """
    This method is like :func:`difference` except that it accepts a comparator which is invoked to
    compare the elements of all arrays. The order and references of result values are determined by
    the first array. The comparator is invoked with two arguments: ``(arr_val, oth_val)``.

    Args:
        array: The array to find the difference of.
        others: Lists to check for difference with `array`.

    Keyword Args:
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        Difference between `others`.

    Example:

        >>> array = ["apple", "banana", "pear"]
        >>> others = (["avocado", "pumpkin"], ["peach"])
        >>> comparator = lambda a, b: a[0] == b[0]
        >>> difference_with(array, *others, comparator=comparator)
        ['banana']

    .. versionadded:: 4.0.0
    """
    pass


def drop(array: t.Sequence[T], n: int = 1) -> t.List[T]:
    """
    Creates a slice of `array` with `n` elements dropped from the beginning.

    Args:
        array: List to process.
        n: Number of elements to drop. Defaults to ``1``.

    Returns:
        Dropped list.

    Example:

        >>> drop([1, 2, 3, 4], 2)
        [3, 4]

    .. versionadded:: 1.0.0

    .. versionchanged:: 1.1.0
        Added ``n`` argument and removed as alias of :func:`rest`.

    .. versionchanged:: 3.0.0
        Made ``n`` default to ``1``.
    """
    pass


def drop_right(array: t.Sequence[T], n: int = 1) -> t.List[T]:
    """
    Creates a slice of `array` with `n` elements dropped from the end.

    Args:
        array: List to process.
        n: Number of elements to drop. Defaults to ``1``.

    Returns:
        Dropped list.

    Example:

        >>> drop_right([1, 2, 3, 4], 2)
        [1, 2]

    .. versionadded:: 1.1.0

    .. versionchanged:: 3.0.0
        Made ``n`` default to ``1``.
    """
    pass


@t.overload
def drop_right_while(
    array: t.Sequence[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> t.List[T]: pass


@t.overload
def drop_right_while(array: t.Sequence[T], predicate: t.Callable[[T, int], t.Any]) -> t.List[T]: pass


@t.overload
def drop_right_while(array: t.Sequence[T], predicate: t.Callable[[T], t.Any]) -> t.List[T]: pass


@t.overload
def drop_right_while(array: t.Sequence[T], predicate: None = None) -> t.List[T]: pass


def drop_right_while(array, predicate=None):
    """
    Creates a slice of `array` excluding elements dropped from the end. Elements are dropped until
    the `predicate` returns falsey. The `predicate` is invoked with three arguments: ``(value,
    index, array)``.

    Args:
        array: List to process.
        predicate: Predicate called per iteration

    Returns:
        Dropped list.

    Example:

        >>> drop_right_while([1, 2, 3, 4], lambda x: x >= 3)
        [1, 2]

    .. versionadded:: 1.1.0
    """
    pass


@t.overload
def drop_while(
    array: t.Sequence[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> t.List[T]: pass


@t.overload
def drop_while(array: t.Sequence[T], predicate: t.Callable[[T, int], t.Any]) -> t.List[T]: pass


@t.overload
def drop_while(array: t.Sequence[T], predicate: t.Callable[[T], t.Any]) -> t.List[T]: pass


@t.overload
def drop_while(array: t.Sequence[T], predicate: None = None) -> t.List[T]: pass


def drop_while(array, predicate=None):
    """
    Creates a slice of `array` excluding elements dropped from the beginning. Elements are dropped
    until the `predicate` returns falsey. The `predicate` is invoked with three arguments: ``(value,
    index, array)``.

    Args:
        array: List to process.
        predicate: Predicate called per iteration

    Returns:
        Dropped list.

    Example:

        >>> drop_while([1, 2, 3, 4], lambda x: x < 3)
        [3, 4]

    .. versionadded:: 1.1.0
    """
    pass


def duplicates(
    array: t.Sequence[T], iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None
) -> t.List[T]:
    """
    Creates a unique list of duplicate values from `array`. If iteratee is passed, each element of
    array is passed through an iteratee before duplicates are computed. The iteratee is invoked with
    three arguments: ``(value, index, array)``. If an object path is passed for iteratee, the
    created iteratee will return the path value of the given element. If an object is passed for
    iteratee, the created filter style iteratee will return ``True`` for elements that have the
    properties of the given object, else ``False``.

    Args:
        array: List to process.
        iteratee: Iteratee applied per iteration.

    Returns:
        List of duplicates.

    Example:

        >>> duplicates([0, 1, 3, 2, 3, 1])
        [3, 1]

    .. versionadded:: 3.0.0
    """
    pass


def fill(
    array: t.Sequence[T], value: T2, start: int = 0, end: t.Union[int, None] = None
) -> t.List[t.Union[T, T2]]:
    """
    Fills elements of array with value from `start` up to, but not including, `end`.

    Args:
        array: List to fill.
        value: Value to fill with.
        start: Index to start filling. Defaults to ``0``.
        end: Index to end filling. Defaults to ``len(array)``.

    Returns:
        Filled `array`.

    Example:

        >>> fill([1, 2, 3, 4, 5], 0)
        [0, 0, 0, 0, 0]
        >>> fill([1, 2, 3, 4, 5], 0, 1, 3)
        [1, 0, 0, 4, 5]
        >>> fill([1, 2, 3, 4, 5], 0, 0, 100)
        [0, 0, 0, 0, 0]

    Warning:
        `array` is modified in place.

    .. versionadded:: 3.1.0
    """
    pass


@t.overload
def find_index(array: t.Iterable[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]) -> int: pass


@t.overload
def find_index(array: t.Iterable[T], predicate: t.Callable[[T, int], t.Any]) -> int: pass


@t.overload
def find_index(array: t.Iterable[T], predicate: t.Callable[[T], t.Any]) -> int: pass


@t.overload
def find_index(array: t.Iterable[t.Any], predicate: IterateeObjT) -> int: pass


@t.overload
def find_index(array: t.Iterable[t.Any], predicate: None = None) -> int: pass


def find_index(array, predicate=None):
    """
    This method is similar to :func:`pydash.collections.find`, except that it returns the index of
    the element that passes the predicate check, instead of the element itself.

    Args:
        array: List to process.
        predicate: Predicate applied per iteration.

    Returns:
        Index of found item or ``-1`` if not found.

    Example:

        >>> find_index([1, 2, 3, 4], lambda x: x >= 3)
        2
        >>> find_index([1, 2, 3, 4], lambda x: x > 4)
        -1

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def find_last_index(
    array: t.Iterable[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> int: pass


@t.overload
def find_last_index(array: t.Iterable[T], predicate: t.Callable[[T, int], t.Any]) -> int: pass


@t.overload
def find_last_index(array: t.Iterable[T], predicate: t.Callable[[T], t.Any]) -> int: pass


@t.overload
def find_last_index(array: t.Iterable[t.Any], predicate: IterateeObjT) -> int: pass


@t.overload
def find_last_index(array: t.Iterable[t.Any], predicate: None = None) -> int: pass


def find_last_index(array, predicate=None):
    """
    This method is similar to :func:`find_index`, except that it iterates over elements from right
    to left.

    Args:
        array: List to process.
        predicate: Predicate applied per iteration.

    Returns:
        Index of found item or ``-1`` if not found.

    Example:

        >>> find_last_index([1, 2, 3, 4], lambda x: x >= 3)
        3
        >>> find_last_index([1, 2, 3, 4], lambda x: x > 4)
        -1

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def flatten(array: t.Iterable[t.Iterable[T]]) -> t.List[T]: pass


@t.overload
def flatten(array: t.Iterable[T]) -> t.List[T]: pass


def flatten(array):
    """
    Flattens array a single level deep.

    Args:
        array: List to flatten.

    Returns:
        Flattened list.

    Example:

        >>> flatten([[1], [2, [3]], [[4]]])
        [1, 2, [3], [4]]


    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0
        Removed `callback` option. Added ``is_deep`` option. Made it shallow
        by default.

    .. versionchanged:: 4.0.0
        Removed ``is_deep`` option. Use :func:`flatten_deep` instead.
    """
    pass


def flatten_deep(array: t.Iterable[t.Any]) -> t.List[t.Any]:
    """
    Flattens an array recursively.

    Args:
        array: List to flatten.

    Returns:
        Flattened list.

    Example:

        >>> flatten_deep([[1], [2, [3]], [[4]]])
        [1, 2, 3, 4]

    .. versionadded:: 2.0.0
    """
    pass


def flatten_depth(array: t.Iterable[t.Any], depth: int = 1) -> t.List[t.Any]:
    """
    Recursively flatten `array` up to `depth` times.

    Args:
        array: List to flatten.
        depth: Depth to flatten to. Defaults to ``1``.

    Returns:
        Flattened list.

    Example:

        >>> flatten_depth([[[1], [2, [3]], [[4]]]], 1)
        [[1], [2, [3]], [[4]]]
        >>> flatten_depth([[[1], [2, [3]], [[4]]]], 2)
        [1, 2, [3], [4]]
        >>> flatten_depth([[[1], [2, [3]], [[4]]]], 3)
        [1, 2, 3, 4]
        >>> flatten_depth([[[1], [2, [3]], [[4]]]], 4)
        [1, 2, 3, 4]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def from_pairs(pairs: t.Iterable[t.Tuple[T, T2]]) -> t.Dict[T, T2]: pass


@t.overload
def from_pairs(
    pairs: t.Iterable[t.List[t.Union[T, T2]]],
) -> t.Dict[t.Union[T, T2], t.Union[T, T2]]: pass


def from_pairs(pairs):
    """
    Returns a dict from the given list of pairs.

    Args:
        pairs: List of key-value pairs.

    Returns:
        dict

    Example:

        >>> from_pairs([["a", 1], ["b", 2]]) == {"a": 1, "b": 2}
        True

    .. versionadded:: 4.0.0
    """
    pass


def head(array: t.Sequence[T]) -> t.Union[T, None]:
    """
    Return the first element of `array`.

    Args:
        array: List to process.

    Returns:
        First element of list.

    Example:

        >>> head([1, 2, 3, 4])
        1

    .. versionadded:: 1.0.0

    .. versionchanged::
        Renamed from ``first`` to ``head``.
    """
    pass


def index_of(array: t.Sequence[T], value: T, from_index: int = 0) -> int:
    """
    Gets the index at which the first occurrence of value is found.

    Args:
        array: List to search.
        value: Value to search for.
        from_index: Index to search from.

    Returns:
        Index of found item or ``-1`` if not found.

    Example:

        >>> index_of([1, 2, 3, 4], 2)
        1
        >>> index_of([2, 1, 2, 3], 2, from_index=1)
        2

    .. versionadded:: 1.0.0
    """
    pass


def initial(array: t.Sequence[T]) -> t.Sequence[T]:
    """
    Return all but the last element of `array`.

    Args:
        array: List to process.

    Returns:
        Initial part of `array`.

    Example:

        >>> initial([1, 2, 3, 4])
        [1, 2, 3]

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def intercalate(array: t.Iterable[t.Iterable[T]], separator: T2) -> t.List[t.Union[T, T2]]: pass


@t.overload
def intercalate(array: t.Iterable[T], separator: T2) -> t.List[t.Union[T, T2]]: pass


def intercalate(array, separator):
    """
    Like :func:`intersperse` for lists of lists but shallowly flattening the result.

    Args:
        array: List to intercalate.
        separator: Element to insert.

    Returns:
        Intercalated list.

    Example:

        >>> intercalate([1, [2], [3], 4], "x")
        [1, 'x', 2, 'x', 3, 'x', 4]


    .. versionadded:: 2.0.0
    """
    pass


def interleave(*arrays: t.Iterable[T]) -> t.List[T]:
    """
    Merge multiple lists into a single list by inserting the next element of each list by sequential
    round-robin into the new list.

    Args:
        arrays: Lists to interleave.

    Returns:
        Interleaved list.

    Example:

        >>> interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])
        [1, 4, 7, 2, 5, 8, 3, 6, 9]

    .. versionadded:: 2.0.0
    """
    pass


def intersection(array: t.Sequence[T], *others: t.Iterable[t.Any]) -> t.List[T]:
    """
    Computes the intersection of all the passed-in arrays.

    Args:
        array: The array to find the intersection of.
        others: Lists to check for intersection with `array`.

    Returns:
        Intersection of provided lists.

    Example:

        >>> intersection([1, 2, 3], [1, 2, 3, 4, 5], [2, 3])
        [2, 3]

        >>> intersection([1, 2, 3])
        [1, 2, 3]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Support finding intersection of unhashable types.
    """
    pass


@t.overload
def intersection_by(
    array: t.Sequence[T],
    *others: t.Iterable[t.Any],
    iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT],
) -> t.List[T]: pass


@t.overload
def intersection_by(
    array: t.Sequence[T], *others: t.Union[t.Iterable[t.Any], t.Callable[[T], t.Any], IterateeObjT]
) -> t.List[T]: pass


def intersection_by(array, *others, **kwargs):
    """
    This method is like :func:`intersection` except that it accepts an iteratee which is invoked for
    each element of each array to generate the criterion by which they're compared. The order and
    references of result values are determined by `array`. The iteratee is invoked with one
    argument: ``(value)``.

    Args:
        array: The array to find the intersection of.
        others: Lists to check for intersection with `array`.

    Keyword Args:
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        Intersection of provided lists.

    Example:

        >>> intersection_by([1.2, 1.5, 1.7, 2.8], [0.9, 3.2], round)
        [1.2, 2.8]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def intersection_with(
    array: t.Sequence[T], *others: t.Iterable[T2], comparator: t.Callable[[T, T2], t.Any]
) -> t.List[T]: pass


@t.overload
def intersection_with(
    array: t.Sequence[T], *others: t.Union[t.Iterable[T2], t.Callable[[T, T2], t.Any]]
) -> t.List[T]: pass


def intersection_with(array, *others, **kwargs):
    """
    This method is like :func:`intersection` except that it accepts a comparator which is invoked to
    compare the elements of all arrays. The order and references of result values are determined by
    the first array. The comparator is invoked with two arguments: ``(arr_val, oth_val)``.

    Args:
        array: The array to find the intersection of.
        others: Lists to check for intersection with `array`.

    Keyword Args:
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        Intersection of provided lists.

    Example:

        >>> array = ["apple", "banana", "pear"]
        >>> others = (["avocado", "pumpkin"], ["peach"])
        >>> comparator = lambda a, b: a[0] == b[0]
        >>> intersection_with(array, *others, comparator=comparator)
        ['pear']

    .. versionadded:: 4.0.0
    """
    pass


def intersperse(array: t.Iterable[T], separator: T2) -> t.List[t.Union[T, T2]]:
    """
    Insert a separating element between the elements of `array`.

    Args:
        array: List to intersperse.
        separator: Element to insert.

    Returns:
        Interspersed list.

    Example:

        >>> intersperse([1, [2], [3], 4], "x")
        [1, 'x', [2], 'x', [3], 'x', 4]

    .. versionadded:: 2.0.0
    """
    pass


def last(array: t.Sequence[T]) -> t.Union[T, None]:
    """
    Return the last element of `array`.

    Args:
        array: List to process.

    Returns:
        Last part of `array`.

    Example:

        >>> last([1, 2, 3, 4])
        4

    .. versionadded:: 1.0.0
    """
    pass


def last_index_of(
    array: t.Sequence[t.Any], value: t.Any, from_index: t.Union[int, None] = None
) -> int:
    """
    Gets the index at which the last occurrence of value is found.

    Args:
        array: List to search.
        value: Value to search for.
        from_index: Index to search from.

    Returns:
        Index of found item or ``-1`` if not found.

    Example:

        >>> last_index_of([1, 2, 2, 4], 2)
        2
        >>> last_index_of([1, 2, 2, 4], 2, from_index=1)
        1

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def mapcat(
    array: t.Iterable[T],
    iteratee: t.Callable[[T, int, t.List[T]], t.Union[t.List[T2], t.List[t.List[T2]]]],
) -> t.List[T2]: pass


@t.overload
def mapcat(array: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], T2]) -> t.List[T2]: pass


@t.overload
def mapcat(
    array: t.Iterable[T], iteratee: t.Callable[[T, int], t.Union[t.List[T2], t.List[t.List[T2]]]]
) -> t.List[T2]: pass


@t.overload
def mapcat(array: t.Iterable[T], iteratee: t.Callable[[T, int], T2]) -> t.List[T2]: pass


@t.overload
def mapcat(
    array: t.Iterable[T], iteratee: t.Callable[[T], t.Union[t.List[T2], t.List[t.List[T2]]]]
) -> t.List[T2]: pass


@t.overload
def mapcat(array: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.List[T2]: pass


@t.overload
def mapcat(
    array: t.Iterable[t.Union[t.List[T], t.List[t.List[T]]]], iteratee: None = None
) -> t.List[t.Union[T, t.List[T]]]: pass


def mapcat(array, iteratee=None):
    """
    Map an iteratee to each element of a list and concatenate the results into a single list using
    :func:`concat`.

    Args:
        array: List to map and concatenate.
        iteratee: Iteratee to apply to each element.

    Returns:
        Mapped and concatenated list.

    Example:

        >>> mapcat(range(4), lambda x: list(range(x)))
        [0, 0, 1, 0, 1, 2]

    .. versionadded:: 2.0.0
    """
    pass


def nth(array: t.Iterable[T], pos: int = 0) -> t.Union[T, None]:
    """
    Gets the element at index n of array.

    Args:
        array: List passed in by the user.
        pos: Index of element to return.

    Returns:
        Returns the element at :attr:`pos`.

    Example:

        >>> nth([1, 2, 3], 0)
        1
        >>> nth([3, 4, 5, 6], 2)
        5
        >>> nth([11, 22, 33], -1)
        33
        >>> nth([11, 22, 33])
        11

    .. versionadded:: 4.0.0
    """
    pass


def pop(array: t.List[T], index: int = -1) -> T:
    """
    Remove element of array at `index` and return element.

    Args:
        array: List to pop from.
        index: Index to remove element from. Defaults to ``-1``.

    Returns:
        Value at `index`.

    Warning:
        `array` is modified in place.

    Example:

        >>> array = [1, 2, 3, 4]
        >>> item = pop(array)
        >>> item
        4
        >>> array
        [1, 2, 3]
        >>> item = pop(array, index=0)
        >>> item
        1
        >>> array
        [2, 3]

    .. versionadded:: 2.2.0
    """
    pass


def pull(array: t.List[T], *values: T) -> t.List[T]:
    """
    Removes all provided values from the given array.

    Args:
        array: List to pull from.
        values: Values to remove.

    Returns:
        Modified `array`.

    Warning:
        `array` is modified in place.

    Example:

        >>> pull([1, 2, 2, 3, 3, 4], 2, 3)
        [1, 4]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        :func:`pull` method now calls :func:`pull_all` method for the desired
        functionality.
    """
    pass


def pull_all(array: t.List[T], values: t.Iterable[T]) -> t.List[T]:
    """
    Removes all provided values from the given array.

    Args:
        array: Array to modify.
        values: Values to remove.

    Returns:
        Modified `array`.

    Example:

        >>> pull_all([1, 2, 2, 3, 3, 4], [2, 3])
        [1, 4]

    .. versionadded:: 4.0.0
    """
    pass


def pull_all_by(
    array: t.List[T],
    values: t.Iterable[T],
    iteratee: t.Union[IterateeObjT, t.Callable[[T], t.Any], None] = None,
) -> t.List[T]:
    """
    This method is like :func:`pull_all` except that it accepts iteratee which is invoked for each
    element of array and values to generate the criterion by which they're compared. The iteratee is
    invoked with one argument: ``(value)``.

    Args:
        array: Array to modify.
        values: Values to remove.
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        Modified `array`.

    Example:

        >>> array = [{"x": 1}, {"x": 2}, {"x": 3}, {"x": 1}]
        >>> pull_all_by(array, [{"x": 1}, {"x": 3}], "x")
        [{'x': 2}]

    .. versionadded:: 4.0.0
    """
    pass


def pull_all_with(
    array: t.List[T],
    values: t.Iterable[T],
    comparator: t.Union[t.Callable[[T, T], t.Any], None] = None,
) -> t.List[T]:
    """
    This method is like :func:`pull_all` except that it accepts comparator which is invoked to
    compare elements of array to values. The comparator is invoked with two arguments: ``(arr_val,
    oth_val)``.

    Args:
        array: Array to modify.
        values: Values to remove.
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        Modified `array`.

    Example:

        >>> array = [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}]
        >>> res = pull_all_with(array, [{"x": 3, "y": 4}], lambda a, b: a == b)
        >>> res == [{"x": 1, "y": 2}, {"x": 5, "y": 6}]
        True
        >>> array = [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}]
        >>> res = pull_all_with(array, [{"x": 3, "y": 4}], lambda a, b: a != b)
        >>> res == [{"x": 3, "y": 4}]
        True

    .. versionadded:: 4.0.0
    """
    pass


def pull_at(array: t.List[T], *indexes: int) -> t.List[T]:
    """
    Removes elements from `array` corresponding to the specified indexes and returns a list of the
    removed elements. Indexes may be specified as a list of indexes or as individual arguments.

    Args:
        array: List to pull from.
        indexes: Indexes to pull.

    Returns:
        Modified `array`.

    Warning:
        `array` is modified in place.

    Example:

        >>> pull_at([1, 2, 3, 4], 0, 2)
        [2, 4]

    .. versionadded:: 1.1.0
    """
    pass


def push(array: t.List[T], *items: T2) -> t.List[t.Union[T, T2]]:
    """
    Push items onto the end of `array` and return modified `array`.

    Args:
        array: List to push to.
        items: Items to append.

    Returns:
        Modified `array`.

    Warning:
        `array` is modified in place.

    Example:

        >>> array = [1, 2, 3]
        >>> push(array, 4, 5, [6])
        [1, 2, 3, 4, 5, [6]]

    .. versionadded:: 2.2.0

    .. versionchanged:: 4.0.0
        Removed alias ``append``.
    """
    pass


def remove(
    array: t.List[T],
    predicate: t.Union[
        t.Callable[[T, int, t.List[T]], t.Any],
        t.Callable[[T, int], t.Any],
        t.Callable[[T], t.Any],
        None,
    ] = None,
) -> t.List[T]:
    """
    Removes all elements from a list that the predicate returns truthy for and returns an array of
    removed elements.

    Args:
        array: List to remove elements from.
        predicate: Predicate applied per iteration.

    Returns:
        Removed elements of `array`.

    Warning:
        `array` is modified in place.

    Example:

        >>> array = [1, 2, 3, 4]
        >>> items = remove(array, lambda x: x >= 3)
        >>> items
        [3, 4]
        >>> array
        [1, 2]

    .. versionadded:: 1.0.0
    """
    pass


def reverse(array: SequenceT) -> SequenceT:
    """
    Return `array` in reverse order.

    Args:
        array: Object to process.

    Returns:
        Reverse of object.

    Example:

        >>> reverse([1, 2, 3, 4])
        [4, 3, 2, 1]

    .. versionadded:: 2.2.0
    """
    pass


def shift(array: t.List[T]) -> T:
    """
    Remove the first element of `array` and return it.

    Args:
        array: List to shift.

    Returns:
        First element of `array`.

    Warning:
        `array` is modified in place.

    Example:

        >>> array = [1, 2, 3, 4]
        >>> item = shift(array)
        >>> item
        1
        >>> array
        [2, 3, 4]

    .. versionadded:: 2.2.0
    """
    pass


def slice_(array: SequenceT, start: int = 0, end: t.Union[int, None] = None) -> SequenceT:
    """
    Slices `array` from the `start` index up to, but not including, the `end` index.

    Args:
        array: Array to slice.
        start: Start index. Defaults to ``0``.
        end: End index. Defaults to selecting the value at ``start`` index.

    Returns:
        Sliced list.

    Example:

        >>> slice_([1, 2, 3, 4])
        [1]
        >>> slice_([1, 2, 3, 4], 1)
        [2]
        >>> slice_([1, 2, 3, 4], 1, 3)
        [2, 3]

    .. versionadded:: 1.1.0
    """
    pass


@t.overload
def sort(
    array: t.List["SupportsRichComparisonT"],
    comparator: None = None,
    key: None = None,
    reverse: bool = False,
) -> t.List["SupportsRichComparisonT"]: pass


@t.overload
def sort(
    array: t.List[T], comparator: t.Callable[[T, T], int], *, reverse: bool = False
) -> t.List[T]: pass


@t.overload
def sort(
    array: t.List[T], *, key: t.Callable[[T], "SupportsRichComparisonT"], reverse: bool = False
) -> t.List[T]: pass


def sort(array, comparator=None, key=None, reverse=False):
    """
    Sort `array` using optional `comparator`, `key`, and `reverse` options and return sorted
    `array`.

    Note:
        Python 3 removed the option to pass a custom comparator function and instead only allows a
        key function. Therefore, if a comparator function is passed in, it will be converted to a
        key function automatically using ``functools.cmp_to_key``.

    Args:
        array: List to sort.
        comparator: A custom comparator function used to sort the list.
            Function should accept two arguments and return a negative, zero, or position number
            depending on whether the first argument is considered smaller than, equal to, or larger
            than the second argument. Defaults to ``None``. This argument is mutually exclusive with
            `key`.
        key: A function of one argument used to extract a comparator key from each list element.
            Defaults to ``None``. This argument is mutually exclusive with `comparator`.
        reverse: Whether to reverse the sort. Defaults to ``False``.

    Returns:
        Sorted list.

    Warning:
        `array` is modified in place.

    Example:

        >>> sort([2, 1, 4, 3])
        [1, 2, 3, 4]
        >>> sort([2, 1, 4, 3], reverse=True)
        [4, 3, 2, 1]
        >>> results = sort([{'a': 2, 'b': 1},\
                            {'a': 3, 'b': 2},\
                            {'a': 0, 'b': 3}],\
                           key=lambda item: item['a'])
        >>> assert results == [{'a': 0, 'b': 3},\
                               {'a': 2, 'b': 1},\
                               {'a': 3, 'b': 2}]

    .. versionadded:: 2.2.0
    """
    pass


def sorted_index(
    array: t.Sequence["SupportsRichComparisonT"], value: "SupportsRichComparisonT"
) -> int:
    """
    Uses a binary search to determine the lowest index at which `value` should be inserted into
    `array` in order to maintain its sort order.

    Args:
        array: List to inspect.
        value: Value to evaluate.

    Returns:
        Returns the index at which `value` should be inserted into `array`.

    Example:

        >>> sorted_index([1, 2, 2, 3, 4], 2)
        1

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Move iteratee support to :func:`sorted_index_by`.
    """
    pass


@t.overload
def sorted_index_by(
    array: t.Sequence[T],
    value: T,
    iteratee: t.Union[IterateeObjT, t.Callable[[T], "SupportsRichComparisonT"]],
) -> int: pass


@t.overload
def sorted_index_by(
    array: t.Sequence["SupportsRichComparisonT"],
    value: "SupportsRichComparisonT",
    iteratee: None = None,
) -> int: pass


def sorted_index_by(array, value, iteratee=None):
    """
    This method is like :func:`sorted_index` except that it accepts iteratee which is invoked for
    `value` and each element of `array` to compute their sort ranking. The iteratee is invoked with
    one argument: ``(value)``.

    Args:
        array: List to inspect.
        value: Value to evaluate.
        iteratee: The iteratee invoked per element. Defaults to :func:`.identity`.

    Returns:
        Returns the index at which `value` should be inserted into `array`.

    Example:

        >>> array = [{"x": 4}, {"x": 5}]
        >>> sorted_index_by(array, {"x": 4}, lambda o: o["x"])
        0
        >>> sorted_index_by(array, {"x": 4}, "x")
        0

    .. versionadded:: 4.0.0
    """
    pass


def sorted_index_of(
    array: t.Sequence["SupportsRichComparisonT"], value: "SupportsRichComparisonT"
) -> int:
    """
    Returns the index of the matched `value` from the sorted `array`, else ``-1``.

    Args:
        array: Array to inspect.
        value: Value to search for.

    Returns:
        Returns the index of the first matched value, else ``-1``.

    Example:

        >>> sorted_index_of([3, 5, 7, 10], 3)
        0
        >>> sorted_index_of([10, 10, 5, 7, 3], 10)
        -1

    .. versionadded:: 4.0.0
    """
    pass


def sorted_last_index(
    array: t.Sequence["SupportsRichComparisonT"], value: "SupportsRichComparisonT"
) -> int:
    """
    This method is like :func:`sorted_index` except that it returns the highest index at which
    `value` should be inserted into `array` in order to maintain its sort order.

    Args:
        array: List to inspect.
        value: Value to evaluate.

    Returns:
        Returns the index at which `value` should be inserted into `array`.

    Example:

        >>> sorted_last_index([1, 2, 2, 3, 4], 2)
        3

    .. versionadded:: 1.1.0

    .. versionchanged:: 4.0.0
        Move iteratee support to :func:`sorted_last_index_by`.
    """
    pass


@t.overload
def sorted_last_index_by(
    array: t.Sequence[T],
    value: T,
    iteratee: t.Union[IterateeObjT, t.Callable[[T], "SupportsRichComparisonT"]],
) -> int: pass


@t.overload
def sorted_last_index_by(
    array: t.Sequence["SupportsRichComparisonT"],
    value: "SupportsRichComparisonT",
    iteratee: None = None,
) -> int: pass


def sorted_last_index_by(array, value, iteratee=None):
    """
    This method is like :func:`sorted_last_index` except that it accepts iteratee which is invoked
    for `value` and each element of `array` to compute their sort ranking. The iteratee is invoked
    with one argument: ``(value)``.

    Args:
        array: List to inspect.
        value: Value to evaluate.
        iteratee: The iteratee invoked per element. Defaults to :func:`.identity`.

    Returns:
        Returns the index at which `value` should be inserted into `array`.

    Example:

        >>> array = [{"x": 4}, {"x": 5}]
        >>> sorted_last_index_by(array, {"x": 4}, lambda o: o["x"])
        1
        >>> sorted_last_index_by(array, {"x": 4}, "x")
        1
    """
    pass


def sorted_last_index_of(
    array: t.Sequence["SupportsRichComparisonT"], value: "SupportsRichComparisonT"
) -> int:
    """
    This method is like :func:`last_index_of` except that it performs a binary search on a sorted
    `array`.

    Args:
        array: Array to inspect.
        value: Value to search for.

    Returns:
        Returns the index of the matched value, else ``-1``.

    Example:

        >>> sorted_last_index_of([4, 5, 5, 5, 6], 5)
        3
        >>> sorted_last_index_of([6, 5, 5, 5, 4], 6)
        -1

    .. versionadded:: 4.0.0
    """
    pass


def sorted_uniq(array: t.Iterable["SupportsRichComparisonT"]) -> t.List["SupportsRichComparisonT"]:
    """
    Return sorted array with unique elements.

    Args:
        array: List of values to be sorted.

    Returns:
        List of unique elements in a sorted fashion.

    Example:

        >>> sorted_uniq([4, 2, 2, 5])
        [2, 4, 5]
        >>> sorted_uniq([-2, -2, 4, 1])
        [-2, 1, 4]

    .. versionadded:: 4.0.0
    """
    pass


def sorted_uniq_by(
    array: t.Iterable["SupportsRichComparisonT"],
    iteratee: t.Union[
        t.Callable[["SupportsRichComparisonT"], "SupportsRichComparisonT"], None
    ] = None,
) -> t.List["SupportsRichComparisonT"]:
    """
    This method is like :func:`sorted_uniq` except that it accepts iteratee which is invoked for
    each element in array to generate the criterion by which uniqueness is computed. The order of
    result values is determined by the order they occur in the array. The iteratee is invoked with
    one argument: ``(value)``.

    Args:
        array: List of values to be sorted.
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        Unique list.

    Example:

        >>> sorted_uniq_by([3, 2, 1, 3, 2, 1], lambda val: val % 2)
        [2, 3]

    .. versionadded:: 4.0.0
    """
    pass


def splice(
    array: MutableSequenceT, start: int, count: t.Union[int, None] = None, *items: t.Any
) -> MutableSequenceT:
    """
    Modify the contents of `array` by inserting elements starting at index `start` and removing
    `count` number of elements after.

    Args:
        array: List to splice.
        start: Start to splice at.
        count: Number of items to remove starting at `start`. If ``None`` then all
            items after `start` are removed. Defaults to ``None``.
        items: Elements to insert starting at `start`. Each item is inserted in the order
            given.

    Returns:
        The removed elements of `array` or the spliced string.

    Warning:
        `array` is modified in place if ``list``.

    Example:

        >>> array = [1, 2, 3, 4]
        >>> splice(array, 1)
        [2, 3, 4]
        >>> array
        [1]
        >>> array = [1, 2, 3, 4]
        >>> splice(array, 1, 2)
        [2, 3]
        >>> array
        [1, 4]
        >>> array = [1, 2, 3, 4]
        >>> splice(array, 1, 2, 0, 0)
        [2, 3]
        >>> array
        [1, 0, 0, 4]

    .. versionadded:: 2.2.0

    .. versionchanged:: 3.0.0
        Support string splicing.
    """
    pass


def split_at(array: t.Sequence[T], index: int) -> t.List[t.Sequence[T]]:
    """
    Returns a list of two lists composed of the split of `array` at `index`.

    Args:
        array: List to split.
        index: Index to split at.

    Returns:
        Split list.

    Example:

        >>> split_at([1, 2, 3, 4], 2)
        [[1, 2], [3, 4]]

    .. versionadded:: 2.0.0
    """
    pass


def tail(array: t.Sequence[T]) -> t.Sequence[T]:
    """
    Return all but the first element of `array`.

    Args:
        array: List to process.

    Returns:
        Rest of the list.

    Example:

        >>> tail([1, 2, 3, 4])
        [2, 3, 4]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Renamed from ``rest`` to ``tail``.
    """
    pass


def take(array: t.Sequence[T], n: int = 1) -> t.Sequence[T]:
    """
    Creates a slice of `array` with `n` elements taken from the beginning.

    Args:
        array: List to process.
        n: Number of elements to take. Defaults to ``1``.

    Returns:
        Taken list.

    Example:

        >>> take([1, 2, 3, 4], 2)
        [1, 2]

    .. versionadded:: 1.0.0

    .. versionchanged:: 1.1.0
        Added ``n`` argument and removed as alias of :func:`first`.

    .. versionchanged:: 3.0.0
        Made ``n`` default to ``1``.
    """
    pass


def take_right(array: t.Sequence[T], n: int = 1) -> t.Sequence[T]:
    """
    Creates a slice of `array` with `n` elements taken from the end.

    Args:
        array: List to process.
        n: Number of elements to take. Defaults to ``1``.

    Returns:
        Taken list.

    Example:

        >>> take_right([1, 2, 3, 4], 2)
        [3, 4]

    .. versionadded:: 1.1.0

    .. versionchanged:: 3.0.0
        Made ``n`` default to ``1``.
    """
    pass


@t.overload
def take_right_while(
    array: t.Sequence[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> t.Sequence[T]: pass


@t.overload
def take_right_while(
    array: t.Sequence[T], predicate: t.Callable[[T, int], t.Any]
) -> t.Sequence[T]: pass


@t.overload
def take_right_while(array: t.Sequence[T], predicate: t.Callable[[T], t.Any]) -> t.Sequence[T]: pass


@t.overload
def take_right_while(array: t.Sequence[T], predicate: None = None) -> t.Sequence[T]: pass


def take_right_while(array, predicate=None):
    """
    Creates a slice of `array` with elements taken from the end. Elements are taken until the
    `predicate` returns falsey. The `predicate` is invoked with three arguments: ``(value, index,
    array)``.

    Args:
        array: List to process.
        predicate: Predicate called per iteration

    Returns:
        Dropped list.

    Example:

        >>> take_right_while([1, 2, 3, 4], lambda x: x >= 3)
        [3, 4]

    .. versionadded:: 1.1.0
    """
    pass


@t.overload
def take_while(
    array: t.Sequence[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> t.List[T]: pass


@t.overload
def take_while(array: t.Sequence[T], predicate: t.Callable[[T, int], t.Any]) -> t.List[T]: pass


@t.overload
def take_while(array: t.Sequence[T], predicate: t.Callable[[T], t.Any]) -> t.List[T]: pass


@t.overload
def take_while(array: t.Sequence[T], predicate: None = None) -> t.List[T]: pass


def take_while(array, predicate=None):
    """
    Creates a slice of `array` with elements taken from the beginning. Elements are taken until the
    `predicate` returns falsey. The `predicate` is invoked with three arguments: ``(value, index,
    array)``.

    Args:
        array: List to process.
        predicate: Predicate called per iteration

    Returns:
        Taken list.

    Example:

        >>> take_while([1, 2, 3, 4], lambda x: x < 3)
        [1, 2]

    .. versionadded:: 1.1.0
    """
    pass


@t.overload
def union(array: t.Sequence[T]) -> t.List[T]: pass


@t.overload
def union(array: t.Sequence[T], *others: t.Sequence[T2]) -> t.List[t.Union[T, T2]]: pass


def union(array, *others):
    """
    Computes the union of the passed-in arrays.

    Args:
        array: List to union with.
        others: Lists to unionize with `array`.

    Returns:
        Unionized list.

    Example:

        >>> union([1, 2, 3], [2, 3, 4], [3, 4, 5])
        [1, 2, 3, 4, 5]

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def union_by(
    array: t.Sequence[T], *others: t.Iterable[T], iteratee: t.Callable[[T], t.Any]
) -> t.List[T]: pass


@t.overload
def union_by(
    array: t.Sequence[T], *others: t.Union[t.Iterable[T], t.Callable[[T], t.Any]]
) -> t.List[T]: pass


def union_by(array, *others, **kwargs):
    """
    This method is similar to :func:`union` except that it accepts iteratee which is invoked for
    each element of each array to generate the criterion by which uniqueness is computed.

    Args:
        array: List to unionize with.
        others: Lists to unionize with `array`.

    Keyword Args:
        iteratee: Function to invoke on each element.

    Returns:
        Unionized list.

    Example:

        >>> union_by([1, 2, 3], [2, 3, 4], iteratee=lambda x: x % 2)
        [1, 2]
        >>> union_by([1, 2, 3], [2, 3, 4], iteratee=lambda x: x % 9)
        [1, 2, 3, 4]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def union_with(
    array: t.Sequence[T], *others: t.Iterable[T2], comparator: t.Callable[[T, T2], t.Any]
) -> t.List[T]: pass


@t.overload
def union_with(
    array: t.Sequence[T], *others: t.Union[t.Iterable[T2], t.Callable[[T, T2], t.Any]]
) -> t.List[T]: pass


def union_with(array, *others, **kwargs):
    """
    This method is like :func:`union` except that it accepts comparator which is invoked to compare
    elements of arrays. Result values are chosen from the first array in which the value occurs.

    Args:
        array: List to unionize with.
        others: Lists to unionize with `array`.

    Keyword Args:
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        Unionized list.

    Example:

        >>> comparator = lambda a, b: (a % 2) == (b % 2)
        >>> union_with([1, 2, 3], [2, 3, 4], comparator=comparator)
        [1, 2]
        >>> union_with([1, 2, 3], [2, 3, 4])
        [1, 2, 3, 4]

    .. versionadded:: 4.0.0
    """
    pass


def uniq(array: t.Iterable[T]) -> t.List[T]:
    """
    Creates a duplicate-value-free version of the array. If iteratee is passed, each element of
    array is passed through an iteratee before uniqueness is computed. The iteratee is invoked with
    three arguments: ``(value, index, array)``. If an object path is passed for iteratee, the
    created iteratee will return the path value of the given element. If an object is passed for
    iteratee, the created filter style iteratee will return ``True`` for elements that have the
    properties of the given object, else ``False``.

    Args:
        array: List to process.

    Returns:
        Unique list.

    Example:

        >>> uniq([1, 2, 3, 1, 2, 3])
        [1, 2, 3]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0

        - Moved `iteratee` argument to :func:`uniq_by`.
        - Removed alias ``unique``.
    """
    pass


def uniq_by(
    array: t.Iterable[T], iteratee: t.Union[t.Callable[[T], t.Any], None] = None
) -> t.List[T]:
    """
    This method is like :func:`uniq` except that it accepts iteratee which is invoked for each
    element in array to generate the criterion by which uniqueness is computed. The order of result
    values is determined by the order they occur in the array. The iteratee is invoked with one
    argument: ``(value)``.

    Args:
        array: List to process.
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        Unique list.

    Example:

        >>> uniq_by([1, 2, 3, 1, 2, 3], lambda val: val % 2)
        [1, 2]

    .. versionadded:: 4.0.0
    """
    pass


def uniq_with(
    array: t.Sequence[T], comparator: t.Union[t.Callable[[T, T], t.Any], None] = None
) -> t.List[T]:
    """
    This method is like :func:`uniq` except that it accepts comparator which is invoked to compare
    elements of array. The order of result values is determined by the order they occur in the
    array.The comparator is invoked with two arguments: ``(value, other)``.

    Args:
        array: List to process.
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        Unique list.

    Example:

        >>> uniq_with([1, 2, 3, 4, 5], lambda a, b: (a % 2) == (b % 2))
        [1, 2]

    .. versionadded:: 4.0.0
    """
    pass


def unshift(array: t.List[T], *items: T2) -> t.List[t.Union[T, T2]]:
    """
    Insert the given elements at the beginning of `array` and return the modified list.

    Args:
        array: List to modify.
        items: Items to insert.

    Returns:
        Modified list.

    Warning:
        `array` is modified in place.

    Example:

        >>> array = [1, 2, 3, 4]
        >>> unshift(array, -1, -2)
        [-1, -2, 1, 2, 3, 4]
        >>> array
        [-1, -2, 1, 2, 3, 4]

    .. versionadded:: 2.2.0
    """
    pass


@t.overload
def unzip(array: t.Iterable[t.Tuple[T, T2]]) -> t.List[t.Tuple[T, T2]]: pass


@t.overload
def unzip(array: t.Iterable[t.Tuple[T, T2, T3]]) -> t.List[t.Tuple[T, T2, T3]]: pass


@t.overload
def unzip(array: t.Iterable[t.Tuple[T, T2, T3, T4]]) -> t.List[t.Tuple[T, T2, T3, T4]]: pass


@t.overload
def unzip(array: t.Iterable[t.Tuple[T, T2, T3, T4, T5]]) -> t.List[t.Tuple[T, T2, T3, T4, T5]]: pass


@t.overload
def unzip(array: t.Iterable[t.Iterable[t.Any]]) -> t.List[t.Tuple[t.Any, ...]]: pass


def unzip(array):
    """
    The inverse of :func:`zip_`, this method splits groups of elements into tuples composed of
    elements from each group at their corresponding indexes.

    Args:
        array: List to process.

    Returns:
        Unzipped list.

    Example:

        >>> unzip([(1, 4, 7), (2, 5, 8), (3, 6, 9)])
        [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    .. versionadded:: 1.0.0

    .. versionchanged:: 8.0.0
        Support list of tuples instead.
    """
    pass


@t.overload
def unzip_with(
    array: t.Iterable[t.Tuple[T, T2]],
    iteratee: t.Union[
        t.Callable[[t.Union[T, T2, T3], t.Union[T, T2], int], T3],
        t.Callable[[t.Union[T, T2, T3], t.Union[T, T2]], T3],
        t.Callable[[t.Union[T, T2, T3]], T3],
    ],
) -> t.List[T3]: pass


@t.overload
def unzip_with(
    array: t.Iterable[t.Iterable[t.Any]],
    iteratee: t.Union[
        t.Callable[[t.Any, t.Any, int], T3],
        t.Callable[[t.Any, t.Any], T3],
        t.Callable[[t.Any], T3],
    ],
) -> t.List[T3]: pass


@t.overload
def unzip_with(
    array: t.Iterable[t.Iterable[T]],
    iteratee: None = None,
) -> t.List[t.Tuple[T]]: pass


def unzip_with(array, iteratee=None):
    """
    This method is like :func:`unzip` except that it accepts an iteratee to specify how regrouped
    values should be combined. The iteratee is invoked with three arguments: ``(accumulator, value,
    index)``.

    Args:
        array: List to process.
        iteratee: Function to combine regrouped values.

    Returns:
        Unzipped list.

    Example:

        >>> from pydash import add
        >>> unzip_with([(1, 10, 100), (2, 20, 200)], add)
        [3, 30, 300]

    .. versionadded:: 3.3.0
    """
    pass


def without(array: t.Iterable[T], *values: T) -> t.List[T]:
    """
    Creates an array with all occurrences of the passed values removed.

    Args:
        array: List to filter.
        values: Values to remove.

    Returns:
        Filtered list.

    Example:

        >>> without([1, 2, 3, 2, 4, 4], 2, 4)
        [1, 3]

    .. versionadded:: 1.0.0
    """
    pass


def xor(array: t.Iterable[T], *lists: t.Iterable[T]) -> t.List[T]:
    """
    Creates a list that is the symmetric difference of the provided lists.

    Args:
        array: List to process.
        *lists: Lists to xor with.

    Returns:
        XOR'd list.

    Example:

        >>> xor([1, 3, 4], [1, 2, 4], [2])
        [3]

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def xor_by(
    array: t.Iterable[T],
    *lists: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT],
) -> t.List[T]: pass


@t.overload
def xor_by(
    array: t.Iterable[T], *lists: t.Union[t.Iterable[T], t.Callable[[T], t.Any]]
) -> t.List[T]: pass


def xor_by(array, *lists, **kwargs):
    """
    This method is like :func:`xor` except that it accepts iteratee which is invoked for each
    element of each arras to generate the criterion by which they're compared. The order of result
    values is determined by the order they occur in the arrays. The iteratee is invoked with one
    argument: ``(value)``.

    Args:
        array: List to process.
        *lists: Lists to xor with.

    Keyword Args:
        iteratee: Function to transform the elements of the arrays. Defaults to
            :func:`.identity`.

    Returns:
        XOR'd list.

    Example:

        >>> xor_by([2.1, 1.2], [2.3, 3.4], round)
        [1.2, 3.4]
        >>> xor_by([{"x": 1}], [{"x": 2}, {"x": 1}], "x")
        [{'x': 2}]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def xor_with(
    array: t.Sequence[T], *lists: t.Iterable[T2], comparator: t.Callable[[T, T2], t.Any]
) -> t.List[T]: pass


@t.overload
def xor_with(
    array: t.Sequence[T], *lists: t.Union[t.Iterable[T2], t.Callable[[T, T2], t.Any]]
) -> t.List[T]: pass


def xor_with(array, *lists, **kwargs):
    """
    This method is like :func:`xor` except that it accepts comparator which is invoked to compare
    elements of arrays. The order of result values is determined by the order they occur in the
    arrays. The comparator is invoked with two arguments: ``(arr_val, oth_val)``.

    Args:
        array: List to process.
        *lists: Lists to xor with.

    Keyword Args:
        comparator: Function to compare the elements of the arrays. Defaults to
            :func:`.is_equal`.

    Returns:
        XOR'd list.

    Example:

        >>> objects = [{"x": 1, "y": 2}, {"x": 2, "y": 1}]
        >>> others = [{"x": 1, "y": 1}, {"x": 1, "y": 2}]
        >>> expected = [{"y": 1, "x": 2}, {"y": 1, "x": 1}]
        >>> xor_with(objects, others, lambda a, b: a == b) == expected
        True

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def zip_(array1: t.Iterable[T], array2: t.Iterable[T2], /) -> t.List[t.Tuple[T, T2]]: pass


@t.overload
def zip_(
    array1: t.Iterable[T], array2: t.Iterable[T2], array3: t.Iterable[T3], /
) -> t.List[t.Tuple[T, T2, T3]]: pass


@t.overload
def zip_(
    array1: t.Iterable[T], array2: t.Iterable[T2], array3: t.Iterable[T3], array4: t.Iterable[T4], /
) -> t.List[t.Tuple[T, T2, T3, T4]]: pass


@t.overload
def zip_(
    array1: t.Iterable[T],
    array2: t.Iterable[T2],
    array3: t.Iterable[T3],
    array4: t.Iterable[T4],
    array5: t.Iterable[T5],
    /,
) -> t.List[t.Tuple[T, T2, T3, T4, T5]]: pass


@t.overload
def zip_(*arrays: t.Iterable[t.Any]) -> t.List[t.Tuple[t.Any, ...]]: pass


def zip_(*arrays):
    """
    Groups the elements of each array at their corresponding indexes. Useful for separate data
    sources that are coordinated through matching array indexes.

    Args:
        arrays: Lists to process.

    Returns:
        Zipped list.

    Example:

        >>> zip_([1, 2, 3], [4, 5, 6], [7, 8, 9])
        [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

    .. versionadded:: 1.0.0

    .. versionchanged:: 8.0.0
        Return list of tuples instead of list of lists.
    """
    pass


@t.overload
def zip_object(keys: t.Iterable[t.Tuple[T, T2]], values: None = None) -> t.Dict[T, T2]: pass


@t.overload
def zip_object(
    keys: t.Iterable[t.List[t.Union[T, T2]]], values: None = None
) -> t.Dict[t.Union[T, T2], t.Union[T, T2]]: pass


@t.overload
def zip_object(keys: t.Iterable[T], values: t.List[T2]) -> t.Dict[T, T2]: pass


def zip_object(keys, values=None):
    """
    Creates a dict composed of lists of keys and values. Pass either a single two-dimensional list,
    i.e. ``[[key1, value1], [key2, value2]]``, or two lists, one of keys and one of corresponding
    values.

    Args:
        keys: Either a list of keys or a list of ``[key, value]`` pairs.
        values: List of values to zip.

    Returns:
        Zipped dict.

    Example:

        >>> zip_object([1, 2, 3], [4, 5, 6])
        {1: 4, 2: 5, 3: 6}

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``object_``.
    """
    pass


def zip_object_deep(
    keys: t.Iterable[t.Any], values: t.Union[t.List[t.Any], None] = None
) -> t.Dict[t.Any, t.Any]:
    """
    This method is like :func:`zip_object` except that it supports property paths.

    Args:
        keys: Either a list of keys or a list of ``[key, value]`` pairs.
        values: List of values to zip.

    Returns:
        Zipped dict.

    Example:

        >>> expected = {"a": {"b": {"c": 1, "d": 2}}}
        >>> zip_object_deep(["a.b.c", "a.b.d"], [1, 2]) == expected
        True

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def zip_with(
    array1: t.Iterable[T],
    array2: t.Iterable[T2],
    *,
    iteratee: t.Union[
        t.Callable[[T, T2, int], T3],
        t.Callable[[T, T2], T3],
        t.Callable[[T], T3],
    ],
) -> t.List[T3]: pass


@t.overload
def zip_with(
    *arrays: t.Iterable[t.Any],
    iteratee: t.Union[
        t.Callable[[t.Any, t.Any, int], T2],
        t.Callable[[t.Any, t.Any], T2],
        t.Callable[[t.Any], T2],
    ],
) -> t.List[T2]: pass


@t.overload
def zip_with(
    *arrays: t.Union[
        t.Iterable[t.Any],
        t.Callable[[t.Any, t.Any, int], T2],
        t.Callable[[t.Any, t.Any], T2],
        t.Callable[[t.Any], T2],
    ],
) -> t.List[T2]: pass


def zip_with(*arrays, **kwargs):
    """
    This method is like :func:`zip` except that it accepts an iteratee to specify how grouped values
    should be combined. The iteratee is invoked with three arguments:
    ``(accumulator, value, index)``.

    Args:
        *arrays: Lists to process.

    Keyword Args:
        iteratee (callable): Function to combine grouped values.

    Returns:
        Zipped list of grouped elements.

    Example:

        >>> from pydash import add
        >>> zip_with([1, 2], [10, 20], [100, 200], add)
        [111, 222]
        >>> zip_with([1, 2], [10, 20], [100, 200], iteratee=add)
        [111, 222]

    .. versionadded:: 3.3.0
    """
    pass


#
# Utility methods not a part of the main API
#


def iterflatten(array, depth=-1):
    """Iteratively flatten a list shallowly or deeply."""
    pass


def iterinterleave(*arrays):
    """Interleave multiple lists."""
    pass


def iterintersperse(iterable, separator):
    """Iteratively intersperse iterable."""
    pass


def iterunique(array, comparator=None, iteratee=None):  # noqa: PLR0912
    """Yield each unique item in array."""
    pass


def iterduplicates(array):
    """Yield duplictes found in `array`."""
    pass


def iterintersection(array, other, comparator=None, iteratee=None):
    """Yield intersecting values between `array` and `other` using `comparator` to determine if they
    intersect."""
    pass


def iterdifference(array, other, comparator=None, iteratee=None):
    """Yield different values in `array` as compared to `other` using `comparator` to determine if
    they are different."""
    pass
