# Heat Transfer Surrogate Model

## Overview
This project builds a machine learning surrogate model for a physics-based heat
transfer system. The surrogate learns the mapping from physical parameters to
temperature outcomes, enabling fast predictions compared to running simulations.
The dataset is to be synthetically generated using a 1D steady-state heat transfer
model with convection on both sides. Input parameters are to be sampled across
physically reasonable ranges to create a diverse training set.

## Physics Model (v1)
The ground-truth model is a steady-state thermal resistance network consisting of
conduction through a plane wall with convection on both sides. Heat flux is
computed analytically and used as the target for surrogate training.

## Goals
- Generate synthetic data from physics equations.
- Train ML models to predict temperature outcomes.
- Compare accuracy and speed vs. the physics model.
- Perform error analysis and sensitivity to parameters.

## Tools
Python, NumPy, pandas, scikit-learn, matplotlib

## Methods
- Physics-based synthetic data generation
- Linear regression baseline surrogate
- Nonlinear Random Forest surrogate
- Train/test evaluation and cross-validation
- Error diagnostics and visualization
- Feature importance analysis
- One-at-a-time sensitivity analysis

## Results
- Linear regression captures global trends but exhibits structured error
- Random Forest surrogate significantly reduces RMSE and error curvature
- Feature importance aligns with thermal resistance theory
- Cross-validation confirms strong generalization

## Key Insights
- Temperature difference and convection coefficients dominate heat flux
- Model expressiveness is critical for inverse resistance relationships
- Surrogate models can approximate physics accurately while enabling fast evaluation

## How to Run
1. Create environment:

conda create -n ml python=3.10
conda activate ml
conda install numpy pandas matplotlib scikit-learn jupyter

2. Generate dataset:

python projects/02-heat-transfer-surrogate/src/simulate.py

3. Launch Jupyter and open the notebook in `notebooks/`

## Future Work
- Multi-output surrogates (surface temperatures)
- Regime-specific modeling (conduction-limited vs convection-limited)
- Physics-informed feature engineering