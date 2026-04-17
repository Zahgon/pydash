"""
Functions that operate on lists and dicts.

.. versionadded:: 1.0.0
"""

from __future__ import annotations

from functools import cmp_to_key
import random
import typing as t

import pydash as pyd

from .helpers import callit, cmp, getargcount, iterator, iteriteratee
from .types import IterateeObjT, PathT


__all__ = (
    "at",
    "count_by",
    "every",
    "filter_",
    "find",
    "find_last",
    "flat_map",
    "flat_map_deep",
    "flat_map_depth",
    "for_each",
    "for_each_right",
    "group_by",
    "includes",
    "invoke_map",
    "key_by",
    "map_",
    "nest",
    "order_by",
    "partition",
    "pluck",
    "reduce_",
    "reduce_right",
    "reductions",
    "reductions_right",
    "reject",
    "sample",
    "sample_size",
    "shuffle",
    "size",
    "some",
    "sort_by",
)

T = t.TypeVar("T")
T2 = t.TypeVar("T2")
T3 = t.TypeVar("T3")
T4 = t.TypeVar("T4")


@t.overload
def at(collection: t.Mapping[T, T2], *paths: T) -> t.List[t.Union[T2, None]]: pass


@t.overload
def at(collection: t.Mapping[T, t.Any], *paths: t.Union[T, t.Iterable[T]]) -> t.List[t.Any]: pass


@t.overload
def at(collection: t.Iterable[T], *paths: int) -> t.List[t.Union[T, None]]: pass


@t.overload
def at(collection: t.Iterable[t.Any], *paths: t.Union[int, t.Iterable[int]]) -> t.List[t.Any]: pass


def at(collection, *paths):
    """
    Creates a list of elements from the specified indexes, or keys, of the collection. Indexes may
    be specified as individual arguments or as arrays of indexes.

    Args:
        collection: Collection to iterate over.
        *paths: The indexes of `collection` to retrieve, specified as individual indexes or
            arrays of indexes.

    Returns:
        filtered list

    Example:

        >>> at([1, 2, 3, 4], 0, 2)
        [1, 3]
        >>> at({"a": 1, "b": 2, "c": 3, "d": 4}, "a", "c")
        [1, 3]
        >>> at({"a": 1, "b": 2, "c": {"d": {"e": 3}}}, "a", ["c", "d", "e"])
        [1, 3]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.1.0
        Support deep path access.
    """
    pass


@t.overload
def count_by(collection: t.Mapping[t.Any, T2], iteratee: None = None) -> t.Dict[T2, int]: pass


@t.overload
def count_by(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], T3]
) -> t.Dict[T3, int]: pass


@t.overload
def count_by(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], T3]
) -> t.Dict[T3, int]: pass


@t.overload
def count_by(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], T3]
) -> t.Dict[T3, int]: pass


@t.overload
def count_by(collection: t.Iterable[T], iteratee: None = None) -> t.Dict[T, int]: pass


@t.overload
def count_by(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], T2]
) -> t.Dict[T2, int]: pass


@t.overload
def count_by(collection: t.Iterable[T], iteratee: t.Callable[[T, int], T2]) -> t.Dict[T2, int]: pass


