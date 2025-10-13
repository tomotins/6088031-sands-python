
import numpy as np

def add_unit_step(signal, t, step_time=0):
    """
    Adds a unit step function to a given signal.

    Parameters
    
    signal : np.ndarray
        The input sinusoidal signal (e.g., np.sin(t)).
    t : np.ndarray
        The time array corresponding to the signal.
    step_time : float, optional
        The time at which the step function starts (default: 0).

    Returns

    np.ndarray
        The resulting signal after adding the unit step.
    """
    step = np.heaviside(t - step_time, 1)  # 1 means the value at t=step_time is 1
    return signal + step
