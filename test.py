# imports and stuff
import numpy as np
from signal_and_signalchange import sine_wave, cosine_wave
from utils import add_unit_step  # not really using this rn but whatever


# testing sine wave
def test_sine_wave():
    # make a 5hz sine for 2 sec
    t, signal = sine_wave(freq=5, duration=2)

    # should be 2000 samples cuz 2 sec * 1000hz sample rate
    assert len(t) == 2000, "wrong length?? should be 2000"

    # sine starts at 0 i think
    assert np.isclose(signal[0], 0, atol=1e-8), "first value not zero lol"

    # at 0.5 sec it should hit 0 again
    idx = int(0.5 * 1000)
    assert np.isclose(signal[idx], 0, atol=1e-8), "value at 0.5s should probly be 0"


# testing cosine wave
def test_cosine_wave():
    # same idea but cosine
    t, signal = cosine_wave(freq=5, duration=2)

    # check number of samples
    assert len(t) == 2000, "wrong length again"

    # cosine starts at 1
    assert np.isclose(signal[0], 1, atol=1e-8), "first value should be 1 idk why not"

    # at 0.5 sec it should be 0
    idx = int(0.5 * 1000)
    assert np.isclose(signal[idx], 0, atol=1e-8), "cosine at 0.5s should be zero i think"


# i guess you run this with pytest or whatever
# pytest -v  (if it even works)
