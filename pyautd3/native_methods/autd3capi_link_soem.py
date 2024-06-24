# This file is autogenerated
import threading
import ctypes
import os
from pyautd3.native_methods.structs import Vector3, Quaternion, FfiFuture, LocalFfiFuture
from pyautd3.native_methods.autd3capi_driver import LinkBuilderPtr, SyncMode

from enum import IntEnum


class Status(IntEnum):
    Error = 0
    StateChanged = 1
    Lost = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class TimerStrategy(IntEnum):
    Sleep = 0
    BusyWait = 1
    NativeTimer = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class EthernetAdaptersPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class LinkSOEMBuilderPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class LinkRemoteSOEMBuilderPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class ResultLinkRemoteSOEMBuilder(ctypes.Structure):
    _fields_ = [("result", LinkRemoteSOEMBuilderPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultLinkRemoteSOEMBuilder) and self._fields_ == other._fields_ # pragma: no cover
                    


class Singleton(type):
    _instances = {}  # type: ignore
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances: # pragma: no cover
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NativeMethods(metaclass=Singleton):

    def init_dll(self, bin_location: str, bin_prefix: str, bin_ext: str):
        try:
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_link_soem{bin_ext}'))
        except Exception:   # pragma: no cover
            return          # pragma: no cover

        self.dll.AUTDLinkSOEMSetUltrasoundFreq.argtypes = [ctypes.c_uint32] 
        self.dll.AUTDLinkSOEMSetUltrasoundFreq.restype = None

        self.dll.AUTDAUTDLinkSOEMTracingInit.argtypes = [ctypes.c_uint8] 
        self.dll.AUTDAUTDLinkSOEMTracingInit.restype = None

        self.dll.AUTDAdapterPointer.argtypes = [] 
        self.dll.AUTDAdapterPointer.restype = EthernetAdaptersPtr

        self.dll.AUTDAdapterGetSize.argtypes = [EthernetAdaptersPtr]  # type: ignore 
        self.dll.AUTDAdapterGetSize.restype = ctypes.c_uint32

        self.dll.AUTDAdapterGetAdapter.argtypes = [EthernetAdaptersPtr, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDAdapterGetAdapter.restype = None

        self.dll.AUTDAdapterPointerDelete.argtypes = [EthernetAdaptersPtr]  # type: ignore 
        self.dll.AUTDAdapterPointerDelete.restype = None

        self.dll.AUTDLinkSOEM.argtypes = [] 
        self.dll.AUTDLinkSOEM.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithSendCycle.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMWithSendCycle.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithSync0Cycle.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMWithSync0Cycle.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithBufSize.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint32]  # type: ignore 
        self.dll.AUTDLinkSOEMWithBufSize.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithTimerStrategy.argtypes = [LinkSOEMBuilderPtr, TimerStrategy]  # type: ignore 
        self.dll.AUTDLinkSOEMWithTimerStrategy.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithSyncMode.argtypes = [LinkSOEMBuilderPtr, SyncMode]  # type: ignore 
        self.dll.AUTDLinkSOEMWithSyncMode.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithSyncTolerance.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMWithSyncTolerance.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithSyncTimeout.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMWithSyncTimeout.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithIfname.argtypes = [LinkSOEMBuilderPtr, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDLinkSOEMWithIfname.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithStateCheckInterval.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint32]  # type: ignore 
        self.dll.AUTDLinkSOEMWithStateCheckInterval.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMStatusGetMsg.argtypes = [Status, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDLinkSOEMStatusGetMsg.restype = ctypes.c_uint32

        self.dll.AUTDLinkSOEMWithErrHandler.argtypes = [LinkSOEMBuilderPtr, ctypes.c_void_p, ctypes.c_void_p]  # type: ignore 
        self.dll.AUTDLinkSOEMWithErrHandler.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMWithTimeout.argtypes = [LinkSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMWithTimeout.restype = LinkSOEMBuilderPtr

        self.dll.AUTDLinkSOEMIntoBuilder.argtypes = [LinkSOEMBuilderPtr]  # type: ignore 
        self.dll.AUTDLinkSOEMIntoBuilder.restype = LinkBuilderPtr

        self.dll.AUTDLinkRemoteSOEM.argtypes = [ctypes.c_char_p] 
        self.dll.AUTDLinkRemoteSOEM.restype = ResultLinkRemoteSOEMBuilder

        self.dll.AUTDLinkRemoteSOEMWithTimeout.argtypes = [LinkRemoteSOEMBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkRemoteSOEMWithTimeout.restype = LinkRemoteSOEMBuilderPtr

        self.dll.AUTDLinkRemoteSOEMIntoBuilder.argtypes = [LinkRemoteSOEMBuilderPtr]  # type: ignore 
        self.dll.AUTDLinkRemoteSOEMIntoBuilder.restype = LinkBuilderPtr

    def link_soem_set_ultrasound_freq(self, f: int) -> None:
        return self.dll.AUTDLinkSOEMSetUltrasoundFreq(f)

    def autd_link_soem_tracing_init(self, level: int) -> None:
        return self.dll.AUTDAUTDLinkSOEMTracingInit(level)

    def adapter_pointer(self) -> EthernetAdaptersPtr:
        return self.dll.AUTDAdapterPointer()

    def adapter_get_size(self, adapters: EthernetAdaptersPtr) -> ctypes.c_uint32:
        return self.dll.AUTDAdapterGetSize(adapters)

    def adapter_get_adapter(self, adapters: EthernetAdaptersPtr, idx: int, desc: ctypes.Array[ctypes.c_char] | None, name: ctypes.Array[ctypes.c_char] | None) -> None:
        return self.dll.AUTDAdapterGetAdapter(adapters, idx, desc, name)

    def adapter_pointer_delete(self, adapters: EthernetAdaptersPtr) -> None:
        return self.dll.AUTDAdapterPointerDelete(adapters)

    def link_soem(self) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEM()

    def link_soem_with_send_cycle(self, soem: LinkSOEMBuilderPtr, cycle: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithSendCycle(soem, cycle)

    def link_soem_with_sync_0_cycle(self, soem: LinkSOEMBuilderPtr, cycle: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithSync0Cycle(soem, cycle)

    def link_soem_with_buf_size(self, soem: LinkSOEMBuilderPtr, buf_size: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithBufSize(soem, buf_size)

    def link_soem_with_timer_strategy(self, soem: LinkSOEMBuilderPtr, timer_strategy: TimerStrategy) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithTimerStrategy(soem, timer_strategy)

    def link_soem_with_sync_mode(self, soem: LinkSOEMBuilderPtr, mode: SyncMode) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithSyncMode(soem, mode)

    def link_soem_with_sync_tolerance(self, soem: LinkSOEMBuilderPtr, tolerance_ns: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithSyncTolerance(soem, tolerance_ns)

    def link_soem_with_sync_timeout(self, soem: LinkSOEMBuilderPtr, timeout_ns: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithSyncTimeout(soem, timeout_ns)

    def link_soem_with_ifname(self, soem: LinkSOEMBuilderPtr, ifname: bytes) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithIfname(soem, ifname)

    def link_soem_with_state_check_interval(self, soem: LinkSOEMBuilderPtr, interval_ms: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithStateCheckInterval(soem, interval_ms)

    def link_soem_status_get_msg(self, src: Status, dst: ctypes.Array[ctypes.c_char] | None) -> ctypes.c_uint32:
        return self.dll.AUTDLinkSOEMStatusGetMsg(src, dst)

    def link_soem_with_err_handler(self, soem: LinkSOEMBuilderPtr, handler: ctypes.c_void_p | None, context: ctypes.c_void_p | None) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithErrHandler(soem, handler, context)

    def link_soem_with_timeout(self, soem: LinkSOEMBuilderPtr, timeout_ns: int) -> LinkSOEMBuilderPtr:
        return self.dll.AUTDLinkSOEMWithTimeout(soem, timeout_ns)

    def link_soem_into_builder(self, soem: LinkSOEMBuilderPtr) -> LinkBuilderPtr:
        return self.dll.AUTDLinkSOEMIntoBuilder(soem)

    def link_remote_soem(self, addr: bytes) -> ResultLinkRemoteSOEMBuilder:
        return self.dll.AUTDLinkRemoteSOEM(addr)

    def link_remote_soem_with_timeout(self, soem: LinkRemoteSOEMBuilderPtr, timeout_ns: int) -> LinkRemoteSOEMBuilderPtr:
        return self.dll.AUTDLinkRemoteSOEMWithTimeout(soem, timeout_ns)

    def link_remote_soem_into_builder(self, soem: LinkRemoteSOEMBuilderPtr) -> LinkBuilderPtr:
        return self.dll.AUTDLinkRemoteSOEMIntoBuilder(soem)
