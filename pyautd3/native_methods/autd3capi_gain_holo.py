# This file is autogenerated
import threading
import ctypes
import os
from pyautd3.native_methods.structs import Vector3, Quaternion, FfiFuture, LocalFfiFuture
from pyautd3.native_methods.autd3capi_driver import GainPtr

from enum import IntEnum


class EmissionConstraintTag(IntEnum):
    Normalize = 1
    Uniform = 2
    Multiply = 3
    Clamp = 4

    @classmethod
    def from_param(cls, obj):
        return int(obj)  # pragma: no cover


class BackendPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class EmissionConstraintValue(ctypes.Union):
    _fields_ = [("null", ctypes.c_uint8), ("uniform", ctypes.c_uint8), ("multiply", ctypes.c_float), ("clamp", ctypes.c_uint8 * 2)]


class EmissionConstraintWrap(ctypes.Structure):
    _fields_ = [("tag", ctypes.c_uint8), ("value", EmissionConstraintValue)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, EmissionConstraintWrap) and self._fields_ == other._fields_ # pragma: no cover
                    

class ResultBackend(ctypes.Structure):
    _fields_ = [("result", BackendPtr), ("err_len", ctypes.c_uint32), ("err", ctypes.c_void_p)]


    def __eq__(self, other: object) -> bool:
        return isinstance(other, ResultBackend) and self._fields_ == other._fields_ # pragma: no cover
                    


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
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_gain_holo{bin_ext}'))
        except Exception:   # pragma: no cover
            return          # pragma: no cover

        self.dll.AUTDGainHoloConstraintNormalize.argtypes = [] 
        self.dll.AUTDGainHoloConstraintNormalize.restype = EmissionConstraintWrap

        self.dll.AUTDGainHoloConstraintUniform.argtypes = [ctypes.c_uint8] 
        self.dll.AUTDGainHoloConstraintUniform.restype = EmissionConstraintWrap

        self.dll.AUTDGainHoloConstraintMultiply.argtypes = [ctypes.c_float] 
        self.dll.AUTDGainHoloConstraintMultiply.restype = EmissionConstraintWrap

        self.dll.AUTDGainHoloConstraintClamp.argtypes = [ctypes.c_uint8, ctypes.c_uint8] 
        self.dll.AUTDGainHoloConstraintClamp.restype = EmissionConstraintWrap

        self.dll.AUTDGainHoloGreedySphere.argtypes = [ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint8, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGreedySphere.restype = GainPtr

        self.dll.AUTDGainHoloGreedyT4010A1.argtypes = [ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint8, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGreedyT4010A1.restype = GainPtr

        self.dll.AUTDGainGreedyIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainGreedyIsDefault.restype = ctypes.c_bool

        self.dll.AUTDGainHoloGSSphere.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGSSphere.restype = GainPtr

        self.dll.AUTDGainHoloGST4010A1.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGST4010A1.restype = GainPtr

        self.dll.AUTDGainGSIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainGSIsDefault.restype = ctypes.c_bool

        self.dll.AUTDGainHoloGSPATSphere.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGSPATSphere.restype = GainPtr

        self.dll.AUTDGainHoloGSPATT4010A1.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloGSPATT4010A1.restype = GainPtr

        self.dll.AUTDGainGSPATIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainGSPATIsDefault.restype = ctypes.c_bool

        self.dll.AUTDGainHoloSPLToPascal.argtypes = [ctypes.c_float] 
        self.dll.AUTDGainHoloSPLToPascal.restype = ctypes.c_float

        self.dll.AUTDGainHoloPascalToSPL.argtypes = [ctypes.c_float] 
        self.dll.AUTDGainHoloPascalToSPL.restype = ctypes.c_float

        self.dll.AUTDGainHoloLMSphere.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint32, ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloLMSphere.restype = GainPtr

        self.dll.AUTDGainHoloLMT4010A1.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_uint32, ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloLMT4010A1.restype = GainPtr

        self.dll.AUTDGainLMIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainLMIsDefault.restype = ctypes.c_bool

        self.dll.AUTDGainHoloNaiveSphere.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloNaiveSphere.restype = GainPtr

        self.dll.AUTDGainHoloNaiveT4010A1.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloNaiveT4010A1.restype = GainPtr

        self.dll.AUTDGainNaiveIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainNaiveIsDefault.restype = ctypes.c_bool

        self.dll.AUTDNalgebraBackendSphere.argtypes = [] 
        self.dll.AUTDNalgebraBackendSphere.restype = BackendPtr

        self.dll.AUTDNalgebraBackendT4010A1.argtypes = [] 
        self.dll.AUTDNalgebraBackendT4010A1.restype = BackendPtr

        self.dll.AUTDDeleteNalgebraBackendSphere.argtypes = [BackendPtr]  # type: ignore 
        self.dll.AUTDDeleteNalgebraBackendSphere.restype = None

        self.dll.AUTDDeleteNalgebraBackendT4010A1.argtypes = [BackendPtr]  # type: ignore 
        self.dll.AUTDDeleteNalgebraBackendT4010A1.restype = None

        self.dll.AUTDGainHoloSDPSphere.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloSDPSphere.restype = GainPtr

        self.dll.AUTDGainHoloSDPT4010A1.argtypes = [BackendPtr, ctypes.POINTER(Vector3), ctypes.POINTER(ctypes.c_float), ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_uint32, EmissionConstraintWrap]  # type: ignore 
        self.dll.AUTDGainHoloSDPT4010A1.restype = GainPtr

        self.dll.AUTDGainSDPIsDefault.argtypes = [GainPtr]  # type: ignore 
        self.dll.AUTDGainSDPIsDefault.restype = ctypes.c_bool

    def gain_holo_constraint_normalize(self) -> EmissionConstraintWrap:
        return self.dll.AUTDGainHoloConstraintNormalize()

    def gain_holo_constraint_uniform(self, intensity: int) -> EmissionConstraintWrap:
        return self.dll.AUTDGainHoloConstraintUniform(intensity)

    def gain_holo_constraint_multiply(self, v: float) -> EmissionConstraintWrap:
        return self.dll.AUTDGainHoloConstraintMultiply(v)

    def gain_holo_constraint_clamp(self, min_v: int, max_v: int) -> EmissionConstraintWrap:
        return self.dll.AUTDGainHoloConstraintClamp(min_v, max_v)

    def gain_holo_greedy_sphere(self, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, div: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGreedySphere(points, amps, size, div, constraint)

    def gain_holo_greedy_t_4010_a_1(self, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, div: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGreedyT4010A1(points, amps, size, div, constraint)  # pragma: no cover

    def gain_greedy_is_default(self, greedy: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainGreedyIsDefault(greedy)

    def gain_holo_gs_sphere(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGSSphere(backend, points, amps, size, repeat, constraint)

    def gain_holo_gst_4010_a_1(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGST4010A1(backend, points, amps, size, repeat, constraint)  # pragma: no cover

    def gain_gs_is_default(self, gs: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainGSIsDefault(gs)

    def gain_holo_gspat_sphere(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGSPATSphere(backend, points, amps, size, repeat, constraint)

    def gain_holo_gspatt_4010_a_1(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloGSPATT4010A1(backend, points, amps, size, repeat, constraint)  # pragma: no cover

    def gain_gspat_is_default(self, gs: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainGSPATIsDefault(gs)

    def gain_holo_spl_to_pascal(self, value: float) -> ctypes.c_float:
        return self.dll.AUTDGainHoloSPLToPascal(value)

    def gain_holo_pascal_to_spl(self, value: float) -> ctypes.c_float:
        return self.dll.AUTDGainHoloPascalToSPL(value)

    def gain_holo_lm_sphere(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, eps_1: float, eps_2: float, tau: float, k_max: int, initial_ptr: ctypes.Array[ctypes.c_float] | None, initial_len: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloLMSphere(backend, points, amps, size, eps_1, eps_2, tau, k_max, initial_ptr, initial_len, constraint)

    def gain_holo_lmt_4010_a_1(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, eps_1: float, eps_2: float, tau: float, k_max: int, initial_ptr: ctypes.Array[ctypes.c_float] | None, initial_len: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloLMT4010A1(backend, points, amps, size, eps_1, eps_2, tau, k_max, initial_ptr, initial_len, constraint)  # pragma: no cover

    def gain_lm_is_default(self, gs: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainLMIsDefault(gs)

    def gain_holo_naive_sphere(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloNaiveSphere(backend, points, amps, size, constraint)

    def gain_holo_naive_t_4010_a_1(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloNaiveT4010A1(backend, points, amps, size, constraint)  # pragma: no cover

    def gain_naive_is_default(self, gs: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainNaiveIsDefault(gs)

    def nalgebra_backend_sphere(self) -> BackendPtr:
        return self.dll.AUTDNalgebraBackendSphere()

    def nalgebra_backend_t_4010_a_1(self) -> BackendPtr:
        return self.dll.AUTDNalgebraBackendT4010A1()  # pragma: no cover

    def delete_nalgebra_backend_sphere(self, backend: BackendPtr) -> None:
        return self.dll.AUTDDeleteNalgebraBackendSphere(backend)

    def delete_nalgebra_backend_t_4010_a_1(self, backend: BackendPtr) -> None:
        return self.dll.AUTDDeleteNalgebraBackendT4010A1(backend)  # pragma: no cover

    def gain_holo_sdp_sphere(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, alpha: float, lambda_: float, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloSDPSphere(backend, points, amps, size, alpha, lambda_, repeat, constraint)

    def gain_holo_sdpt_4010_a_1(self, backend: BackendPtr, points: ctypes.Array | None, amps: ctypes.Array[ctypes.c_float] | None, size: int, alpha: float, lambda_: float, repeat: int, constraint: EmissionConstraintWrap) -> GainPtr:
        return self.dll.AUTDGainHoloSDPT4010A1(backend, points, amps, size, alpha, lambda_, repeat, constraint)  # pragma: no cover

    def gain_sdp_is_default(self, gs: GainPtr) -> ctypes.c_bool:
        return self.dll.AUTDGainSDPIsDefault(gs)