@t.overload
def count_by(collection: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.Dict[T2, int]: pass


def count_by(collection, iteratee=None):
    """
    Creates an object composed of keys generated from the results of running each element of
    `collection` through the iteratee.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Dict containing counts by key.

    Example:

        >>> results = count_by([1, 2, 1, 2, 3, 4])
        >>> assert results == {1: 2, 2: 2, 3: 1, 4: 1}
        >>> results = count_by(["a", "A", "B", "b"], lambda x: x.lower())
        >>> assert results == {"a": 2, "b": 2}
        >>> results = count_by({"a": 1, "b": 1, "c": 3, "d": 3})
        >>> assert results == {1: 2, 3: 2}

    .. versionadded:: 1.0.0
    """
    pass


def every(
    collection: t.Iterable[T], predicate: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None
) -> bool:
    """
    Checks if the predicate returns a truthy value for all elements of a collection. The predicate
    is invoked with three arguments: ``(value, index|key, collection)``. If a property name is
    passed for predicate, the created :func:`pluck` style predicate will return the property value
    of the given element. If an object is passed for predicate, the created :func:`.matches` style
    predicate will return ``True`` for elements that have the properties of the given object, else
    ``False``.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        Whether all elements are truthy.

    Example:

        >>> every([1, True, "hello"])
        True
        >>> every([1, False, "hello"])
        False
        >>> every([{"a": 1}, {"a": True}, {"a": "hello"}], "a")
        True
        >>> every([{"a": 1}, {"a": False}, {"a": "hello"}], "a")
        False
        >>> every([{"a": 1}, {"a": 1}], {"a": 1})
        True
        >>> every([{"a": 1}, {"a": 2}], {"a": 1})
        False

    .. versionadded:: 1.0.0

    .. versionchanged: 4.0.0
        Removed alias ``all_``.
    """
    pass


@t.overload
def filter_(
    collection: t.Mapping[T, T2],
    predicate: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def filter_(
    collection: t.Mapping[T, T2],
    predicate: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def filter_(
    collection: t.Mapping[t.Any, T2],
    predicate: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def filter_(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def filter_(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T, int], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def filter_(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


def filter_(collection, predicate=None):
    """
    Iterates over elements of a collection, returning a list of all elements the predicate returns
    truthy for.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        Filtered list.

    Example:

        >>> results = filter_([{"a": 1}, {"b": 2}, {"a": 1, "b": 3}], {"a": 1})
        >>> assert results == [{"a": 1}, {"a": 1, "b": 3}]
        >>> filter_([1, 2, 3, 4], lambda x: x >= 3)
        [3, 4]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``select``.
    """
    pass


@t.overload
def find(
    collection: t.Dict[T, T2],
    predicate: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find(
    collection: t.Dict[T, T2],
    predicate: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find(
    collection: t.Dict[T, T2],
    predicate: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


@t.overload
def find(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T, int], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


@t.overload
def find(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


def find(collection, predicate=None):
    """
    Iterates over elements of a collection, returning the first element that the predicate returns
    truthy for.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        First element found or ``None``.

    Example:

        >>> find([1, 2, 3, 4], lambda x: x >= 3)
        3
        >>> find([{"a": 1}, {"b": 2}, {"a": 1, "b": 2}], {"a": 1})
        {'a': 1}

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed aliases ``detect`` and ``find_where``.
    """
    pass


@t.overload
def find_last(
    collection: t.Dict[T, T2],
    predicate: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find_last(
    collection: t.Dict[T, T2],
    predicate: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find_last(
    collection: t.Dict[t.Any, T2],
    predicate: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
) -> t.Union[T2, None]: pass


@t.overload
def find_last(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


@t.overload
def find_last(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T, int], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


@t.overload
def find_last(
    collection: t.List[T],
    predicate: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
) -> t.Union[T, None]: pass


def find_last(collection, predicate=None):
    """
    This method is like :func:`find` except that it iterates over elements of a `collection` from
    right to left.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        Last element found or ``None``.

    Example:

        >>> find_last([1, 2, 3, 4], lambda x: x >= 3)
        4
        >>> results = find_last([{'a': 1}, {'b': 2}, {'a': 1, 'b': 2}],\
                                 {'a': 1})
        >>> assert results == {'a': 1, 'b': 2}

    .. versionadded:: 1.0.0
    """
    pass


@t.overload
def flat_map(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], t.Iterable[T3]]
) -> t.List[T3]: pass


@t.overload
def flat_map(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], t.Iterable[T3]]
) -> t.List[T3]: pass


@t.overload
def flat_map(
    collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], t.Iterable[T3]]
) -> t.List[T3]: pass


@t.overload
def flat_map(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], T3]
) -> t.List[T3]: pass


@t.overload
def flat_map(collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], T3]) -> t.List[T3]: pass


@t.overload
def flat_map(collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], T3]) -> t.List[T3]: pass


@t.overload
def flat_map(collection: t.Mapping[t.Any, t.Iterable[T2]], iteratee: None = None) -> t.List[T2]: pass


@t.overload
def flat_map(collection: t.Mapping[t.Any, T2], iteratee: None = None) -> t.List[T2]: pass


@t.overload
def flat_map(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], t.Iterable[T2]]
) -> t.List[T2]: pass


@t.overload
def flat_map(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int], t.Iterable[T2]]
) -> t.List[T2]: pass


@t.overload
def flat_map(
    collection: t.Iterable[T], iteratee: t.Callable[[T], t.Iterable[T2]]
) -> t.List[T2]: pass


@t.overload
def flat_map(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], T2]
) -> t.List[T2]: pass


@t.overload
def flat_map(collection: t.Iterable[T], iteratee: t.Callable[[T, int], T2]) -> t.List[T2]: pass


