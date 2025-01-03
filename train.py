import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_csv('respiratory_data.csv')  # Replace 'your_dataset.csv' with the actual file path

# Convert 'Age' to numeric, invalid parsing will be set as NaN
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Now fill missing 'Age' values with the median
data['Age'] = data['Age'].fillna(data['Age'].median())

# Ensure other necessary columns are handled similarly
data['fev1'] = data['fev1'].fillna(data['fev1'].median())
data['fvc'] = data['fvc'].fillna(data['fvc'].median())
data['fev1_fvc_ratio'] = data['fev1_fvc_ratio'].fillna(data['fev1_fvc_ratio'].median())
data['Condition'] = data['Condition'].fillna(data['Condition'].mode()[0])
data['Medication'] = data['Medication'].fillna(data['Medication'].mode()[0])
data['AllergyStatus'] = data['AllergyStatus'].fillna(data['AllergyStatus'].mode()[0])

# Convert categorical columns to numerical using LabelEncoder
label_encoder = LabelEncoder()

# Label encoding for categorical columns
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Condition'] = label_encoder.fit_transform(data['Condition'])
data['Medication'] = label_encoder.fit_transform(data['Medication'])
data['AllergyStatus'] = label_encoder.fit_transform(data['AllergyStatus'])

# Split the dataset into features (X) and target (y)
X = data.drop(columns=['TargetColumn'])  # Replace 'TargetColumn' with the actual target column name
y = data['TargetColumn']  # Replace with the actual target column name

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features (optional)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation (optional)
accuracy = model.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')
