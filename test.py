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
    sin_signal = np.sin(t)
    assert len(sin_signal) == 2000, "Length of time array should be 2000 for 2 seconds at 1000 Hz sampling rate"
    assert np.isclose(sin_signal[0], 0), "First value of sine wave should be 0"
    assert np.isclose(sin_signal[500], 0)

test_2()

def test_3():
    t_cos, signal_cos = cosine_wave(freq=5, duration=2)
    assert len(t_cos) == 2000, "Length of time array should be 2000 for 2 seconds at 1000 Hz sampling rate"
    assert np.isclose(signal_cos[0], 0), "First value of sine wave should be 0"
    assert np.isclose(signal_cos[500], 0)

test_3()