@t.overload
def flat_map(collection: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.List[T2]: pass


@t.overload
def flat_map(collection: t.Iterable[t.Iterable[T]], iteratee: None = None) -> t.List[T]: pass


@t.overload
def flat_map(collection: t.Iterable[T], iteratee: None = None) -> t.List[T]: pass


def flat_map(collection, iteratee=None):
    """
    Creates a flattened list of values by running each element in collection through `iteratee` and
    flattening the mapped results. The `iteratee` is invoked with three arguments: ``(value,
    index|key, collection)``.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Flattened mapped list.

    Example:

        >>> duplicate = lambda n: [[n, n]]
        >>> flat_map([1, 2], duplicate)
        [[1, 1], [2, 2]]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def flat_map_deep(
    collection: t.Mapping[T, T2],
    iteratee: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], None] = None,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_deep(
    collection: t.Mapping[T, T2], iteratee: t.Union[t.Callable[[T2, T], t.Any], None] = None
) -> t.List[t.Any]: pass


@t.overload
def flat_map_deep(
    collection: t.Mapping[t.Any, T2], iteratee: t.Union[t.Callable[[T2], t.Any], None] = None
) -> t.List[t.Any]: pass


@t.overload
def flat_map_deep(
    collection: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T, int, t.List[T]], t.Any], None] = None,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_deep(
    collection: t.Iterable[T], iteratee: t.Union[t.Callable[[T, int], t.Any], None] = None
) -> t.List[t.Any]: pass


@t.overload
def flat_map_deep(
    collection: t.Iterable[T], iteratee: t.Union[t.Callable[[T], t.Any], None] = None
) -> t.List[t.Any]: pass


def flat_map_deep(collection, iteratee=None):
    """
    This method is like :func:`flat_map` except that it recursively flattens the mapped results.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Flattened mapped list.

    Example:

        >>> duplicate = lambda n: [[n, n]]
        >>> flat_map_deep([1, 2], duplicate)
        [1, 1, 2, 2]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def flat_map_depth(
    collection: t.Mapping[T, T2],
    iteratee: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_depth(
    collection: t.Mapping[T, T2],
    iteratee: t.Union[t.Callable[[T2, T], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_depth(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Union[t.Callable[[T2], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_depth(
    collection: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T, int, t.List[T]], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_depth(
    collection: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T, int], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


@t.overload
def flat_map_depth(
    collection: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T], t.Any], None] = None,
    depth: int = 1,
) -> t.List[t.Any]: pass


def flat_map_depth(collection, iteratee=None, depth=1):
    """
    This method is like :func:`flat_map` except that it recursively flattens the mapped results up
    to `depth` times.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Flattened mapped list.

    Example:

        >>> duplicate = lambda n: [[n, n]]
        >>> flat_map_depth([1, 2], duplicate, 1)
        [[1, 1], [2, 2]]
        >>> flat_map_depth([1, 2], duplicate, 2)
        [1, 1, 2, 2]

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def for_each(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT, None] = None,
) -> t.Dict[T, T2]: pass


@t.overload
def for_each(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT, None] = None,
) -> t.Dict[T, T2]: pass


@t.overload
def for_each(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
) -> t.Dict[T, T2]: pass


@t.overload
def for_each(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def for_each(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T, int], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def for_each(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


def for_each(collection, iteratee=None):
    """
    Iterates over elements of a collection, executing the iteratee for each element.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        `collection`

    Example:

        >>> results = {}
        >>> def cb(x):
        ...     results[x] = x**2
        >>> for_each([1, 2, 3, 4], cb)
        [1, 2, 3, 4]
        >>> assert results == {1: 1, 2: 4, 3: 9, 4: 16}

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``each``.
    """
    pass


@t.overload
def for_each_right(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT],
) -> t.Dict[T, T2]: pass


@t.overload
def for_each_right(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT],
) -> t.Dict[T, T2]: pass


@t.overload
def for_each_right(
    collection: t.Dict[T, T2],
    iteratee: t.Union[t.Callable[[T2], t.Any], IterateeObjT],
) -> t.Dict[T, T2]: pass


@t.overload
def for_each_right(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT],
) -> t.List[T]: pass


@t.overload
def for_each_right(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T, int], t.Any], IterateeObjT],
) -> t.List[T]: pass


@t.overload
def for_each_right(
    collection: t.List[T],
    iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT],
) -> t.List[T]: pass


def for_each_right(collection, iteratee):
    """
    This method is like :func:`for_each` except that it iterates over elements of a `collection`
    from right to left.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        `collection`

    Example:

        >>> results = {"total": 1}
        >>> def cb(x):
        ...     results["total"] = x * results["total"]
        >>> for_each_right([1, 2, 3, 4], cb)
        [1, 2, 3, 4]
        >>> assert results == {"total": 24}

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``each_right``.
    """
    pass


@t.overload
def group_by(collection: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.Dict[T2, t.List[T]]: pass


@t.overload
def group_by(
    collection: t.Iterable[T], iteratee: t.Union[IterateeObjT, None] = None
) -> t.Dict[t.Any, t.List[T]]: pass


def group_by(collection, iteratee=None):
    """
    Creates an object composed of keys generated from the results of running each element of a
    `collection` through the iteratee.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Results of grouping by `iteratee`.

    Example:

        >>> results = group_by([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], 'a')
        >>> assert results == {1: [{'a': 1, 'b': 2}], 3: [{'a': 3, 'b': 4}]}
        >>> results = group_by([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], {'a': 1})
        >>> assert results == {False: [{'a': 3, 'b': 4}],\
                               True: [{'a': 1, 'b': 2}]}

    .. versionadded:: 1.0.0
    """
    pass


def includes(
    collection: t.Union[t.Sequence[t.Any], t.Dict[t.Any, t.Any]], target: t.Any, from_index: int = 0
) -> bool:
    """
    Checks if a given value is present in a collection. If `from_index` is negative, it is used as
    the offset from the end of the collection.

    Args:
        collection: Collection to iterate over.
        target: Target value to compare to.
        from_index: Offset to start search from.

    Returns:
        Whether `target` is in `collection`.

    Example:

        >>> includes([1, 2, 3, 4], 2)
        True
        >>> includes([1, 2, 3, 4], 2, from_index=2)
        False
        >>> includes({"a": 1, "b": 2, "c": 3, "d": 4}, 2)
        True

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Renamed from ``contains`` to ``includes`` and removed alias
        ``include``.
    """
    pass


def invoke_map(
    collection: t.Iterable[t.Any], path: PathT, *args: t.Any, **kwargs: t.Any
) -> t.List[t.Any]:
    """
    Invokes the method at `path` of each element in `collection`, returning a list of the results of
    each invoked method. Any additional arguments are provided to each invoked method. If `path` is
    a function, it's invoked for each element in `collection`.

    Args:
        collection: Collection to iterate over.
        path: String path to method to invoke or callable to invoke for each element in
            `collection`.
        args: Arguments to pass to method call.
        kwargs: Keyword arguments to pass to method call.

    Returns:
        List of results of invoking method of each item.

    Example:

        >>> items = [{"a": [{"b": 1}]}, {"a": [{"c": 2}]}]
        >>> expected = [{"b": 1}.items(), {"c": 2}.items()]
        >>> invoke_map(items, "a[0].items") == expected
        True

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def key_by(collection: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.Dict[T2, T]: pass


@t.overload
def key_by(
    collection: t.Iterable[t.Any], iteratee: t.Union[IterateeObjT, None] = None
) -> t.Dict[t.Any, t.Any]: pass


def key_by(collection, iteratee=None):
    """
    Creates an object composed of keys generated from the results of running each element of the
    collection through the given iteratee.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Results of indexing by `iteratee`.

    Example:

        >>> results = key_by([{"a": 1, "b": 2}, {"a": 3, "b": 4}], "a")
        >>> assert results == {1: {"a": 1, "b": 2}, 3: {"a": 3, "b": 4}}


    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Renamed from ``index_by`` to ``key_by``.
    """
    pass


@t.overload
def map_(collection: t.Mapping[t.Any, T2], iteratee: t.Callable[[T2], T3]) -> t.List[T3]: pass


@t.overload
def map_(collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T], T3]) -> t.List[T3]: pass


@t.overload
def map_(
    collection: t.Mapping[T, T2], iteratee: t.Callable[[T2, T, t.Dict[T, T2]], T3]
) -> t.List[T3]: pass


@t.overload
def map_(collection: t.Iterable[T], iteratee: t.Callable[[T], T2]) -> t.List[T2]: pass


@t.overload
def map_(collection: t.Iterable[T], iteratee: t.Callable[[T, int], T2]) -> t.List[T2]: pass


@t.overload
def map_(
    collection: t.Iterable[T], iteratee: t.Callable[[T, int, t.List[T]], T2]
) -> t.List[T2]: pass


@t.overload
def map_(
    collection: t.Iterable[t.Any], iteratee: t.Union[IterateeObjT, None] = None
) -> t.List[t.Any]: pass


def map_(collection, iteratee=None):
    """
    Creates an array of values by running each element in the collection through the iteratee. The
    iteratee is invoked with three arguments: ``(value, index|key, collection)``. If a property name
    is passed for iteratee, the created :func:`pluck` style iteratee will return the property value
    of the given element. If an object is passed for iteratee, the created :func:`.matches` style
    iteratee will return ``True`` for elements that have the properties of the given object, else
    ``False``.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.

    Returns:
        Mapped list.

    Example:

        >>> map_([1, 2, 3, 4], str)
        ['1', '2', '3', '4']
        >>> map_([{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}], "a")
        [1, 3, 5]
        >>> map_([[[0, 1]], [[2, 3]], [[4, 5]]], "0.1")
        [1, 3, 5]
        >>> map_([{"a": {"b": 1}}, {"a": {"b": 2}}], "a.b")
        [1, 2]
        >>> map_([{"a": {"b": [0, 1]}}, {"a": {"b": [2, 3]}}], "a.b[1]")
        [1, 3]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``collect``.
    """
    pass


def nest(collection: t.Iterable[t.Any], *properties: t.Any) -> t.Any:
    """
    This method is like :func:`group_by` except that it supports nested grouping by multiple string
    `properties`. If only a single key is given, it is like calling ``group_by(collection, prop)``.

    Args:
        collection: Collection to iterate over.
        *properties: Properties to nest by.

    Returns:
        Results of nested grouping by `properties`.

    Example:

        >>> results = nest([{'shape': 'square', 'color': 'red', 'qty': 5},\
                            {'shape': 'square', 'color': 'blue', 'qty': 10},\
                            {'shape': 'square', 'color': 'orange', 'qty': 5},\
                            {'shape': 'circle', 'color': 'yellow', 'qty': 5},\
                            {'shape': 'circle', 'color': 'pink', 'qty': 10},\
                            {'shape': 'oval', 'color': 'purple', 'qty': 5}],\
                           'shape', 'qty')
        >>> expected = {\
            'square': {5: [{'shape': 'square', 'color': 'red', 'qty': 5},\
                           {'shape': 'square', 'color': 'orange', 'qty': 5}],\
                       10: [{'shape': 'square', 'color': 'blue', 'qty': 10}]},\
            'circle': {5: [{'shape': 'circle', 'color': 'yellow', 'qty': 5}],\
                       10: [{'shape': 'circle', 'color': 'pink', 'qty': 10}]},\
            'oval': {5: [{'shape': 'oval', 'color': 'purple', 'qty': 5}]}}
        >>> results == expected
        True

    .. versionadded:: 4.3.0
    """
    pass


@t.overload
def order_by(
    collection: t.Mapping[t.Any, T2],
    keys: t.Iterable[t.Union[str, int]],
    orders: t.Union[t.Iterable[bool], bool],
    reverse: bool = False,
) -> t.List[T2]: pass


@t.overload
def order_by(
    collection: t.Mapping[t.Any, T2],
    keys: t.Iterable[str],
    orders: None = None,
    reverse: bool = False,
) -> t.List[T2]: pass


@t.overload
def order_by(
    collection: t.Iterable[T],
    keys: t.Iterable[t.Union[str, int]],
    orders: t.Union[t.Iterable[bool], bool],
    reverse: bool = False,
) -> t.List[T]: pass


@t.overload
def order_by(
    collection: t.Iterable[T],
    keys: t.Iterable[str],
    orders: None = None,
    reverse: bool = False,
) -> t.List[T]: pass


def order_by(collection, keys, orders=None, reverse=False):
    """
    This method is like :func:`sort_by` except that it sorts by key names instead of an iteratee
    function. Keys can be sorted in descending order by prepending a ``"-"`` to the key name (e.g.
    ``"name"`` would become ``"-name"``) or by passing a list of boolean sort options via `orders`
    where ``True`` is ascending and ``False`` is descending.

    Args:
        collection: Collection to iterate over.
        keys: List of keys to sort by. By default, keys will be sorted in ascending order. To
            sort a key in descending order, prepend a ``"-"`` to the key name. For example, to sort
            the key value for ``"name"`` in descending order, use ``"-name"``.
        orders: List of boolean sort orders to apply for each key. ``True``
            corresponds to ascending order while ``False`` is descending. Defaults to ``None``.
        reverse (bool, optional): Whether to reverse the sort. Defaults to ``False``.

    Returns:
        Sorted list.

    Example:

        >>> items = [{'a': 2, 'b': 1}, {'a': 3, 'b': 2}, {'a': 1, 'b': 3}]
        >>> results = order_by(items, ['b', 'a'])
        >>> assert results == [{'a': 2, 'b': 1},\
                               {'a': 3, 'b': 2},\
                               {'a': 1, 'b': 3}]
        >>> results = order_by(items, ['a', 'b'])
        >>> assert results == [{'a': 1, 'b': 3},\
                               {'a': 2, 'b': 1},\
                               {'a': 3, 'b': 2}]
        >>> results = order_by(items, ['-a', 'b'])
        >>> assert results == [{'a': 3, 'b': 2},\
                               {'a': 2, 'b': 1},\
                               {'a': 1, 'b': 3}]
        >>> results = order_by(items, ['a', 'b'], [False, True])
        >>> assert results == [{'a': 3, 'b': 2},\
                               {'a': 2, 'b': 1},\
                               {'a': 1, 'b': 3}]

    .. versionadded:: 3.0.0

    .. versionchanged:: 3.2.0
        Added `orders` argument.

    .. versionchanged:: 3.2.0
        Added :func:`sort_by_order` as alias.

    .. versionchanged:: 4.0.0
        Renamed from ``order_by`` to ``order_by`` and removed alias
        ``sort_by_order``.
    """
    pass


@t.overload
def partition(
    collection: t.Mapping[T, T2], predicate: t.Callable[[T2, T, t.Dict[T, T2]], t.Any]
) -> t.List[t.List[T2]]: pass


@t.overload
def partition(
    collection: t.Mapping[T, T2], predicate: t.Callable[[T2, T], t.Any]
) -> t.List[t.List[T2]]: pass


@t.overload
def partition(
    collection: t.Mapping[t.Any, T2], predicate: t.Callable[[T2], t.Any]
) -> t.List[t.List[T2]]: pass


@t.overload
def partition(
    collection: t.Mapping[t.Any, T2], predicate: t.Union[IterateeObjT, None] = None
) -> t.List[t.List[T2]]: pass


@t.overload
def partition(
    collection: t.Iterable[T], predicate: t.Callable[[T, int, t.List[T]], t.Any]
) -> t.List[t.List[T]]: pass


@t.overload
def partition(
    collection: t.Iterable[T], predicate: t.Callable[[T, int], t.Any]
) -> t.List[t.List[T]]: pass


@t.overload
def partition(
    collection: t.Iterable[T], predicate: t.Callable[[T], t.Any]
) -> t.List[t.List[T]]: pass


@t.overload
def partition(
    collection: t.Iterable[T], predicate: t.Union[IterateeObjT, None] = None
) -> t.List[t.List[T]]: pass


def partition(collection, predicate=None):
    """
    Creates an array of elements split into two groups, the first of which contains elements the
    `predicate` returns truthy for, while the second of which contains elements the `predicate`
    returns falsey for. The `predicate` is invoked with three arguments: ``(value, index|key,
    collection)``.

    If a property name is provided for `predicate` the created :func:`pluck` style predicate returns
    the property value of the given element.

    If an object is provided for `predicate` the created :func:`.matches` style predicate returns
    ``True`` for elements that have the properties of the given object, else ``False``.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        List of grouped elements.

    Example:

        >>> partition([1, 2, 3, 4], lambda x: x >= 3)
        [[3, 4], [1, 2]]

    .. versionadded:: 1.1.0
    """
    pass


def pluck(collection: t.Iterable[t.Any], path: PathT) -> t.List[t.Any]:
    """
    Retrieves the value of a specified property from all elements in the collection.

    Args:
        collection: List of dicts.
        path: Collection's path to pluck

    Returns:
        Plucked list.

    Example:

        >>> pluck([{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}], "a")
        [1, 3, 5]
        >>> pluck([[[0, 1]], [[2, 3]], [[4, 5]]], "0.1")
        [1, 3, 5]
        >>> pluck([{"a": {"b": 1}}, {"a": {"b": 2}}], "a.b")
        [1, 2]
        >>> pluck([{"a": {"b": [0, 1]}}, {"a": {"b": [2, 3]}}], "a.b.1")
        [1, 3]
        >>> pluck([{"a": {"b": [0, 1]}}, {"a": {"b": [2, 3]}}], ["a", "b", 1])
        [1, 3]

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Function removed.

    .. versionchanged:: 4.0.1
        Made property access deep.
    """
    pass


@t.overload
def reduce_(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T3, T2, T], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T3, T2], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T3], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T2, T], T2],
    accumulator: None = None,
) -> T2: pass


