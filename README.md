# MLE vs MAP Simulation Project

This project implements simulations to compare the Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP) estimation methods for estimating the bias of a coin based on toss results. The project uses Python for both the calculation of estimations and the visualization of results.

## Features

- **MLE Estimation**: Calculate the maximum likelihood estimation of a coin's bias.
- **MAP Estimation**: Calculate the maximum a posteriori estimation using a predefined Beta distribution as the prior.
- **Visualization**: Visualize the results of the estimations and the Beta distribution.

## Prerequisites

Before you can run the simulations, make sure you have Python installed on your system. The code has been tested with Python 3.12. You also need to have the following Python libraries installed:

- NumPy
- Matplotlib
- SciPy

You can install these packages using pip:

```
pip install -r requirements.txt
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://yourrepositoryurl.com
   ```
2. Navigate to the project directory:
   ```
   cd MLEvsMAP
   ```
3. Install the project (ensure you have `setuptools` installed):
   ```
   pip install -e .
   ```

## Usage

To run a simulation, use the following command from the root of the project:

```
python3.12 -m scripts.run_simulation <alpha> <beta> <theta>
```

Where:

- `<alpha>` is the alpha parameter of the Beta distribution.
- `<beta>` is the beta parameter of the Beta distribution.
- `<theta>` is the true bias of the coin (probability of getting heads).

Example:

```
python3.12 -m scripts.run_simulation 2 100 0.7
```

This command will run the simulation with the specified parameters and display the results.

## Contributing

Contributions to the project are welcome! Please fork the repository and submit a pull request with your features or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or further information, please contact [Your Email or Contact Information].
