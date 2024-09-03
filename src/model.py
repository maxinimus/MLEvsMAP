import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from .utils import validate_coin_tosses

# MLE model
def MLE_model(n, h):
    """
    Maximum Likelihood Estimation (MLE) model for the number of coin tosses.

    Parameters:
    n (int): Number of coin tosses.
    h (int): Number of heads.

    Returns:
    theta (float): Predicted probability of the distribution.
    """
    
    validate_coin_tosses(n, h)

    theta = h / n
    
    return theta

# MAP model
def MAP_model(n, h, a, b):
    """
    Maximum A Posteriori (MAP) model for the number of coin tosses.

    Parameters:
    n (int): Number of coin tosses.
    h (int): Number of heads.
    a (float): Alpha parameter of the Beta distribution, must be > 0.
    b (float): Beta parameter of the Beta distribution, must be > 0.

    Returns:
    theta (float): Predicted probability of the distribution.
    """

    validate_coin_tosses(n, h)

    a_new = a - 1 + h
    b_new = b - 1 + n - h

    theta = a_new / (a_new + b_new)

    return theta