@t.overload
def reduce_(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2, T2], T2],
    accumulator: None = None,
) -> T2: pass


@t.overload
def reduce_(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T, int], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T2], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T, int], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_(
    collection: t.Iterable[T], iteratee: None = None, accumulator: t.Union[T, None] = None
) -> T: pass


def reduce_(collection, iteratee=None, accumulator=None):
    """
    Reduces a collection to a value which is the accumulated result of running each element in the
    collection through the iteratee, where each successive iteratee execution consumes the return
    value of the previous execution.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        accumulator: Initial value of aggregator. Default is to use the result of
            the first iteration.

    Returns:
        Accumulator object containing results of reduction.

    Example:

        >>> reduce_([1, 2, 3, 4], lambda total, x: total * x)
        24

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed aliases ``foldl`` and ``inject``.
    """
    pass


@t.overload
def reduce_right(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T3, T2, T], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_right(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T3, T2], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_right(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T3], T3],
    accumulator: T3,
) -> T3: pass


@t.overload
def reduce_right(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T2, T], T2],
    accumulator: None = None,
) -> T2: pass


@t.overload
def reduce_right(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2, T2], T2],
    accumulator: None = None,
) -> T2: pass


@t.overload
def reduce_right(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T, int], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_right(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T2], T2],
    accumulator: T2,
) -> T2: pass


