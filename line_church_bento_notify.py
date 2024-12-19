import requests
from datetime import datetime
import os


# Define your LINE Notify token
ACCESS_TOKEN = "MlqyxqdjH20tfLOAOCNclnn5f7T8BT50MePKugDvVnW"
# os.getenv("ACCESS_TOKEN")
LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"

today = datetime.now()

# Format it as MM/DD
formatted_date = today.strftime("%m/%d")

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
