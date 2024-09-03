import numpy as np

from .run_models import run_experiments
from src import plot_simulation_results

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

    # Plot the results
    plot_simulation_results(toss_counts, mle_estimates, map_estimates, a, b, theta)

    return None

a = 2
b = 100
theta = 0.5
run_simulation(a,b,theta)