@t.overload
def reduce_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T, int], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_right(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> T: pass


@t.overload
def reduce_right(
    collection: t.Iterable[T], iteratee: None = None, accumulator: t.Union[T, None] = None
) -> T: pass


def reduce_right(collection, iteratee=None, accumulator=None):
    """
    This method is like :func:`reduce_` except that it iterates over elements of a `collection` from
    right to left.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        accumulator: Initial value of aggregator. Default is to use the result of
            the first iteration.

    Returns:
        Accumulator object containing results of reduction.

    Example:

        >>> reduce_right([1, 2, 3, 4], lambda total, x: total**x)
        4096

    .. versionadded:: 1.0.0

    .. versionchanged:: 3.2.1
        Fix bug where collection was not reversed correctly.

    .. versionchanged:: 4.0.0
        Removed alias ``foldr``.
    """
    pass


@t.overload
def reductions(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T3, T2, T], T3],
    accumulator: T3,
    from_right: bool = False,
) -> t.List[T3]: pass


@t.overload
def reductions(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T3, T2], T3],
    accumulator: T3,
    from_right: bool = False,
) -> t.List[T3]: pass


@t.overload
def reductions(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T3], T3],
    accumulator: T3,
    from_right: bool = False,
) -> t.List[T3]: pass


@t.overload
def reductions(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T2, T], T2],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T2]: pass


