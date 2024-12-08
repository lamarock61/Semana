import requests
import json
from datetime import datetime, timedelta



# Load the credentials file
with open("private.json", "r") as file:
    credentials = json.load(file)

api_key = credentials["api_key"]

print(api_key)

print("coucou")

# Define the URL
url = "https://api.semana.io/v1/bookings"  # Replace with your target URL



# Define the headers
headers = {
    "X-API-key": api_key
}

# Define the start date as the current date
start_date = datetime.now()

# Calculate the end date as start_date + 6 weeks (42 days)
end_date = start_date + timedelta(days=42)

# Define other JSON data fields
json_data = {
    "period": "day",
    "collaboratorId": 22229 #my semana Id
}

# Send POST requests for each date in the range
current_date = start_date
while current_date <= end_date:
    # Set the "type" parameter based on the day of the week
    if current_date.weekday() in (3, 4):  # Thursday or Friday
        json_data["type"] = "remote"
    else:
        json_data["type"] = "office"
        #off / remote / office

    formatted_date = current_date.strftime("%Y-%m-%d")
    json_data["date"] = formatted_date

    response = requests.post(url, headers=headers, json=json_data)

    # Check the response status code
    if response.status_code == 201:
        print(f"Request for date {formatted_date} was successful!")
        print("Response:", response.text)
    else:
        print(f"Request for date {formatted_date} failed with status code:", response.status_code)
        print("Response:", response.text)

    current_date += timedelta(days=1)
