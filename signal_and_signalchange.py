#here is my first signal
import numpy as np
import matplotlib.pyplot as plt

def sine_wave(freq=5, duration=1, sampling_rate=1000):

    #Creates a sine wave signal with three variables: frequency, duration, and sampling rate.
        #freq = frequency in Hz
        #duration = duration in seconds
        #sampling_rate = samples per second
    
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) 
        #creates even spaced time values from 0 to duration, 
        # a total of sampling_rate * duration samples are created
    signal = np.sin(2 * np.pi * freq * t)
        #creates the sine wave signal using the formula sin(2πft)
    return t, signal

t, sig = sine_wave(freq=5, duration=2)

# Plot
plt.plot(t, sig, label="Original Signal")

plt.show()