@t.overload
def reductions(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2, T2], T2],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T2]: pass


@t.overload
def reductions(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T]: pass


@t.overload
def reductions(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T, int], T2],
    accumulator: T2,
    from_right: bool = False,
) -> t.List[T2]: pass


@t.overload
def reductions(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T], T2],
    accumulator: T2,
    from_right: bool = False,
) -> t.List[T2]: pass


@t.overload
def reductions(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T2], T2],
    accumulator: T2,
    from_right: bool = False,
) -> t.List[T2]: pass


@t.overload
def reductions(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T, int], T],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T]: pass


@t.overload
def reductions(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T], T],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T]: pass


@t.overload
def reductions(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
    from_right: bool = False,
) -> t.List[T]: pass


@t.overload
def reductions(
    collection: t.Iterable[T],
    iteratee: None = None,
    accumulator: t.Union[T, None] = None,
    from_right: bool = False,
) -> t.List[T]: pass


def reductions(collection, iteratee=None, accumulator=None, from_right=False):
    """
    This function is like :func:`reduce_` except that it returns a list of every intermediate value
    in the reduction operation.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        accumulator: Initial value of aggregator. Default is to use the result of
            the first iteration.

    Returns:
        Results of each reduction operation.

    Example:

        >>> reductions([1, 2, 3, 4], lambda total, x: total * x)
        [2, 6, 24]

    Note:
        The last element of the returned list would be the result of using
        :func:`reduce_`.

    .. versionadded:: 2.0.0
    """
    pass


