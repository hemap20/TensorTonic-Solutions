import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    if isinstance(x, float):
        sig = 1/(1+math.exp(-x))
        return sig
    else:
        num_arr = np.array(x)
        exp_arr = np.exp(-num_arr)
        sig_arr = 1/(1+exp_arr)
        return sig_arr
    pass