# Energy Efficiency Regression

## Overview
This project applies supervised machine learning to predict building heating
load based on geometric and glazing parameters. The goal is to evaluate linear
and nonlinear models and assess their performance using principled validation.

## Dataset
The Energy Efficiency dataset was obtained from the UCI Machine Learning
Repository. It contains 768 simulated building designs with 8 input features
and two target variables: heating load and cooling load.

## Methods
- Exploratory data analysis (EDA)
- Linear regression baseline
- Random Forest regression
- Cross-validation
- Hyperparameter tuning with GridSearchCV

## Results
- Linear Regression: RMSE ≈ 3.0, R² ≈ 0.91.
- Random Forest: RMSE ≈ ~1–1.5, R² ≈ ~0.95+.
- Hyperparameter tuning provided marginal improvement.

## Key Insights
- Building height and compactness strongly influence heating load.
- Nonlinear interactions are important.
- Random Forest improves accuracy but shows higher variance across folds.

## How to Run
1. Create environment:

conda create -n ml python=3.10
conda activate ml
conda install numpy pandas matplotlib scikit-learn jupyter

2. Launch Jupyter:

jupyter notebook

3. Open the notebook in `notebooks/`

## Future Work
- Separate modeling for cooling load
- Additional feature engineering
- Physics-informed constraints