@t.overload
def reductions_right(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T3, T2, T], T3],
    accumulator: T3,
) -> t.List[T3]: pass


@t.overload
def reductions_right(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T3, T2], T3],
    accumulator: T3,
) -> t.List[T3]: pass


@t.overload
def reductions_right(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T3], T3],
    accumulator: T3,
) -> t.List[T3]: pass


@t.overload
def reductions_right(
    collection: t.Mapping[T, T2],
    iteratee: t.Callable[[T2, T2, T], T2],
    accumulator: None = None,
) -> t.List[T2]: pass


@t.overload
def reductions_right(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Callable[[T2, T2], T2],
    accumulator: None = None,
) -> t.List[T2]: pass


@t.overload
def reductions_right(
    collection: t.Mapping[t.Any, t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> t.List[T]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T, int], T2],
    accumulator: T2,
) -> t.List[T2]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T2, T], T2],
    accumulator: T2,
) -> t.List[T2]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T2], T2],
    accumulator: T2,
) -> t.List[T2]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T, int], T],
    accumulator: None = None,
) -> t.List[T]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[T],
    iteratee: t.Callable[[T, T], T],
    accumulator: None = None,
) -> t.List[T]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[t.Any],
    iteratee: t.Callable[[T], T],
    accumulator: None = None,
) -> t.List[T]: pass


@t.overload
def reductions_right(
    collection: t.Iterable[T], iteratee: None = None, accumulator: t.Union[T, None] = None
) -> t.List[T]: pass


def reductions_right(collection, iteratee=None, accumulator=None):
    """
    This method is like :func:`reductions` except that it iterates over elements of a `collection`
    from right to left.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        accumulator: Initial value of aggregator. Default is to use the result of
            the first iteration.

    Returns:
        Results of each reduction operation.

    Example:

        >>> reductions_right([1, 2, 3, 4], lambda total, x: total**x)
        [64, 4096, 4096]

    Note:
        The last element of the returned list would be the result of using
        :func:`reduce_`.

    .. versionadded:: 2.0.0
    """
    pass


