import mlflow
from mlflow.sklearn import log_model
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Training data
X = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])

with mlflow.start_run():

    # Log parameters
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("training_samples", len(X))

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Log metrics
    mlflow.log_metric("coef", float(model.coef_[0]))
    mlflow.log_metric("intercept", float(model.intercept_))

    # Save model for Docker
    joblib.dump(model, "model.pkl")

    # Log model to MLflow
    log_model(model, "model")

print("Training complete. Model saved and logged to MLflow.")