import requests

# API endpoint
url = "https://api.openaq.org/v2/locations/2163058?limit=1000"

# API key for authorization
headers = {
    "x-api-key": "b77f00d01a26e10d71d1a8ba139c4df451e644ebca42d0519592b9b7eadfaee2"}

# Sending GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract air quality measurements
    if "results" in data and data["results"]:
        result = data["results"][0]  # Access the first result
        print("Air Quality Parameters:")

        # Iterate through all parameters and print their values
        for measurement in result.get("parameters", []):
            parameter = measurement.get("parameter", "Unknown")
            last_value = measurement.get("lastValue", "N/A")
            unit = measurement.get("unit", "N/A")
            print(f"{parameter.upper()}: {last_value} {unit}")
        else:
            print("No data available for the location.")
else:
    print(f"Failed to fetch data: {response.status_code}")
