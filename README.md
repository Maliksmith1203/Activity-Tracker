# Activity Tracker
Activity Tracker is a Python script that allows you to log and keep track of your exercise activities and their associated calorie expenditure. This program utilizes the Nutritionix API to retrieve exercise details and stores the data in a Sheety spreadsheet

## Introduction

Activity Tracker is a command-line tool designed to streamline the process of recording exercise information. It leverages the Nutritionix API to fetch details such as exercise names, duration, and calories burned based on your input. The retrieved data is then stored in a Sheety spreadsheet, providing you with a convenient way to monitor your workout progress.

## Features

- **Exercise Data Retrieval:** Enter the exercises you've performed, and the script retrieves information from the Nutritionix API, including the exercise name, duration, and calories burned.

- **Data Logging:** The script logs exercise data to a Sheety spreadsheet, recording both the date and time of the workout.

- **Environment Variable Support:** Sensitive data, such as API keys and endpoints, are securely managed using environment variables.

## Prerequisites

Before using Activity Tracker, ensure that you have the following prerequisites:

- Python 3.x installed on your system.
- Nutritionix API credentials (APP_ID and API_KEY).
- Sheety API credentials (TOKEN).
- A Sheety spreadsheet URL (SHEETY_URL).

Usage
Configure your environment variables for the Nutritionix and Sheety APIs. Make sure to set the following variables:

APP_ID: Your Nutritionix APP_ID.
API_KEY: Your Nutritionix API_KEY.
TOKEN: Your Sheety API token.
SHEETY_URL: The URL of your Sheety spreadsheet.
Run the script:

bash
Copy code
python activity_tracker.py
Follow the on-screen prompts to input the exercises you've completed.

The script will retrieve exercise details from Nutritionix and log them in your Sheety spreadsheet.

Configuration
You can customize the script's behavior by configuring it through environment variables. Ensure that you have these variables set up correctly in your environment before running the script.
