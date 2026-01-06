# Heat Transfer Surrogate Model

## Overview
This project builds a machine learning surrogate model for a physics-based heat
transfer system. The surrogate learns the mapping from physical parameters to
temperature outcomes, enabling fast predictions compared to running simulations.
The dataset is to be synthetically generated using a 1D steady-state heat transfer
model with convection on both sides. Input parameters are to be sampled across
physically reasonable ranges to create a diverse training set.

## Physics Model (v1)
1D steady-state heat conduction through a plane wall with convection on both sides.

## Goals
- Generate synthetic data from physics equations.
- Train ML models to predict temperature outcomes.
- Compare accuracy and speed vs. the physics model.
- Perform error analysis and sensitivity to parameters.

## Tools
Python, NumPy, pandas, scikit-learn, matplotlib