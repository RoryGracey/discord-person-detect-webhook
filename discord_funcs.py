import datetime
import json
import requests



def theres_somebody_at_the_door(url, alert_id):
	file = {
		"file1": open("images/fatherrr.gif", "rb")
	}
	requests.post(url=url, data={"payload_json": json.dumps({"content": f"<@{alert_id}>"})}, files=file)


	payload_json = {
		"content": f"Sneaky Sausage Detected at {datetime.datetime.now()}"
	}

	file = {
		"file1": open("images/detected_person.jpg", "rb")
	}
	response = requests.post(url, data={"payload_json": json.dumps(payload_json)}, files=file)

	if response.status_code == 200:
		print("Files uploaded successfully!")
	else:
		print(f"Error: {response.status_code} - {response.text}")
