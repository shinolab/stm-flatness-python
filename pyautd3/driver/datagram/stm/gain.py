import ctypes
from collections.abc import Iterable

import numpy as np

from pyautd3.driver.datagram.datagram import Datagram
from pyautd3.driver.datagram.gain.base import GainBase
from pyautd3.driver.datagram.with_segment_transition import DatagramST, IntoDatagramWithSegmentTransition
from pyautd3.driver.defined.freq import Freq
from pyautd3.driver.firmware.fpga import LoopBehavior
from pyautd3.driver.geometry import Geometry
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import (
    DatagramPtr,
    GainPtr,
    GainSTMMode,
    GainSTMPtr,
    SamplingConfigWrap,
    Segment,
    TransitionModeWrap,
)
from pyautd3.native_methods.autd3capi_driver import LoopBehavior as _LoopBehavior

__all__ = []  # type: ignore[var-annotated]


class GainSTM(
    IntoDatagramWithSegmentTransition,
    DatagramST[GainSTMPtr],
    Datagram,
):
    _gains: list[GainBase]
    _mode: GainSTMMode

    _freq: Freq[float] | None
    _freq_nearest: Freq[float] | None
    _sampling_config: SamplingConfigWrap | None
    _loop_behavior: _LoopBehavior

    def __new__(cls: type["GainSTM"]) -> "GainSTM":
        raise NotImplementedError

    @classmethod
    def __private_new__(
        cls: type["GainSTM"],
        freq: Freq[float] | None,
        freq_nearest: Freq[float] | None,
        sampling_config: SamplingConfigWrap | None,
    ) -> "GainSTM":
        ins = super().__new__(cls)

        ins._gains = []
        ins._mode = GainSTMMode.PhaseIntensityFull

        ins._freq = freq
        ins._freq_nearest = freq_nearest
        ins._sampling_config = sampling_config

        ins._loop_behavior = LoopBehavior.Infinite

        return ins

    def _raw_ptr(self: "GainSTM", geometry: Geometry) -> GainSTMPtr:
        gains: np.ndarray = np.ndarray(len(self._gains), dtype=GainPtr)
        for i, g in enumerate(self._gains):
            gains[i]["_0"] = g._gain_ptr(geometry)._0
        ptr: GainSTMPtr
        if self._freq is not None:
            ptr = Base().stm_gain_from_freq(self._freq.hz)
        elif self._freq_nearest is not None:
            ptr = Base().stm_gain_from_freq_nearest(self._freq_nearest.hz)
        else:
            ptr = Base().stm_gain_from_sampling_config(self._sampling_config)  # type: ignore[arg-type]
        ptr = Base().stm_gain_with_mode(ptr, self._mode)
        ptr = Base().stm_gain_with_loop_behavior(ptr, self._loop_behavior)
        return Base().stm_gain_add_gains(
            ptr,
            gains.ctypes.data_as(ctypes.POINTER(GainPtr)),  # type: ignore[arg-type]
            len(self._gains),
        )

    def _datagram_ptr(self: "GainSTM", geometry: Geometry) -> DatagramPtr:
        return Base().stm_gain_into_datagram(self._raw_ptr(geometry))

    def _into_segment_transition(self: "GainSTM", ptr: GainSTMPtr, segment: Segment, transition_mode: TransitionModeWrap | None) -> DatagramPtr:
        if transition_mode is None:
            return Base().stm_gain_into_datagram_with_segment(ptr, segment)
        return Base().stm_gain_into_datagram_with_segment_transition(ptr, segment, transition_mode)

    @staticmethod
    def from_freq(freq: Freq[float]) -> "GainSTM":
        return GainSTM.__private_new__(freq, None, None)

    @staticmethod
    def from_freq_nearest(freq: Freq[float]) -> "GainSTM":
        return GainSTM.__private_new__(None, freq, None)

    @staticmethod
    def from_sampling_config(config: SamplingConfigWrap) -> "GainSTM":
        return GainSTM.__private_new__(None, None, config)

    def add_gain(self: "GainSTM", gain: GainBase) -> "GainSTM":
        self._gains.append(gain)
        return self

    def add_gains_from_iter(self: "GainSTM", iterable: Iterable[GainBase]) -> "GainSTM":
        self._gains.extend(iterable)
        return self

    def with_mode(self: "GainSTM", mode: GainSTMMode) -> "GainSTM":
        self._mode = mode
        return self

    @property
    def mode(self: "GainSTM") -> GainSTMMode:
        return self._mode

    def with_loop_behavior(self: "GainSTM", value: _LoopBehavior) -> "GainSTM":
        self._loop_behavior = value
        return self
