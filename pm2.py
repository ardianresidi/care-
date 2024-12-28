import requests
from bs4 import BeautifulSoup

# Get city input
city = input("Enter City:").strip().lower()

# Construct the URL for the entered city
url = f'https://www.iqair.com/north-macedonia/polog/{city}'

# Set headers to mimic a real browser (bypasses 403 Forbidden errors)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Make the request to fetch the HTML page
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing the PM2.5 value (adjust class name if necessary)
    try:
        # Find the element with the PM2.5 value
        pm25_element = soup.find('div', class_='pollutant-concentration-value')
        pm25_value = pm25_element.text.strip() if pm25_element else "PM2.5 data not found."

        print(f"PM2.5 Value for {city.capitalize()}: {pm25_value}")
    except Exception as e:
        print(f"Error extracting PM2.5 value: {e}")
else:
    print(f"Failed to retrieve data for {city}. Status code: {response.status_code}")
