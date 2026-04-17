from abc import ABC, abstractmethod
import typing as t


class AllFuncs(ABC):
    """Exposing all of the exposed functions of a module through an class."""

    module: t.Any
    invalid_method_exception: t.Type[Exception]

    @abstractmethod
    def _wrap(self, func) -> t.Callable:
        """Proxy attribute access to :attr:`module`."""
        pass

    @classmethod
    def get_method(cls, name: str) -> t.Callable:
        """
        Return valid :attr:`module` method.

        Args:
            name: Name of pydash method to get.

        Returns:
            :attr:`module` callable.

        Raises:
            InvalidMethod: Raised if `name` is not a valid :attr:`module` method.
        """
        pass

    def __getattr__(self, name: str) -> t.Callable:
        return self._wrap(self.get_method(name))
