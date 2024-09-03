import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def plot_beta(a, b):
    """
    Plot the probability density function of the Beta distribution.

    Parameters:
    a (float): Alpha parameter of the Beta distribution, must be > 0.
    b (float): Beta parameter of the Beta distribution, must be > 0.

    Returns:
    None
    """
    if a <= 0 or b <= 0:
        raise ValueError("Alpha (a) and Beta (b) parameters must be greater than 0.")
    
    # Values on the x-axis (probability of heads θ)
    x = np.linspace(0, 1, 100)
    # Calculate the probability density function for Beta distribution
    y = beta.pdf(x, a, b)
    # Plotting
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'r-', lw=2, alpha=0.6, label=f'Beta PDF with a={a}, b={b}')
    plt.title('Beta Distribution')
    plt.xlabel('Probability of Heads (θ)')
    plt.ylabel('Density')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
