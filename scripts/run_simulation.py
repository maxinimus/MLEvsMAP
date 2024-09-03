import numpy as np

from .run_models import run_experiments
from src import plot_beta, plot_predictions

def run_simulation(a,b,theta):
    """
    Runs the simulation for MLE and MAP estimation of a coin's bias.

    Parameters: 
    a (float): Prior Beta distribution parameter.
    b (float): Prior Beta distribution parameter.
    theta (float): True bias of the coin.

    Returns:
    None
    """

    # Generate the results of the experiments
    toss_counts, mle_estimates, map_estimates = run_experiments(a,b,theta)

    # Plot the beta distribution
    plot_beta(a,b)

    # Plot the MLE predicted probability
    plot_predictions(toss_counts, mle_estimates)

    # Plot the MAP predicted probability
    plot_predictions(toss_counts, map_estimates)

    return None

# Run the simulation
run_simulation(1,1,0.5)
