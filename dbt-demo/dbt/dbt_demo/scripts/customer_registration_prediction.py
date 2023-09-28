import pandas as pd
from sklearn.linear_model import LogisticRegression

ref_df = ref('customers')

# fill missing values with 0
ref_df.fillna(0, inplace=True)

# Extract the input and output variables
X = ref_df[["no_of_orders", "total_amount"]]
y = ref_df["is_registered"]

# Create a logstic regression model
model = LogisticRegression()

# Fit the model to the data
model.fit(X, y)

# Print the intercept and coefficient
print('Intercept:', model.intercept_)
print('Coefficient:', model.coef_)

ref_df['is_predicted_to_register'] = model.predict(X)

# Upload a `pandas.DataFrame` back to the datawarehouse
write_to_model(ref_df[['customer_id','is_predicted_to_register']])