from abc import ABCMeta, abstractmethod


class Observable(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def subscribe(self, observer=None, scheduler=None):
        raise NotImplementedError
