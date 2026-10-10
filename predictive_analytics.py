
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load historical data
df = pd.read_excel("Predictive_Analytics_Historical_Data.xlsx")

print("Original data:")
print(df.head())

# 2. Clean and preprocess the data
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

df = df.dropna(subset=["Date", "Sales"])
df = df.sort_values("Date").drop_duplicates(subset=["Date"])
df = df.reset_index(drop=True)

print("\nMissing values after cleaning:")
print(df[["Date", "Sales"]].isnull().sum())

# 3. Create a time-based feature
df["Month_Number"] = np.arange(len(df))

X = df[["Month_Number"]]
y = df["Sales"]

# 4. Split data chronologically
split_index = int(len(df) * 0.8)
X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# 5. Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict sales for the test period
test_predictions = model.predict(X_test)

# 7. Evaluate model accuracy
mae = mean_absolute_error(y_test, test_predictions)
rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
r2 = r2_score(y_test, test_predictions)

print("\nMODEL EVALUATION")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.3f}")

# 8. Forecast the next 6 months
future_month_numbers = np.arange(len(df), len(df) + 6)
future_predictions = model.predict(
    pd.DataFrame({"Month_Number": future_month_numbers})
)

future_dates = pd.date_range(
    start=df["Date"].max() + pd.offsets.MonthBegin(1),
    periods=6,
    freq="MS"
)

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Sales": np.maximum(0, future_predictions).round(2)
})

print("\nNEXT 6 MONTHS SALES FORECAST")
print(forecast_df)

# 9. Visualize actual sales and predictions
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Sales"], marker="o", label="Historical Sales")
plt.plot(
    df["Date"].iloc[split_index:],
    test_predictions,
    marker="o",
    linestyle="--",
    label="Test Predictions"
)
plt.plot(
    forecast_df["Date"],
    forecast_df["Predicted_Sales"],
    marker="o",
    linestyle="--",
    label="Future Forecast"
)

plt.title("Historical Sales and Future Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Sales_Forecast_Chart.png", dpi=300)
plt.close()
print("Forecast chart saved successfully!")

# 10. Export results to Excel
evaluation_df = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "R2"],
    "Value": [mae, rmse, r2]
})

with pd.ExcelWriter("Predictive_Analytics_Results.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Historical_Data", index=False)
    forecast_df.to_excel(writer, sheet_name="Future_Forecast", index=False)
    evaluation_df.to_excel(writer, sheet_name="Model_Evaluation", index=False)

print("\nProject completed successfully!")
print("Saved: Predictive_Analytics_Results.xlsx")
print("Saved: Sales_Forecast_Chart.png")