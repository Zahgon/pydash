"""Generic utility methods not part of main API."""

from __future__ import annotations

import builtins
from collections.abc import Hashable, Iterable, Mapping, Sequence
from decimal import Decimal
from functools import wraps
import inspect
import operator
import warnings

import pydash as pyd


#: Singleton object that differentiates between an explicit ``None`` value and an unset value.
#: As a class so it has its own type
class Unset: pass


UNSET = Unset()

#: Tuple of number types.
NUMBER_TYPES = (int, float, Decimal)

#: Dictionary of builtins with keys as the builtin function and values as the string name.
BUILTINS = {value: key for key, value in builtins.__dict__.items() if isinstance(value, Hashable)}

#: Object keys that are restricted from access via path access.
RESTRICTED_KEYS = ("__globals__", "__builtins__")

#: Inspect signature parameter kinds that correspond to positional arguments.
POSITIONAL_PARAMETERS = (
    inspect.Parameter.VAR_POSITIONAL,
    inspect.Parameter.POSITIONAL_ONLY,
    inspect.Parameter.POSITIONAL_OR_KEYWORD,
)


def callit(iteratee, *args, **kwargs):
    """Inspect argspec of `iteratee` function and only pass the supported arguments when calling
    it."""
    pass


def getargcount(iteratee, maxargs):
    """Return argument count of iteratee function."""
    pass


def _getargcount(iteratee, maxargs):
    pass


def iteriteratee(obj, iteratee=None, reverse=False):
    """Return iterative iteratee based on collection type."""
    pass


def iterator(obj):
    """Return iterative based on object type."""
    pass


def base_get(obj, key, default=UNSET):
    """
    Safely get an item by `key` from a sequence or mapping object when `default` provided.

    Args:
        obj: Sequence or mapping to retrieve item from.
        key: Key or index identifying which item to retrieve.
        default: Default value to return if `key` not found in `obj`.

    Returns:
        `obj[key]`, `obj.key`, or `default`.

    Raises:
        KeyError: If `obj` is missing key, index, or attribute and no default value provided.
    """
    pass


def _base_get_dict(obj, key, default=UNSET):
    pass


def _base_get_item(obj, key, default=UNSET):
    pass


def _base_get_object(obj, key, default=UNSET):
    pass


def _raise_if_restricted_key(*keys):
    # Prevent access to restricted keys for security reasons.
    pass


def base_set(obj, key, value, allow_override=True):
    """
    Set an object's `key` to `value`. If `obj` is a ``list`` and the `key` is the next available
    index position, append to list; otherwise, pad the list of ``None`` and then append to the list.

    Args:
        obj: Object to assign value to.
        key: Key or index to assign to.
        value: Value to assign.
        allow_override: Whether to allow overriding a previously set key.
    """
    pass


def cmp(a, b):  # pragma: no cover
    """
    Replacement for built-in function ``cmp`` that was removed in Python 3.

    Note: Mainly used for comparison during sorting.
    """
    pass


def parse_iteratee(iteratee_keyword, *args, **kwargs):
    """Try to find iteratee function passed in either as a keyword argument or as the last
    positional argument in `args`."""
    pass


class iterator_with_default(object):
    """A wrapper around an iterator object that provides a default."""

    def __init__(self, collection, default):
        self.iter = iter(collection)
        self.default = default

    def __iter__(self):
        return self

    def next_default(self):
        pass

    def __next__(self):
        ret = next(self.iter, self.next_default())
        if ret is UNSET:
            raise StopIteration
        return ret

    next = __next__


def deprecated(func):  # pragma: no cover
    """
    This is a decorator which can be used to mark functions as deprecated.

    It will result in a warning being emitted when the function is used.
    """
    pass
