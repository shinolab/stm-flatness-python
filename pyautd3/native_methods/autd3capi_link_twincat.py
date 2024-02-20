# This file is autogenerated
import threading
import ctypes
import os
from pyautd3.native_methods.autd3capi_def import LinkBuilderPtr


class LinkTwinCATBuilderPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class LinkRemoteTwinCATBuilderPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class ResultLinkRemoteTwinCATBuilder(ctypes.Structure):
    _fields_ = [("result", LinkRemoteTwinCATBuilderPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


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
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_link_twincat{bin_ext}'))
        except FileNotFoundError:   # pragma: no cover
            return                  # pragma: no cover

        self.dll.AUTDLinkTwinCAT.argtypes = [] 
        self.dll.AUTDLinkTwinCAT.restype = LinkTwinCATBuilderPtr

        self.dll.AUTDLinkTwinCATWithTimeout.argtypes = [LinkTwinCATBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkTwinCATWithTimeout.restype = LinkTwinCATBuilderPtr

        self.dll.AUTDLinkTwinCATIntoBuilder.argtypes = [LinkTwinCATBuilderPtr]  # type: ignore 
        self.dll.AUTDLinkTwinCATIntoBuilder.restype = LinkBuilderPtr

        self.dll.AUTDLinkRemoteTwinCAT.argtypes = [ctypes.c_char_p] 
        self.dll.AUTDLinkRemoteTwinCAT.restype = ResultLinkRemoteTwinCATBuilder

        self.dll.AUTDLinkRemoteTwinCATWithServerIP.argtypes = [LinkRemoteTwinCATBuilderPtr, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDLinkRemoteTwinCATWithServerIP.restype = LinkRemoteTwinCATBuilderPtr

        self.dll.AUTDLinkRemoteTwinCATWithClientAmsNetId.argtypes = [LinkRemoteTwinCATBuilderPtr, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDLinkRemoteTwinCATWithClientAmsNetId.restype = LinkRemoteTwinCATBuilderPtr

        self.dll.AUTDLinkRemoteTwinCATWithTimeout.argtypes = [LinkRemoteTwinCATBuilderPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkRemoteTwinCATWithTimeout.restype = LinkRemoteTwinCATBuilderPtr

        self.dll.AUTDLinkRemoteTwinCATIntoBuilder.argtypes = [LinkRemoteTwinCATBuilderPtr]  # type: ignore 
        self.dll.AUTDLinkRemoteTwinCATIntoBuilder.restype = LinkBuilderPtr

    def link_twin_cat(self) -> LinkTwinCATBuilderPtr:
        return self.dll.AUTDLinkTwinCAT()

    def link_twin_cat_with_timeout(self, twincat: LinkTwinCATBuilderPtr, timeout_ns: int) -> LinkTwinCATBuilderPtr:
        return self.dll.AUTDLinkTwinCATWithTimeout(twincat, timeout_ns)

    def link_twin_cat_into_builder(self, twincat: LinkTwinCATBuilderPtr) -> LinkBuilderPtr:
        return self.dll.AUTDLinkTwinCATIntoBuilder(twincat)

    def link_remote_twin_cat(self, server_ams_net_id: bytes) -> ResultLinkRemoteTwinCATBuilder:
        return self.dll.AUTDLinkRemoteTwinCAT(server_ams_net_id)

    def link_remote_twin_cat_with_server_ip(self, twincat: LinkRemoteTwinCATBuilderPtr, addr: bytes) -> LinkRemoteTwinCATBuilderPtr:
        return self.dll.AUTDLinkRemoteTwinCATWithServerIP(twincat, addr)

    def link_remote_twin_cat_with_client_ams_net_id(self, twincat: LinkRemoteTwinCATBuilderPtr, id: bytes) -> LinkRemoteTwinCATBuilderPtr:
        return self.dll.AUTDLinkRemoteTwinCATWithClientAmsNetId(twincat, id)

    def link_remote_twin_cat_with_timeout(self, twincat: LinkRemoteTwinCATBuilderPtr, timeout_ns: int) -> LinkRemoteTwinCATBuilderPtr:
        return self.dll.AUTDLinkRemoteTwinCATWithTimeout(twincat, timeout_ns)

    def link_remote_twin_cat_into_builder(self, twincat: LinkRemoteTwinCATBuilderPtr) -> LinkBuilderPtr:
        return self.dll.AUTDLinkRemoteTwinCATIntoBuilder(twincat)
