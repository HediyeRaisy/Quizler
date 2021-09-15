import requests

result = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
result.raise_for_status()
result = result.json()

question_data = result['results']

