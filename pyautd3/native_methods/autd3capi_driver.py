# This file is autogenerated
import threading
import ctypes
import os
from pyautd3.native_methods.structs import Vector3, Quaternion, FfiFuture, LocalFfiFuture, SamplingConfig
from enum import IntEnum


class SyncMode(IntEnum):
    FreeRun = 0
    DC = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class GainSTMMode(IntEnum):
    PhaseIntensityFull = 0
    PhaseFull = 1
    PhaseHalf = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class DebugTypeTag(IntEnum):
    None_ = 0
    BaseSignal = 1
    Thermo = 2
    ForceFan = 3
    Sync = 4
    ModSegment = 5
    ModIdx = 6
    StmSegment = 7
    StmIdx = 8
    IsStmMode = 9
    PwmOut = 10
    Direct = 11

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class GPIOIn(IntEnum):
    I0 = 0
    I1 = 1
    I2 = 2
    I3 = 3

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class GPIOOut(IntEnum):
    O0 = 0
    O1 = 1
    O2 = 2
    O3 = 3

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class Segment(IntEnum):
    S0 = 0
    S1 = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class SilencerTarget(IntEnum):
    Intensity = 0
    PulseWidth = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class TransitionModeTag(IntEnum):
    SyncIdx = 0
    SysTime = 1
    Gpio = 2
    Ext = 3
    Immediate = 4

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class ConstPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class LinkBuilderPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class LinkPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class DatagramPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class GainPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class GeometryPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class DevicePtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class TransducerPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class ModulationPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class FociSTMPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class GainSTMPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class DebugTypeWrap(ctypes.Structure):
    _fields_ = [("ty", ctypes.c_uint8), ("value", ctypes.c_uint16)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, DebugTypeWrap) and self._fields_ == other._fields_ # pragma: no cover
                    

class Drive(ctypes.Structure):
    _fields_ = [("phase", ctypes.c_uint8), ("intensity", ctypes.c_uint8)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, Drive) and self._fields_ == other._fields_ # pragma: no cover
                    

class LoopBehavior(ctypes.Structure):
    _fields_ = [("rep", ctypes.c_uint16)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, LoopBehavior) and self._fields_ == other._fields_ # pragma: no cover
                    

class TransitionModeWrap(ctypes.Structure):
    _fields_ = [("tag", ctypes.c_uint8), ("value", ctypes.c_uint64)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, TransitionModeWrap) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultDatagram(ctypes.Structure):
    _fields_ = [("result", DatagramPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultDatagram) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultModulation(ctypes.Structure):
    _fields_ = [("result", ModulationPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultModulation) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultFociSTM(ctypes.Structure):
    _fields_ = [("result", FociSTMPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultFociSTM) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultGainSTM(ctypes.Structure):
    _fields_ = [("result", GainSTMPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultGainSTM) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultI32(ctypes.Structure):
    _fields_ = [("result", ctypes.c_int32), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultI32) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultSamplingConfig(ctypes.Structure):
    _fields_ = [("result", SamplingConfig), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultSamplingConfig) and self._fields_ == other._fields_ # pragma: no cover
                    

NUM_TRANS_IN_UNIT: int = 249

NUM_TRANS_IN_X: int = 18

NUM_TRANS_IN_Y: int = 14

TRANS_SPACING_MM: float = 10.16

DEVICE_HEIGHT_MM: float = 151.4

DEVICE_WIDTH_MM: float = 192.0

AUTD3_ERR: int = -1

AUTD3_TRUE: int = 1

AUTD3_FALSE: int = 0

