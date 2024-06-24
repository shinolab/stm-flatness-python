import ctypes
from abc import ABCMeta, abstractmethod
from datetime import timedelta
from typing import Generic, TypeVar

import numpy as np

from pyautd3 import SamplingConfig
from pyautd3.driver.datagram.modulation.modulation import Modulation as _Modulation
from pyautd3.driver.defined.freq import Freq
from pyautd3.driver.geometry.geometry import Geometry
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import ModulationPtr

M = TypeVar("M", bound="Modulation")


class Modulation(_Modulation[M], Generic[M], metaclass=ABCMeta):
    def __init__(self: "Modulation", config: SamplingConfig | Freq[int] | timedelta) -> None:
        super().__init__(config)

    @abstractmethod
    def calc(self: "Modulation", geometry: Geometry) -> np.ndarray:
        pass

    def _modulation_ptr(self: "Modulation", geometry: Geometry) -> ModulationPtr:
        data = self.calc(geometry)
        size = len(data)
        return Base().modulation_raw(
            self._config._inner,
            self._loop_behavior,
            data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),  # type: ignore[arg-type]
            size,
        )
