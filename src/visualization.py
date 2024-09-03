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
    plt.xlabel('Theta')
    plt.ylabel('Probability of theta')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# plot the predicted probaiblity against the number of coin tosses.
def plot_predictions(X, theta):
    """
    Plot the predicted probability of the distribution against the number of coin tosses.

    Parameters:
    X (array): Number of coin tosses.
    theta (array): Predicted probability of the distribution.

    Returns:
    None
    """
    plt.figure(figsize=(8, 4))
    plt.plot(X, theta, 'r-', lw=2, alpha=0.6, label='Predicted Probability')
    plt.title('Predicted Probability of the Distribution')
    plt.xlabel('Number of Coin Tosses')
    plt.ylabel('Predicted Probability')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
