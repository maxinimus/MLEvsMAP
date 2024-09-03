
import argparse
import numpy as np
from .run_models import run_experiments
from src import plot_simulation_results

def run_simulation(a, b, theta):
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
    toss_counts, mle_estimates, map_estimates = run_experiments(a, b, theta)

    # Plot the results
    plot_simulation_results(toss_counts, mle_estimates, map_estimates, a, b, theta)

    return None

if __name__ == '__main__':
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Run MLE and MAP estimation simulations for a biased coin.")
    parser.add_argument('a', type=float, help="Alpha parameter of the Beta distribution.")
    parser.add_argument('b', type=float, help="Beta parameter of the Beta distribution.")
    parser.add_argument('theta', type=float, help="True bias of the coin.")

    # Parse arguments
    args = parser.parse_args()

    # Call the simulation function with command-line arguments
    run_simulation(args.a, args.b, args.theta)

