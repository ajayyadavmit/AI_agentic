# train_model.py
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
print("Training Model /. \ | -")
model = RandomForestClassifier()
print("Fitting Model | - \ ")
model.fit(X, y)

# Save model
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as iris_model.pkl")