@t.overload
def reject(
    collection: t.Mapping[T, T2],
    predicate: t.Union[t.Callable[[T2, T, t.Dict[T, T2]], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def reject(
    collection: t.Mapping[T, T2],
    predicate: t.Union[t.Callable[[T2, T], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def reject(
    collection: t.Mapping[t.Any, T2],
    predicate: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
) -> t.List[T2]: pass


@t.overload
def reject(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T, int, t.List[T]], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def reject(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T, int], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


@t.overload
def reject(
    collection: t.Iterable[T],
    predicate: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
) -> t.List[T]: pass


def reject(collection, predicate=None):
    """
    The opposite of :func:`filter_` this method returns the elements of a collection that the
    predicate does **not** return truthy for.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        Rejected elements of `collection`.

    Example:

        >>> reject([1, 2, 3, 4], lambda x: x >= 3)
        [1, 2]
        >>> reject([{"a": 0}, {"a": 1}, {"a": 2}], "a")
        [{'a': 0}]
        >>> reject([{"a": 0}, {"a": 1}, {"a": 2}], {"a": 1})
        [{'a': 0}, {'a': 2}]

    .. versionadded:: 1.0.0
    """
    pass


def sample(collection: t.Sequence[T]) -> T:
    """
    Retrieves a random element from a given `collection`.

    Args:
        collection: Collection to iterate over.

    Returns:
        Random element from the given collection.

    Example:

        >>> items = [1, 2, 3, 4, 5]
        >>> results = sample(items)
        >>> assert results in items

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Moved multiple samples functionality to :func:`sample_size`. This
        function now only returns a single random sample.
    """
    pass


def sample_size(collection: t.Sequence[T], n: t.Union[int, None] = None) -> t.List[T]:
    """
    Retrieves list of `n` random elements from a collection.

    Args:
        collection: Collection to iterate over.
        n: Number of random samples to return.

    Returns:
        List of `n` sampled collection values.

    Examples:

        >>> items = [1, 2, 3, 4, 5]
        >>> results = sample_size(items, 2)
        >>> assert len(results) == 2
        >>> assert set(items).intersection(results) == set(results)

    .. versionadded:: 4.0.0
    """
    pass


@t.overload
def shuffle(collection: t.Mapping[t.Any, T]) -> t.List[T]: pass


@t.overload
def shuffle(collection: t.Iterable[T]) -> t.List[T]: pass


def shuffle(collection):
    """
    Creates a list of shuffled values, using a version of the Fisher-Yates shuffle.

    Args:
        collection: Collection to iterate over.

    Returns:
        Shuffled list of values.

    Example:

        >>> items = [1, 2, 3, 4]
        >>> results = shuffle(items)
        >>> assert len(results) == len(items)
        >>> assert set(results) == set(items)

    .. versionadded:: 1.0.0
    """
    pass


def size(collection: t.Sized) -> int:
    """
    Gets the size of the `collection` by returning `len(collection)` for iterable objects.

    Args:
        collection: Collection to iterate over.

    Returns:
        Collection length.

    Example:

        >>> size([1, 2, 3, 4])
        4

    .. versionadded:: 1.0.0
    """
    pass


def some(
    collection: t.Iterable[T], predicate: t.Union[t.Callable[[T], t.Any], None] = None
) -> bool:
    """
    Checks if the predicate returns a truthy value for any element of a collection. The predicate is
    invoked with three arguments: ``(value, index|key, collection)``. If a property name is passed
    for predicate, the created :func:`map_` style predicate will return the property value of the
    given element. If an object is passed for predicate, the created :func:`.matches` style
    predicate will return ``True`` for elements that have the properties of the given object, else
    ``False``.

    Args:
        collection: Collection to iterate over.
        predicate: Predicate applied per iteration.

    Returns:
        Whether any of the elements are truthy.

    Example:

        >>> some([False, True, 0])
        True
        >>> some([False, 0, None])
        False
        >>> some([1, 2, 3, 4], lambda x: x >= 3)
        True
        >>> some([1, 2, 3, 4], lambda x: x == 0)
        False

    .. versionadded:: 1.0.0

    .. versionchanged:: 4.0.0
        Removed alias ``any_``.
    """
    pass


@t.overload
def sort_by(
    collection: t.Mapping[t.Any, T2],
    iteratee: t.Union[t.Callable[[T2], t.Any], IterateeObjT, None] = None,
    reverse: bool = False,
) -> t.List[T2]: pass


@t.overload
def sort_by(
    collection: t.Iterable[T],
    iteratee: t.Union[t.Callable[[T], t.Any], IterateeObjT, None] = None,
    reverse: bool = False,
) -> t.List[T]: pass


def sort_by(collection, iteratee=None, reverse=False):
    """
    Creates a list of elements, sorted in ascending order by the results of running each element in
    a `collection` through the iteratee.

    Args:
        collection: Collection to iterate over.
        iteratee: Iteratee applied per iteration.
        reverse: Whether to reverse the sort. Defaults to ``False``.

    Returns:
        Sorted list.

    Example:

        >>> sort_by({"a": 2, "b": 3, "c": 1})
        [1, 2, 3]
        >>> sort_by({"a": 2, "b": 3, "c": 1}, reverse=True)
        [3, 2, 1]
        >>> sort_by([{"a": 2}, {"a": 3}, {"a": 1}], "a")
        [{'a': 1}, {'a': 2}, {'a': 3}]

    .. versionadded:: 1.0.0
    """
    pass


#
# Utility methods not a part of the main API
#


def itermap(
    collection: t.Iterable[t.Any],
    iteratee: t.Union[t.Callable[..., t.Any], IterateeObjT, None] = None,
) -> t.Generator[t.Any, None, None]:
    """Generative mapper."""
    pass
