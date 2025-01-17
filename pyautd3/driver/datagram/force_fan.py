import ctypes
from collections.abc import Callable

from pyautd3.driver.datagram.with_parallel_threshold import IntoDatagramWithParallelThreshold
from pyautd3.driver.datagram.with_timeout import IntoDatagramWithTimeout
from pyautd3.driver.geometry import Device, Geometry
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import DatagramPtr, GeometryPtr

from .datagram import Datagram


class ForceFan(
    IntoDatagramWithTimeout["ForceFan"],
    IntoDatagramWithParallelThreshold["ForceFan"],
    Datagram,
):
    def __init__(self: "ForceFan", f: Callable[[Device], bool]) -> None:
        super().__init__()

        def f_native(_context: ctypes.c_void_p, geometry_ptr: GeometryPtr, dev_idx: int) -> bool:
            return f(Device(dev_idx, Base().device(geometry_ptr, dev_idx)))

        self._f_native = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, GeometryPtr, ctypes.c_uint16)(f_native)

    def _datagram_ptr(self: "ForceFan", geometry: Geometry) -> DatagramPtr:
        return Base().datagram_force_fan(self._f_native, None, geometry._ptr)  # type: ignore[arg-type]
