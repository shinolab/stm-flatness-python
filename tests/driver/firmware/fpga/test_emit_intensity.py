import pytest

from pyautd3 import EmitIntensity


def test_emit_intensity():
    for i in range(256):
        intensity = EmitIntensity(i)
        assert intensity.value == i
        assert str(intensity) == f"EmitIntensity({i})"

    with pytest.raises(TypeError):
        _ = EmitIntensity(0.0)  # type: ignore[arg-type]


def test_emit_intensity_min_max():
    assert EmitIntensity.minimum().value == 0x00
    assert EmitIntensity.maximum().value == 0xFF