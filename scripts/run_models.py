import numpy as np
from src import MLE_model, MAP_model

def run_experiments(a,b,theta):
    """
    Generates heads observed in a given number of coin tosses.
    Returns MLE and MAP estimates for the coin's bias.

    Parameters: 
    a (float): Prior Beta distribution parameter.
    b (float): Prior Beta distribution parameter.
    theta (float): True bias of the coin.

    Returns:
    toss_counts (list): Number of coin tosses for each experiment.
    mle_estimates (list): MLE estimates for given theta.
    map_estimates (list): MAP estimates for given theta and prior.
    """

    # Sample number of tosses
    toss_counts = np.array(range(10, 10000, 10))
    # Generate head_counts randomly based on theta
    heads_counts = np.array([np.random.binomial(tc, theta) for tc in toss_counts])

    # Results storage
    mle_estimates = np.zeros(len(toss_counts))
    map_estimates = np.zeros(len(toss_counts))

    # Run experiments
    for i in range(len(toss_counts)):
        n = toss_counts[i]
        h = heads_counts[i]
        mle_theta = MLE_model(n, h)
        map_theta = MAP_model(n, h, a, b)
        mle_estimates[i] = mle_theta
        map_estimates[i] = map_theta 

    return toss_counts, mle_estimates, map_estimates
