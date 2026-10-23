# GDP Growth Nowcasting Using Statistical Machine Learning

## Project Overview

This project investigates how statistical modelling techniques can be used to predict GDP growth using a set of economic indicators. The analysis compares alternative Ordinary Least Squares (OLS) regression models and examines how model selection criteria can help identify a more parsimonious and predictive specification.

The project was completed as part of the **Statistical Machine Learning (ECON5129)** course at the University of Glasgow.

**Note:** The dataset used in this exercise is simulated and should not be interpreted as real-world economic data.

## Objectives

- Explore the relationship between economic indicators and GDP growth.
- Implement OLS regression for prediction.
- Apply exhaustive best subset selection to compare alternative predictor combinations.
- Use Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) to select models.
- Evaluate predictive performance using mean squared error (MSE).
- Compare model complexity with out-of-sample predictive performance.

## Methodology

The analysis follows these main steps:

1. **Data preparation:** Load the training and test datasets and examine the available economic indicators.
2. **Baseline modelling:** Estimate an OLS regression using the available predictors.
3. **Best subset selection:** Evaluate alternative combinations of predictors to identify candidate models.
4. **Model selection:** Compare specifications selected using AIC and BIC.
5. **Model evaluation:** Assess predictive performance using mean squared error (MSE).
6. **Model comparison:** Examine the trade-off between model complexity and predictive accuracy.

## Key Results

| Model | Number of predictors | Validation MSE |
|---|---:|---:|
| Full OLS model | 12 | 0.4837 |
| AIC-selected model | 6 | 0.3463 |
| BIC-selected model | 3 | 0.3295 |

The BIC-selected model achieved the lowest reported validation MSE among the three specifications, while using only three predictors. This illustrates how a more parsimonious model can outperform a larger specification in predictive evaluation.

These results relate to the simulated dataset used in the exercise and should not be interpreted as evidence of real-world GDP forecasting performance.

## Tools and Techniques

- **Language:** Python
- **Environment:** Jupyter Notebook
- **Statistical modelling:** Ordinary Least Squares (OLS) regression
- **Model selection:** Exhaustive best subset selection, AIC and BIC
- **Evaluation:** Mean squared error (MSE)
- **Data handling and analysis:** Python data analysis libraries

## Repository Structure

```text
GDP-Growth-Nowcasting/
├── README.md
├── GDP_Growth_Nowcasting.ipynb
├── ex1_train.csv
├── ex1_test.csv
└── ex1_variables.csv
```

## How to Run

1. Clone or download this repository.
2. Install Python and Jupyter Notebook.
3. Install the Python libraries required by the notebook.
4. Open `GDP_Growth_Nowcasting.ipynb` in Jupyter Notebook.
5. Run the notebook cells in order.

The CSV files required for the analysis are included in this repository.

## Limitations

The dataset is simulated, so the results do not establish how the selected model would perform on actual economic data. In addition, model-selection and validation procedures should be designed carefully to avoid information leakage and overly optimistic performance estimates.

## Skills Demonstrated

- Statistical modelling and regression analysis
- Feature selection and model comparison
- Information criteria: AIC and BIC
- Predictive performance evaluation
- Python-based data analysis
- Interpretation of statistical results

---

*Academic project — Statistical Machine Learning, University of Glasgow.*
