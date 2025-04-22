# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array and calculate the mean
print("--- Task 1: NumPy Array Mean ---")
numbers = np.arange(1, 11)  # Creates array [1, 2, ..., 10]
mean_value = np.mean(numbers)
print(f"Array: {numbers}")
print(f"Mean: {mean_value}\n")

# Task 2: Load dataset into pandas DataFrame and show statistics
print("--- Task 2: Pandas DataFrame Summary ---")
# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print()

## Task 3: Fetch data from public API
print("--- Task 3: API Data Fetch ---")
try:
    # Using JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    if response.status_code == 200:
        data = response.json()
        print("API Response:")
        print(f"Title of todo item: {data['title']}")
    else:
        print(f"API request failed with status code {response.status_code}")
except Exception as e:
    print(f"Error fetching API data: {e}")
print()

## Task 4: Plot a simple line graph
print("--- Task 4: Matplotlib Line Plot ---")
# Create some data points
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.title('Simple Line Plot of sin(x)')
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()