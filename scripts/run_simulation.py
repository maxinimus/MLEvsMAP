import numpy as np

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

    # Sample number of tosses
    toss_counts = [10, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000, 10000]
    heads_counts = [int(tc * theta) for tc in toss_counts]  # Simulating a fair coin

    # Results storage
    mle_estimates = []
    map_estimates = []

    # Run experiments
    for n, h in zip(toss_counts, heads_counts):
        mle_theta = MLE_model(n, h)
        map_theta = MAP_model(n, h, a, b)
        mle_estimates.append(mle_theta)
        map_estimates.append(map_theta)

    return toss_counts, mle_estimates, map_estimates
