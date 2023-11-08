import json
import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["Nutrionix_Api_Key"]
TOKEN = os.environ["TOKEN"]
NUTRITIONIX_ENDPOINT = os.environ["Nutri_Endpoint"]
SHEETY_URL = os.environ["SHEETY_URL"]
today = datetime.now()

# Headers for Nutritionix API
nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

# Input the exercise data
exercise_data = input("What exercises you did?")

# Create the request data for Nutritionix API
nutritionix_request_data = {
    "query": exercise_data,
}

# Convert the request data to JSON format
nutritionix_json_data = json.dumps(nutritionix_request_data)

# Make a POST request to the Nutritionix API
nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, data=nutritionix_json_data)

if nutritionix_response.status_code == 200:
    # The request to Nutritionix was successful
    nutritionix_data = nutritionix_response.json()
    print(json.dumps(nutritionix_data, indent=4))

    # Extract relevant exercise data from the response
    exercises = nutritionix_data.get("exercises", [])
    print(exercises)


    for exercise_info in exercises:
        # Create the Sheety body with the extracted exercise information
        sheety_body = {
            "workout": {
                "date": f"{today.strftime('%Y/%m/%d')}",
                "time":f"{today.strftime('%H:%M:%S')}",
                "exercise": exercise_info.get("name", "N/A"),
                "duration": exercise_info.get('duration_min',0),
                "calories": exercise_info.get("nf_calories", "N/A"),
            }
        }

        # Make a POST request to the Sheety API for each exercise
        sheety_headers = {
            "Content-Type": "application/json",
            "Authorization": TOKEN
        }

        sheety_json_data = json.dumps(sheety_body)

        sheety_response = requests.post(url=SHEETY_URL, headers=sheety_headers, data=sheety_json_data)


        if sheety_response.status_code == 200:
            print(f"Exercise data successfully added to Sheety for: {exercise_info.get('name', 'N/A')}")
        else:
            print(f"Error adding data to Sheety for: {exercise_info.get('name', 'N/A')}: {sheety_response.status_code} - {sheety_response.text}")

else:
    # Something went wrong with the Nutritionix request
    print(f"Error with Nutritionix API: {nutritionix_response.status_code} - {nutritionix_response.text}")
