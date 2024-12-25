import requests
from datetime import datetime, timedelta
import os


# Define your LINE Notify token
ACCESS_TOKEN = "XlmdyvYZIsgeLhJMZ3xbU94DIqOnCgHxOdIUQ0b70ao"
LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"

today = datetime.now()
# Add 4 days
sunday_time = today + timedelta(days=4)

print(f"today: {today}")
print(f"sunday: {sunday_time}")

# Format it as MM/DD
formatted_date = sunday_time.strftime("%m/%d")

# Message to be sent
message = f"{formatted_date} 主日需要便當，麻煩大家在週六中午12點以前登記，謝謝～🍱⏰🙏\n 1. \n 2. "

# Set headers and data payload
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
data = {"message": message}

# Send POST request to LINE Notify API
response = requests.post(LINE_NOTIFY_API, headers=headers, data=data)

# Check the response status
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send message:", response.status_code, response.json())
