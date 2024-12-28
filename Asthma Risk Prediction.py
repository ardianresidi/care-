import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc
import joblib
import requests
from bs4 import BeautifulSoup

# Load your dataset
data = pd.read_csv("D:/Asthma-Risk-Predicition-Using-Machine-Learning-and-Internet-of-Things-main/PEFR_Data_set.csv")
X = data.drop(columns=['Age', 'Height', 'PEFR'])
y = data['PEFR']

# Train the model
model = dtc()
model.fit(X, y)



# Get city input
city = input("Enter City:").strip().lower()

# Construct the URL with the entered city
url = f'https://www.iqair.com/north-macedonia/polog/{city}'

# Print the URL
print(f'Constructed URL: {url}')


try:

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

    r = requests.get(url, headers=headers)

    
    soup = BeautifulSoup(r.content, 'html.parser')

    # Print the entire page content to check
    #Nese don mundesh ta bejsh disable qe mos e postoje krejt HTML
    print(soup.prettify())  # This will print the parsed HTML in a readable format


    

    # Initialize variables
    aqi_dict = []

    # Scrape PM2.5 and PM10 values
    s = soup.find_all(class_="mat-tooltip-trigger pollutant-concentration-value")
    
    if len(s) >= 2:
        pm2 = s[0].text
        pm10 = s[1].text
    else:
        print("Error: Unable to find AQI values.")
        pm2 = input("Enter PM2.5 manually: ")
        pm10 = input("Enter PM10 manually: ")

    # Scrape temperature and humidity
    t = soup.find('div', class_="weather__detail")
    if t:
        y = t.text
        temp_index = y.find('Temperature') + 11
        degree_index = y.find('°')
        temp = y[temp_index:degree_index].strip()

        hum_index = y.find('Humidity') + 8
        perc_index = y.find('%')
        hum = y[hum_index:perc_index].strip()
    else:
        print("Error: Unable to find temperature or humidity.")
        temp = input("Enter temperature manually: ")
        hum = input("Enter humidity manually: ")

    # Input Gender and Prediction
    g = int(input("Enter Gender (1-Male/0-Female): "))
    prediction = model.predict([[g, temp, hum, pm2, pm10]])
    predicted_pefr = prediction[0]

    # Input actual PEFR value
    actual_pefr = float(input("Enter Actual PEFR value: "))

    # Calculate percentage PEFR and display risk level
    perpefr = (actual_pefr / predicted_pefr) * 100
    if perpefr >= 80:
        print('SAFE')
    elif perpefr >= 50:
        print('MODERATE')
    else:
        print('RISK')

except Exception as e:
    print("An error occurred:", e)
