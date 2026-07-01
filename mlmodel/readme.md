# Run the ML Files from the API access. 

 # Step 3: run FastAPI Server 

 # Install dependencies (if not already)
> pip install fastapi uvicorn scikit-learn

# Run the server
> uvicorn app:app --reload

Step 4: Test the API
Option 1: Use Swagger UI (Built-in)
Go to http://localhost:8000/docs in your browser. You'll see the interactive Swagger UI where you can test the API.

Option 2: Use cURL in Terminal

> curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

# Sample Output: JSON
> {
  "prediction": "setosa",
  "input": {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
}