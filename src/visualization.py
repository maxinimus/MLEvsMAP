import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

from .utils import validate_beta_params

def plot_beta(a, b, ax):
    """
    Plot the probability density function of the Beta distribution.

    Parameters:
    a (float): Alpha parameter of the Beta distribution, must be > 0.
    b (float): Beta parameter of the Beta distribution, must be > 0.
    ax (matplotlib axes object): The axis to plot on.

    Returns:
    None
    """

    validate_beta_params(a, b)

    x = np.linspace(0, 1, 100)
    y = beta.pdf(x, a, b)
    ax.plot(x, y, 'r-', lw=2, alpha=0.6)
    ax.set_title('Beta Distribution')
    ax.set_xlabel('Theta')
    ax.set_ylabel('Probability of Theta')

# plot the predicted probaiblity against the number of coin tosses.
def plot_predictions(X, theta, ax, title):
    """
    Plot the predicted probability of the distribution against the number of coin tosses.

    Parameters:
    X (array): Number of coin tosses.
    theta (array): Predicted probability of the distribution.
    ax (matplotlib axes object): The axis to plot on.
    title (str): The title of the plot.

    Returns:
    None
    """

    ax.plot(X, theta, 'b-', lw=2, alpha=0.6)
    ax.set_title(title)
    ax.set_xlabel('Number of Coin Tosses')
    ax.set_ylabel('Predicted Probability')
    ax.set_ylim(0.0, 1.0)  # Set y-axis limits from 0.0 to 1.0

def plot_simulation_results(toss_counts, mle_estimates, map_estimates, a, b, theta):
    """
    Plot the results of the simulation.

    Parameters:
    toss_counts (array): Number of coin tosses for each experiment.
    mle_estimates (array): MLE estimates for given theta.
    map_estimates (array): MAP estimates for given theta and prior.

    Returns:
    None
    """

    # Setup the figure and axes
    fig, axs = plt.subplots(3, 1, figsize=(15, 9))

    # Plot the beta distribution
    plot_beta(a, b, axs[0])

    # Plot the MLE predicted probability
    plot_predictions(toss_counts, mle_estimates, axs[1], 'MLE Predictions')

    # Plot the MAP predicted probability
    plot_predictions(toss_counts, map_estimates, axs[2], 'MAP Predictions')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust horizontal space
    plt.show()
