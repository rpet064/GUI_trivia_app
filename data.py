import requests
AMOUNT = 10
TYPE = "boolean"
CATEGORY = 18,
PARAMETERS = {"amount": AMOUNT, "type": TYPE, "category": CATEGORY}
response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
question_dict = response.json()
question_data = question_dict["results"]