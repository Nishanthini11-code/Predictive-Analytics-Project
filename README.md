# Predictive Analytics Using Historical Data

## Project Overview

This project uses machine learning to analyze historical sales data and forecast future sales trends using Python and Linear Regression.

## Objectives

* Clean and preprocess historical sales data.
* Build a predictive model using Linear Regression.
* Evaluate model performance using MAE, RMSE, and R-squared.
* Visualize historical sales and future predictions.
* Export forecasts and evaluation metrics to Excel.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Excel

## Dataset

The historical dataset contains:

* Date
* Sales
* Marketing Spend
* Orders

The model uses historical dates and sales values to predict future sales.

## Project Workflow

1. Load the historical dataset.
2. Clean missing and duplicate records.
3. Convert dates and sales values to appropriate data types.
4. Split the data chronologically into training and testing sets.
5. Train a Linear Regression model.
6. Evaluate model performance.
7. Forecast sales for the next six months.
8. Visualize historical sales and predicted sales.
9. Export results to Excel.

## Output Files

* `Predictive_Analytics_Results.xlsx` — cleaned data, forecasts, and model evaluation metrics.
* `Sales_Forecast_Chart.png` — visualization of historical sales and predictions.
* `predictive_analytics.py` — Python source code.
* `Predictive_Analytics_Historical_Data.xlsx` — input dataset.

## How to Run

1. Install Python.

2. Install the required libraries:

   `pip install pandas numpy matplotlib scikit-learn openpyxl`

3. Place the dataset and Python script in the same folder.

4. Run:

   `python predictive_analytics.py`

## Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R-squared (R²)

Note: Model performance depends on the dataset and the relationship between time and sales. Forecasts are estimates, not guaranteed future results.

## Conclusion

This project demonstrates how historical data and machine learning can support sales forecasting, trend analysis, and data-driven business decisions.
