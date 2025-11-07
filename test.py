from signal_and_signalchange import sine_wave, cosine_wave
import numpy as np
import matplotlib.pyplot as plt
from utils import add_unit_step 

def test_1():
    t_sin, signal_sin = sine_wave(freq=5, duration=2)
    assert len(t_sin) == 2000, "Length of time array should be 2000 for 2 seconds at 1000 Hz sampling rate"
    assert np.isclose(signal_sin[0], 0), "First value of sine wave should be 0"
    assert np.isclose(signal_sin[500], 0)

test_1()


def test_2():
    t_cos, signal_cos = cosine_wave(freq=5, duration=2)
    assert len(t_cos) == 2000, "Length of time array should be 2000 for 2 seconds at 1000 Hz sampling rate"
    assert np.isclose(signal_cos[0], 1), "first value of cosine wave should be 1"
    assert np.isclose(signal_cos[500], 0), " value at t=0.5s should be 0"

test_2()