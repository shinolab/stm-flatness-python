from typing import Generic, TypeVar

from forbiddenfruit import curse

from pyautd3.driver.datagram.datagram_tuple import DatagramTuple
from pyautd3.driver.geometry import Geometry
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import DatagramPtr

from .datagram import Datagram

__all__ = []  # type: ignore[var-annotated]

D = TypeVar("D", bound="Datagram")


class DatagramWithParallelThreshold(Datagram, Generic[D]):
    _datagram: D
    _threshold: int

    def __init__(self: "DatagramWithParallelThreshold[D]", datagram: D, threshold: int) -> None:
        self._datagram = datagram
        self._threshold = threshold

    def _datagram_ptr(self: "DatagramWithParallelThreshold[D]", g: Geometry) -> DatagramPtr:
        raw_ptr = self._datagram._datagram_ptr(g)
        return Base().datagram_with_parallel_threshold(raw_ptr, self._threshold)


class IntoDatagramWithParallelThreshold(Generic[D]):
    def with_parallel_threshold(self: D, threshold: int) -> DatagramWithParallelThreshold[D]:
        return DatagramWithParallelThreshold(self, threshold)


def __with_parallel_threshold(self: tuple[Datagram, Datagram], threshold: int) -> DatagramWithParallelThreshold[D]:
    return DatagramWithParallelThreshold(DatagramTuple(self), threshold)


curse(tuple, "with_parallel_threshold", __with_parallel_threshold)
