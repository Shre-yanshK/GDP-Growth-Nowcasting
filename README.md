# GDP Growth Nowcasting Using Statistical Machine Learning

## Project Overview

This project explores the prediction of GDP growth using economic indicators and statistical modelling techniques. It compares alternative Ordinary Least Squares (OLS) regression models and examines how information criteria can support model selection and predictive performance.

Completed as part of the **Statistical Machine Learning (ECON5129)** course at the University of Glasgow, the project applies exhaustive best subset selection and evaluates alternative model specifications using mean squared error (MSE).

**Note:** The dataset used in this exercise is simulated.

## Objectives

- Explore the relationship between economic indicators and GDP growth.
- Implement OLS regression for prediction.
- Apply exhaustive best subset selection across alternative predictor combinations.
- Compare models selected using Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC).
- Evaluate predictive performance using mean squared error.
- Examine the trade-off between model complexity and predictive accuracy.

## Methodology

1. **Data preparation:** Load and examine the training and test datasets.
2. **OLS regression:** Estimate a full regression model using the available predictors.
3. **Best subset selection:** Evaluate alternative combinations of predictors.
4. **Model selection:** Identify candidate specifications using AIC and BIC.
5. **Predictive evaluation:** Compare model performance using MSE.
6. **Final model:** Use the selected BIC specification to generate predictions for the test dataset.

## Key Results

| Model | Number of predictors | Validation MSE |
|---|---:|---:|
| Full OLS model | 12 | 0.4837 |
| AIC-selected model | 6 | 0.3463 |
| BIC-selected model | 3 | 0.3295 |

The BIC-selected model achieved the lowest reported validation MSE among the three specifications while using only three predictors. This highlights the importance of considering both model complexity and predictive performance when selecting a statistical model.

## Tools and Techniques

- **Programming language:** Python
- **Development environment:** Google Colab
- **Statistical modelling:** Ordinary Least Squares (OLS) regression
- **Feature selection:** Exhaustive best subset selection
- **Model selection:** AIC and BIC
- **Model evaluation:** Mean squared error (MSE)
- **Data analysis:** Pandas, NumPy, Statsmodels and Scikit-learn

## Repository Structure

| File | Description |
|---|---|
| `README.md` | Project overview, objectives, methodology, results and tools used. |
| `gdp_growth_model_selection.py` | Python source code for regression modelling, exhaustive best subset selection, AIC/BIC comparison and prediction generation. |
| `ex1_train.csv` | Training dataset used to estimate regression models and perform model selection. |
| `ex1_test.csv` | Test dataset used to generate predictions from the selected model. |
| `ex1_variables.csv` | Variable descriptions for the dataset's economic indicators. |

## Skills Demonstrated

- Statistical modelling and regression analysis
- Feature selection and model comparison
- Information criteria: AIC and BIC
- Predictive performance evaluation
- Python-based data analysis
- Interpretation of statistical results
- Analytical problem-solving

---

*Academic project — Statistical Machine Learning (ECON5129), University of Glasgow.*
