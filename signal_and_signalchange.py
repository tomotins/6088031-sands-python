#here is my first signal
import numpy as np
import matplotlib.pyplot as plt

def sine_wave(freq=5, duration=1, sampling_rate=1000):

    #Creates a sine wave signal with three variables: frequency, duration, and sampling rate.
        #freq = frequency in Hz
        #duration = duration in seconds
        #sampling_rate = samples per second
    
    t_sin = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) 
        #creates even spaced time values from 0 to duration, 
        # a total of sampling_rate * duration samples are created
    signal_sin = np.sin(2 * np.pi * freq * t_sin)
        #creates the sine wave signal using the formula sin(2πft)
    return t_sin, signal_sin

t_sin, signal_sin = sine_wave(freq=5, duration=2)

# Plot
plt.plot(t_sin, signal_sin, label="Original Sine Signal")

plt.show()

def cosine_wave(freq=5, duration=1, sampling_rate=1000):
    """
    Creates a cosine wave signal with three variables: frequency, duration, and sampling rate.
    
    Input:
        freq (float): frequency in Hz
        duration (float): duration in seconds
        sampling_rate (int): samples per second
        
    Output:
        t_cos (numpy array): time values
        signal_cos (numpy array): cosine wave signal
    """
    t_cos = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False) 
    signal_cos = np.cos(2 * np.pi * freq * t_cos)
    return t_cos, signal_cos

# Generate cosine wave
t_cos, signal_cos = cosine_wave(freq=5, duration=2)

# Plot
plt.figure()
plt.plot(t_cos, signal_cos, label='Cosine Wave')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Cosine Wave")
plt.legend()
plt.grid(True)
plt.show()