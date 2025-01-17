from typing import TYPE_CHECKING

import numpy as np

from pyautd3 import Controller, Segment
from pyautd3.driver.defined.freq import Hz
from pyautd3.modulation import Mixer, Sine
from tests.test_autd import create_controller

if TYPE_CHECKING:
    from pyautd3.link.audit import Audit


def test_mixer_exact():
    autd: Controller[Audit]
    with create_controller() as autd:
        m = Mixer(Sine(x * Hz) for x in [50, 100, 150, 200, 250])
        autd.send(m)

        for dev in autd.geometry:
            mod = autd.link.modulation(dev.idx, Segment.S0)
            mod_expect = [
                7,
                21,
                46,
                81,
                115,
                138,
                137,
                113,
                75,
                38,
                13,
                2,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                3,
                4,
                4,
                3,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                3,
                6,
                8,
                7,
                5,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                2,
                2,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ]
            assert np.array_equal(mod, mod_expect)
            assert autd.link.modulation_frequency_division(dev.idx, Segment.S0) == 5120


def test_mixer_exact_float():
    autd: Controller[Audit]
    with create_controller() as autd:
        m = Mixer(Sine(x * Hz) for x in [50.0, 100.0, 150.0, 200.0, 250.0])
        autd.send(m)

        for dev in autd.geometry:
            mod = autd.link.modulation(dev.idx, Segment.S0)
            mod_expect = [
                7,
                21,
                46,
                81,
                115,
                138,
                137,
                113,
                75,
                38,
                13,
                2,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                3,
                4,
                4,
                3,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                3,
                6,
                8,
                7,
                5,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                2,
                2,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
            ]
            assert np.array_equal(mod, mod_expect)
            assert autd.link.modulation_frequency_division(dev.idx, Segment.S0) == 5120


def test_mixer_nearest():
    autd: Controller[Audit]
    with create_controller() as autd:
        m = Mixer([Sine.from_freq_nearest(50.0 * Hz), Sine.from_freq_nearest(100.0 * Hz)])
        autd.send(m)

        for dev in autd.geometry:
            mod = autd.link.modulation(dev.idx, Segment.S0)
            mod_expect = [
                63,
                78,
                95,
                113,
                131,
                149,
                166,
                183,
                196,
                208,
                217,
                222,
                223,
                223,
                217,
                208,
                196,
                182,
                164,
                146,
                127,
                106,
                87,
                67,
                50,
                35,
                22,
                12,
                5,
                0,
                0,
                0,
                4,
                9,
                17,
                25,
                33,
                42,
                50,
                57,
                63,
                67,
                69,
                70,
                69,
                66,
                62,
                56,
                50,
                43,
                37,
                29,
                23,
                17,
                11,
                7,
                4,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                3,
                6,
                11,
                17,
                26,
                36,
                49,
            ]
            assert np.array_equal(mod, mod_expect)
            assert autd.link.modulation_frequency_division(dev.idx, Segment.S0) == 5120
