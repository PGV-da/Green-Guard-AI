import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('data/crop_data.csv')

# Select relevant columns for modeling
X = data[['N', 'P', 'K', 'Zn', 'Mg', 'S', 'pH', 'Rainfall', 'Temperature', 'Humidity']]
y = data['Crop_Subcategory']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

def recommend_crop(attributes):
    """Predicts the best crop based on soil attributes."""
    attribute_values = [list(attributes.values())]
    crop = rf_model.predict(attribute_values)[0]
    return crop
