import requests

parameters = {
    "amount": 25,
    "type": "boolean"
}

questions_api = requests.get(url='https://opentdb.com/api.php', params=parameters)
questions_api.raise_for_status()
question_data = questions_api.json()["results"]
